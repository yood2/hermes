from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from ..models.user import User
from ..persist.connection import get_session
from datetime import datetime

router = APIRouter()

@router.post('/', response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get('/{name}', response_model=User)
def get_user(name: str, session: Session = Depends(get_session)):
    statement = select(User).where(User.name == name)
    user = session.exec(statement).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user