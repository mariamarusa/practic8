from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Подключение к базе данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./catalog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()