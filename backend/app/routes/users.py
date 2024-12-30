from fastapi import APIRouter
import json
from typing import List
from ..models.user import User

router = APIRouter()

USER_DATABASE = '../data/users.json'

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
    users.append(user)
    save_users(users)
    return user