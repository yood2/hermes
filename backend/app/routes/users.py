from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from ..models.user import User
from ..persist.connection import get_session

router = APIRouter()

@router.post('/', response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    db_user = User(user_id=user.user_id)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@router.get('/{user_id}', response_model=User)
def get_user(user_id: str, session: Session = Depends(get_session)):
    statement = select(User).where(User.user_id == user_id)
    user = session.exec(statement).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user