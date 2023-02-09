from fastapi import FastAPI, status, Depends, HTTPException

from aiogram_app.main import bot
from .database import engine, SessionLocal
from . import crud, models, schemas
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        yield db


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_chat_id(db, chat_id=str(user.chat_id))
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat_id already registered")
    return crud.create_user(db=db, user=user)


@app.patch("/users/", status_code=status.HTTP_200_OK)
async def update_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_chat_id(db, chat_id=str(user.chat_id))
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This chat_id not founded")
    else:
        return crud.update_user_nickname_by_chat_id(db=db, user=user)


@app.delete("/users/", status_code=status.HTTP_200_OK)
async def update_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_chat_id(db, chat_id=str(user.chat_id))
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This chat_id not founded")
    else:
        return crud.delete_user_by_chat_id(db=db, chat_id=user.chat_id)


@app.get("/users/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/")
async def start():
    await bot.send_message(634832505, "Hi")
    return {"message": "Hey, wats up!"}


@app.post("/send_message_by_chat_id/")
async def send_message(message: schemas.MessageCreate):
    await bot.send_message(message.owner_id, message.text)


@app.post("/send_message_all_user_in_db/")
async def send_message_all_user_in_db(message: schemas.MessageBase, db: Session = Depends(get_db)):
    users = crud.get_users(db)
    if not users:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="We have not users in DB")
    else:
        for user in users:
            await bot.send_message(user.chat_id, message.text)


@app.post("/message/", status_code=status.HTTP_201_CREATED)
async def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=message.owner_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"We dont have user with {message.owner_id} id"
        )
    return crud.create_message(db=db, message=message)


@app.get("/message/", response_model=list[schemas.Message])
async def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = crud.get_message(db, skip=skip, limit=limit)
    return messages
