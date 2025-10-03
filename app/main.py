from fastapi import FastAPI
from .db import init_db

app = FastAPI(title="eSport Verwaltung API")

# beim Start Tabellen erzeugen
init_db()

@app.get("/")
def root():
    return {"status": "ok", "db": "sqlite"}
