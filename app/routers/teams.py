from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..db import get_session
from ..models import Team

router = APIRouter(prefix="/teams", tags=["teams"])

@router.post("", response_model=Team)
def create_team(payload: Team, session: Session = Depends(get_session)):
    # name muss unique sein
    exists = session.exec(select(Team).where(Team.name == payload.name)).first()
    if exists:
        raise HTTPException(status_code=400, detail="Teamname existiert bereits")
    team = Team(name=payload.name)
    session.add(team)
    session.commit()
    session.refresh(team)
    return team

@router.get("", response_model=list[Team])
def list_teams(session: Session = Depends(get_session)):
    return session.exec(select(Team)).all()
