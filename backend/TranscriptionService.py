from openai import OpenAI
import dotenv, os, base64, io, re

dotenv.load_dotenv()

class TranscriptionService:

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def transcribe_file(self, binary_string):
        if binary_string.startswith("data:"):
            binary_string = binary_string.split(",")[1]

        decoded_bytes = base64.b64decode(binary_string)
        audio_file = io.BytesIO(decoded_bytes)
        audio_file.name = "audio.wav"

        transcription = self.client.audio.transcriptions.create(
            file = audio_file,
            model="whisper-1",
            response_format="verbose_json",
        )

        full_text = transcription.text
        match = re.search(r"on line (\d+),?\s+(.*)", full_text, flags=re.IGNORECASE)

        if match:
            line_number = int(match.group(1))
            instruction = match.group(2).strip()
        else:
            line_number = None
            instruction = full_text

        return instruction, line_number