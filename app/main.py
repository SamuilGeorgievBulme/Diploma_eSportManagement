from fastapi import FastAPI
from .db import init_db
from .routers.teams import router as teams_router
from .routers.spiele import router as spiele_router  

app = FastAPI(title="eSport Verwaltung API (SQLite)")
init_db()

app.include_router(teams_router)
app.include_router(spiele_router)  

@app.get("/")
def root():
    return {"status": "ok"}
