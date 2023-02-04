from typing import List, Union

from pydantic import BaseModel


class MessageBase(BaseModel):
    text: str
    owner_id: int

class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int


    class Config:
        orm_mode = True


class UserBase(BaseModel):
    chat_id: int



class UserCreate(UserBase):
    nickname: str


class User(UserCreate):
    id: int
    messages: List[Message] = []

    class Config:
        orm_mode = True
