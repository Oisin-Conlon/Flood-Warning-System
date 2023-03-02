from floodsystem.flood import warning
from floodsystem.flood import forcast
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels

stations = build_station_list()
list = []
update_water_levels(stations)
for station in stations:
    if MonitoringStation.typical_range_consistent(station) == True:
        if MonitoringStation.relative_water_level(station) != None:
            if MonitoringStation.relative_water_level(station) > 0.6:
                if warning(station) == "severe" or warning(station) == "high":
                    list.append((station.name,warning(station)))

print(list)