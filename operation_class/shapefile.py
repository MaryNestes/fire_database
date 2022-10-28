import os
import geopandas as gpd
from datetime import datetime


class ReadShp:
    def __init__(self, path: str):
        self.path = path
        self.date = self.pars_data(path)

    def __call__(self, *args, **kwargs) -> gpd.GeoDataFrame:
        return gpd.read_file(self.path)

    @classmethod
    def pars_data(cls, path: str) -> datetime:
        tmp = os.path.basename(path).split("_")
        tmp = tmp[4] + tmp[5]
        return datetime.strptime(tmp, "%Y%m%d%H%M")
