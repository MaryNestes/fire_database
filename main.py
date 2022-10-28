import glob
import os

from cofig import PATH
from operation_class.shapefile import ReadShp
from operation_class.database import WriteToDB


def start():
    '''
    Главная функция для записи данных из shp-файлов в postgresql
    (для каждой итерации открывается своя сессия)
    '''
    # находит все shp файлы в директории
    for file_name in glob.glob(PATH + os.sep + "/*/*/*.shp"):
        # читаем файлы в geoDataFrame и вытягиваем время shp-файла
        reader = ReadShp(file_name)
        print(reader.date)
        # получаем ссессию
        db = WriteToDB()
        # если в бд нет необходимых таблиц для данных, то создаем
        db.crate_tables()
        # пишем данные из geoDataFrame в бд
        db.write_data(reader.date, reader())


if __name__ == '__main__':
    start()
