from typing import Union

from fastapi import FastAPI

app = FastAPI()


user_info = [
    {
    "username": "blank_user",
    "email": "blankuser@example.com"
    },
    {
    "username": "1_user_demo",
    "email": "1userdemo@example.com"
    },
    {
    "username": "2_user_demo",
    "email": "2userdemo@example.com"
    },
    {
    "username": "3_user_demo",
    "email": "3userdemo@example.com"
    }
]

@app.get("/")
def read_root():
    return {"api docs url": "domain/docs"}

@app.get("/user")
def read_users():
    return user_info

@app.get("/user/{id}")
def read_user(id: int):
    return user_info[id]

@app.post("/user")
def create_user(user: dict):
    user_info.append(user)
    return user_info
