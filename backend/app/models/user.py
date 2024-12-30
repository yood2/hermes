from pydantic import BaseModel
from typing import Dict

class User(BaseModel):
    user_id: str
    portfolio: Dict = {}
