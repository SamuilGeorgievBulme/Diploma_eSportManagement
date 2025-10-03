from sqlmodel import SQLModel, create_engine, Session

# SQLite-Datei im Projektverzeichnis
sqlite_url = "sqlite:///./esport.db"
engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})

# Tabellen erstellen
def init_db():
    SQLModel.metadata.create_all(engine)

# Session bereitstellen (für Queries in Routern)
def get_session():
    with Session(engine) as session:
        yield session
