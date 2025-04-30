from fastapi import FastAPI, Request, HTTPException
import os, dotenv, psycopg2
from contextlib import asynccontextmanager
from TranscriptionService import TranscriptionService
from fastapi.middleware.cors import CORSMiddleware
from ModelService import ModelService

dotenv.load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # code to run on startup
    conn = get_db_connection()
    cur = conn.cursor()
    print("Connected to database!")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS transcriptions (
            id SERIAL PRIMARY KEY,
            token TEXT,
            created_at TIMESTAMP DEFAULT NOW(),
            code TEXT NOT NULL,
            line_number INTEGER
        );
    """)
    conn.commit()
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
        port=int(os.getenv("DATABASE_PORT", 5432)),
        database=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
    )
    return conn

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

    transcription_service = TranscriptionService()
    instruction, line_number = transcription_service.transcribe_file(binary_string)
    
    model_service = ModelService()
    code = model_service.generate_code(instruction=instruction)

    con = get_db_connection()
    cur = con.cursor()

    if line_number:
        cur.execute("""
            INSERT INTO transcriptions (token, code, line_number)
            VALUES (%s, %s, %s)
        """, (token, code, line_number))
    else:
        cur.execute("""
            INSERT INTO transcriptions (token, code)
            VALUES (%s, %s)
        """, (token, code))

    con.commit()
    cur.close()
    con.close()
    
    return {"status": "success"}

@app.get("/poll-data/{token}")
async def poll_data(token: str):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT code, line_number
        FROM transcriptions
        WHERE token = %s
        ORDER BY created_at ASC
        LIMIT 1;
    """, (token,))
    row = cur.fetchone()

    if not row:
        return {"code": None}
    
    code, line_number = row

    cur.execute("""
        DELETE FROM transcriptions
        WHERE token = %s AND code = %s
    """, (token, code))
    conn.commit()

    cur.close()
    conn.close()

    return {"code": code, "line_number": line_number}

@app.get("/transcriptions")
async def get_all_transcriptions():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM transcriptions
        ORDER BY created_at DESC;
    """)
    rows = cur.fetchall()

    cur.close()
    conn.close()

    results = []
    for row in rows:
        results.append({
            "id": row[0],
            "token": row[1],
            "created_at": row[2].isoformat(),
            "code": row[3],
            "line_number": row[4],
        })

    return {"transcriptions": results}