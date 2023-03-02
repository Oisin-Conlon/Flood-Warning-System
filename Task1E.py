from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import rivers_by_station_number

stations = build_station_list()

rivers_by_station_number(stations,15)
