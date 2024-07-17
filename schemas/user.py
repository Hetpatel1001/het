from pydantic import BaseModel

class User(BaseModel):
    username: str
    firstname: str
    lastname: str
    pincode: int
    email: str

