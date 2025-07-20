from typing import TypedDict


class User(TypedDict):
    id: int
    name: str
    email: str


newPerson: User = {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}

