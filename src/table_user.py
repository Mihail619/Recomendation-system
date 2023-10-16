from sqlalchemy import Column, String, Integer, func, desc

from database import Base, SessionLocal

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, name='id', primary_key=True)
    age = Column(Integer, name='age')
    city = Column(String, name='city')
    country = Column(String, name='country')
    experiment_group = Column(Integer, name='exp_group')
    gender = Column(Integer, name='gender')
    os = Column(String, name='os')
    source = Column(String, name='source')

if __name__ == "__main__":
    pass
