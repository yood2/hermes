from fastapi import FastAPI
from app.routes import users
from app.persist.connection import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Hello World"}