from typing import Optional
from sqlmodel import SQLModel, Field

class Spiel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=64)
    genre: str | None = Field(default=None, max_length=64)
