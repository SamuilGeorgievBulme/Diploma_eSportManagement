from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, SQLModel
from ..db import get_session
from ..models import Spiel
from typing import Optional

class SpielUpdate(SQLModel):
    name: str
    genre: Optional[str] = None

router = APIRouter(prefix="/spiele", tags=["spiele"])

@router.post("", response_model=Spiel)
def create_spiel(payload: Spiel, session: Session = Depends(get_session)):
    exists = session.exec(
        select(Spiel).where(Spiel.name == payload.name, Spiel.genre == payload.genre)
    ).first()
    if exists:
        raise HTTPException(400, detail="Spiel existiert bereits")
    s = Spiel(name=payload.name, genre=payload.genre)
    session.add(s)
    session.commit()
    session.refresh(s)
    return s

@router.get("", response_model=list[Spiel])
def list_spiele(session: Session = Depends(get_session)):
    return session.exec(select(Spiel)).all()

@router.get("/{spiel_id}", response_model=Spiel)
def get_spiel(spiel_id: int, session: Session = Depends(get_session)):
    obj = session.get(Spiel, spiel_id)
    if not obj:
        raise HTTPException(404, "Nicht gefunden")
    return obj

@router.put("/{spiel_id}", response_model=Spiel)
def update_spiel(spiel_id: int, payload: SpielUpdate, session: Session = Depends(get_session)):
    obj = session.get(Spiel, spiel_id)
    if not obj:
        raise HTTPException(404, "Nicht gefunden")
    obj.name = payload.name
    obj.genre = payload.genre
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.delete("/{spiel_id}")
def delete_spiel(spiel_id: int, session: Session = Depends(get_session)):
    obj = session.get(Spiel, spiel_id)
    if not obj:
        raise HTTPException(404, "Nicht gefunden")
    session.delete(obj)
    session.commit()
    return {"ok": True}
