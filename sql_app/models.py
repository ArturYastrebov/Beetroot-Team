from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import relationship

from .database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(200))
    owner_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))

    owner = relationship("User", backref="messages")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(50))
    chat_id = Column(BigInteger)

    message = relationship("Message", backref="users", cascade="all, delete", passive_deletes=True)
