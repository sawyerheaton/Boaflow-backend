from fastapi import FastAPI
from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

@app.get("/")
def health():
    return {"status": "Boaflow backend live"}

@app.post("/test-insert")
def test_insert():
    supabase.table("leads").insert({
        "company_name": "Example Co",
        "website": "https://example.com",
        "job_title": "Virtual Assistant",
        "job_url": "https://example.com/careers",
        "va_fit_score": 90,
        "contact_role": "Operations Manager"
    }).execute()

    return {"message": "Inserted test lead"}
