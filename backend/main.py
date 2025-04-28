from fastapi import FastAPI, Request, HTTPException
import os, dotenv, psycopg2
from contextlib import asynccontextmanager
from TranscriptionService import TranscriptionService
from fastapi.middleware.cors import CORSMiddleware

dotenv.load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # code to run on startup
    conn = get_db_connection()
    cur = conn.cursor()
    print("Connected to database!")

    # cur.execute("""
    #     CREATE TABLE IF NOT EXISTS transcriptions (
    #         id PRIMARY KEY,
    #         created_at TIMESTAMP DEFAULT NOW(),
    #         transcription TEXT
    #     );
    # """)
    # conn.commit()
    cur.close()
    conn.close()

    yield

# python -m uvicorn main:app --reload
app = FastAPI(lifespan=lifespan)

origins = [
    "https://microphone-project.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DATABASE_HOST"),
        port=int(os.getenv("DATABASE_PORT")),
        database=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
    )
    return conn

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/db-test")
def test_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return {"server_time": str(result[0])}

@app.post("/upload-audio")
async def upload_audio(request: Request):
    try:
        body = await request.json()
        token = body["token"]
        binary_string: str = body["audioBase64"]
    except:
        raise HTTPException(status_code=400, detail="Body format failed")

    transcriptionService = TranscriptionService()
    transcription = transcriptionService.transcribe_file(binary_string)

    # TODO: put the transcription into the database with the current timestamp (should be defaulted to now) and the token as the primary key
    return {"transcription": transcription}

@app.get("/poll-data/{token}")
async def poll_data(token: str):
    code = None
    # we want the latest, not-yet read transcription from the database 
    return {"code": code}