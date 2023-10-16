import datetime

from pydantic import BaseModel

#Создаются классы для валидации для запроса от эндпоинтов. Нужно импортировать в app
class UserGet(BaseModel):
    id: int
    age: int
    city: str
    country: str
    experiment_group: int
    gender: int
    os: str
    source: str

    class Config:
        orm_mode = True

class PostGet(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True

class FeedGet(BaseModel):
    action: str
    post_id: int
    time: datetime.datetime
    user_id: int
    user: UserGet
    post: PostGet

    class Config:
        orm_mode = True