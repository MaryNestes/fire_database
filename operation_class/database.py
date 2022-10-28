import geopandas as gpd
from datetime import datetime
from sqlalchemy import inspect

from core.base import SessionLocal, engine
from core.tables import Base, DateTm, FireValue


class WriteToDB:
    def __init__(self):
        '''Иницилизируем сессию для работы с бд'''
        self.session = SessionLocal()

    def crate_tables(self):
        '''Проверяем необходимое наличие таблиц в бд и если необходимо создаем'''
        tables_names = inspect(engine).get_table_names()
        if not DateTm.__tablename__ in tables_names or not FireValue.__tablename__ in tables_names:
            Base.metadata.create_all(engine)
            print("tables was created")

    def write_data(self, date: datetime, df: gpd.GeoDataFrame):
        '''
        Функция записи данных в бд
        :param date: время shp-файла для бд
        :param df: geoDataFrame с точками и их параметрами
        '''
        dt = DateTm(date=date)
        try:
            self.session.add(dt)
            self.session.commit()
            for index, row in df.iterrows():
                fire = FireValue(date_id=dt.id, temperature=row['name'], longitude=round(row['geometry'].y, 2),
                                 latitude=round(row['geometry'].x, 2))
                self.session.add(fire)
                self.session.commit()
        except Exception as e:
            print(e)
        finally:
            self.session.close()
