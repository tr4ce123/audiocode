from transformers import T5ForConditionalGeneration, RobertaTokenizer

class ModelService:
    def __init__(self):
        self.model = T5ForConditionalGeneration.from_pretrained("../finetuned_model")
        self.tokenizer = RobertaTokenizer.from_pretrained("../finetuned_model")

    def generate_code(self, instruction: str) -> str:
        text = "translate instruction to code: " + instruction.strip()
        enc  = self.tokenizer(text, return_tensors="pt")
        out  = self.model.generate(
            **enc,
            max_new_tokens=64,
            num_beams=4,
            early_stopping=True,
        )
        return self.tokenizer.decode(out[0], skip_special_tokens=True)
