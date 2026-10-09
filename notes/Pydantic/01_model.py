from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {"id": 101, "name": "Learner", "is_active": True}

user = User(**input_data)   # to upack dictionary value we need to use two asterick with input_data

print(user)
