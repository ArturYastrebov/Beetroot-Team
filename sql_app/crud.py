from sqlalchemy.orm import Session

from . import models, schemas


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_nickname(db: Session, nickname: str):
    return db.query(models.User).filter(models.User.nickname == nickname).first()


def get_user_by_chat_id(db: Session, chat_id: str):
    return db.query(models.User).filter(models.User.chat_id == chat_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(chat_id=user.chat_id, nickname=user.nickname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user_by_chat_id(db: Session, chat_id: int):
    db_user = db.query(models.User).filter(models.User.chat_id == chat_id).delete(synchronize_session='evaluate')
    db.commit()
    return db_user


def update_user_nickname_by_chat_id(db: Session, user: schemas.UserCreate):
    # db_user = get_user_by_chat_id(db, chat_id=str(user.chat_id))
    db_user = db.query(models.User).filter(models.User.chat_id == user.chat_id).update({models.User.nickname: user.nickname},
        synchronize_session='evaluate')
    # db_user.nickname = user.nickname
    db.commit()
    # db.refresh(db_user)
    return db_user


def get_message(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Message).offset(skip).limit(limit).all()


# def get_message_by_user_id(db: Session, user_id: int):
#     return db.query(models.Message).filter(models.Message.owner_id == user_id).all()

def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(text=message.text, owner_id=message.owner_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
