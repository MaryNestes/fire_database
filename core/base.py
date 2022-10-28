from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cofig import DB_URL

# содание движка для бд
engine = create_engine(
    DB_URL
)

# создание класса сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




