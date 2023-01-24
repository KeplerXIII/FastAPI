import typing

from fastapi import FastAPI
import pydantic

app = FastAPI()


class User(pydantic.BaseModel):
    id: int
    username: str
    password: str


u1 = User(id=1, username='admin', password='admin')

users: typing.List[User] = []


@app.get("/users", response_model=typing.List[User])
def get_users():
    return users

@app.post('/users', response_model=typing.List[User])
def create_user(user: User):
    users.append(user)
    return users
