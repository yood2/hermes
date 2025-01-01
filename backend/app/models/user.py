from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    def __init__(self, user_id: str):
        self.user_id = self.validate_user_id(user_id)
        self.created_at = datetime.utcnow()

    def validate_user_id(self, user_id):
        if not user_id:
            raise ValueError("User ID cannot be empty")
        if not isinstance(user_id, str):
            raise ValueError("User ID must be a string")
        if len(user_id) > 10:
            raise ValueError("User ID cannot be longer than 10 characters")
        return user_id