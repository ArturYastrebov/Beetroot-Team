from typing import List

from pydantic import BaseModel


class MessageBase(BaseModel):
    text: str


class MessageCreate(MessageBase):
    owner_id: int


class Message(MessageCreate):
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
