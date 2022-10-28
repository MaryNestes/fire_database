from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Numeric, Integer, DateTime, ForeignKey

# базовый класс для таблиц бд
Base = declarative_base()

class DateTm(Base):
    __tablename__ = "date_time"

    id = Column(Integer, primary_key=True, unique=True)
    date = Column(DateTime(timezone=False), unique=True)


class FireValue(Base):
    __tablename__ = "fire_values"

    id = Column(Integer, primary_key=True, unique=True)
    temperature = Column(Numeric(5, 2))
    longitude = Column(Numeric(5, 2))
    latitude = Column(Numeric(5, 2))
    date_id = Column(Integer, ForeignKey('date_time.id'))
