from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker  # , declarative_base
import os
from dotenv import load_dotenv

current_dir = os.getcwd()  # Получаем текущую директорию
parent_dir = os.path.dirname(current_dir)  # Получаем родительскую директорию
file_path = os.path.join(parent_dir, '.env')  # Получаем путь к файлу в родительской директории

# Connect the path with your '.env' file name
load_dotenv(file_path)


SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRESS_URL")



engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

