from pydantic import BaseModel
from typing import Dict
from pydantic import validator

'''
    User Model
    ---------
    Represents a user in the system.

    Attributes:
        user_id: str
        portfolio: Dict
    
    Methods:
        __init__: Initialize a new user and confirms the user_id and portfolio values are valid.
        validate_user_id: Validate the user_id value (has less than 10 characters).
        validate_portfolio: Validate the portfolio value (is a dictionary).
'''
class User(BaseModel):
    user_id: str
    portfolio: Dict = {}

    @validator('user_id')
    def validate_user_id(cls, v):
        if not v:
            raise ValueError("User ID cannot be empty")
        if len(v) > 10:
            raise ValueError("User ID cannot be longer than 10 characters")
        if not isinstance(v, str):
            raise ValueError("User ID must be a string")
        return v
