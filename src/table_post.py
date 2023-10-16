from sqlalchemy import Column, Float, Integer, String, desc
from sqlalchemy.orm import relationship

from database import Base, SessionLocal


class Post(Base):
    __tablename__ = "post"
    # __table_args__ = {"schema": ""}
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)


if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    session = SessionLocal()
    result = []
    for post in session.query(Post) \
            .filter(Post.topic == "business") \
            .order_by(desc(Post.id)) \
            .limit(10) \
            .all():
        result.append(post.id)
    print(result)
