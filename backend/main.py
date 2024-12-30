from fastapi import FastAPI

app = FastAPI()

USER_DATABASE = '../data/users.json'

@app.get("/")
def read_root():
    return {"message": "Hello World"}

def get_users():
    try:
        with open(USER_DATABASE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users):
    with open(USER_DATABASE, 'w') as file:
        json.dump(users, file)

@app.post('/users')
def create_user(user: User):
    users = get_users()
    users.append(user)
    save_users(users)
    return user