from fastapi import APIRouter, HTTPException
import json
from typing import List
from ..models.user import User
import os

router = APIRouter()

# Get the absolute path to the data directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
USER_DATABASE = os.path.join(BASE_DIR, 'data', 'users.json')

# Create data directory if it doesn't exist
os.makedirs(os.path.dirname(USER_DATABASE), exist_ok=True)

def get_users():
    try:
        with open(USER_DATABASE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users):
    with open(USER_DATABASE, 'w') as file:
        json.dump(users, file)

@router.post('/', response_model=User)
def create_user(user: User):
    users = get_users()
    users.append(user.dict())
    save_users(users)
    return user

@router.get('/{user_id}', response_model=User)
def get_user(user_id: str):
    users = get_users()
    user = next((u for u in users if u['user_id'] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user