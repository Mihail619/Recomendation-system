import psycopg2
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy import desc, func
from sqlalchemy.orm import Session
from loguru import logger
import os
import uvicorn
from datetime import datetime
from dotenv import load_dotenv

from table_user import User
from table_post import Post
from table_feed import Feed
from schema import (
    UserGet,
    PostGet,
    FeedGet,
)  # импортируем классы для валидации запросов
import Load_model, Load_sql, Predictions
from database import SessionLocal


# Подгружаем модель
model = Load_model.model
print("Модель загружена!")

# Подгружаем датасет
model_data = Load_sql.load_features()
print("Датасет для предсказаний загружен!!")


# объявляем пиложение
app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get("/", response_model=List[PostGet])
def recommended_posts(
    id: int, 
    time: datetime = None,
    limit: int = 10, 
    db: Session = Depends(get_db)
) -> List[PostGet]:
    """эндпоинт выводит список рекомендаций постов для юзера, основанные на его предыдущих действиях.
    рекомендации выводятся моделью model из Load_model и датафрейма модели"""

    recomend_list = Predictions.prediction_list(
        user_id=id, model=model, data=model_data, limit=limit
    )
    print(recomend_list)
    result = db.query(Post).filter(Post.id.in_(recomend_list)).all()
    if result == []:
        raise HTTPException(404, detail="User not found")
    else:
        return result


@app.get("/user/{id}", response_model=UserGet)
# response_model Указывает что модель ответа соответствует классу валидации UserGet,
# т.е. проводим валидацию
def get_user(id: int, db: Session = Depends(get_db)):
    """эндпоинт который выводит данные о юзере по id юзера"""
    result = db.query(User).filter(User.id == id).one_or_none()
    logger.info(result)
    if result == None:
        raise HTTPException(404, detail="Item not found")
    else:
        return result


@app.get("/post/{id}", response_model=PostGet)
def get_user(id: int, db: Session = Depends(get_db)):
    """эндпоинт который выводит данные о посте по id поста"""
    result = db.query(Post).filter(Post.id == id).one_or_none()
    if result == None:
        raise HTTPException(404, detail="Item not found")
    else:
        return result


@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_user_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    """эндпоинт выводит данные о активности юзера по id юзера.
    т.е. о постах, с которыми взаимодействовал юзер.
    количество постов - limit"""
    response = (
        db.query(Feed)
        .filter(Feed.user_id == id)
        .order_by(desc(Feed.time))
        .limit(limit)
        .all()
    )
    if len(response) == 0:
        raise HTTPException(200, detail=[])
    else:
        return response


@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_post_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    """эндпоинт выводит данные о действиях которые совершались с постом по id поста.
    т.е. о постах, с которыми взаимодействовал юзер.
    количество постов - limit"""
    response = (
        db.query(Feed)
        .filter(Feed.post_id == id)
        .order_by(desc(Feed.time))
        .limit(limit)
        .all()
    )
    if len(response) == 0:
        raise HTTPException(200, detail=[])
    else:
        return response


if __name__ == "__main__":
    load_dotenv()
    # для запуска приложения для github
    uvicorn.run(app)
