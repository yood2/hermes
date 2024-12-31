from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    created_at: datetime = Field(default=datetime.now())

    @field_validator('name')
    @classmethod
    def validate_name(cls, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name cannot be empty")
        if len(value) > 10:
            raise ValueError("Name cannot be longer than 10 characters")
        return value