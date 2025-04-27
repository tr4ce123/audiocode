from fastapi import FastAPI
import dotenv
import psycopg2
import os
from contextlib import asynccontextmanager

dotenv.load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # code to run on startup
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS audio_chunks (
            id SERIAL PRIMARY KEY,
            created_at TIMESTAMP DEFAULT NOW(),
            filename TEXT NOT NULL,
            content BYTEA      
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

    yield

# python -m uvicorn main:app --reload
app = FastAPI(lifespan=lifespan)


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