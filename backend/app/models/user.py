from sqlmodel import SQLModel, Field
from typing import Dict, Optional
from pydantic import validator
from sqlalchemy import JSON

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)
    portfolio: Dict = Field(default={}, sa_type=JSON)

    @validator('user_id')
    def validate_user_id(cls, v):
        if not v:
            raise ValueError("User ID cannot be empty")
        if len(v) > 10:
            raise ValueError("User ID cannot be longer than 10 characters")
        if not isinstance(v, str):
            raise ValueError("User ID must be a string")
        return v
