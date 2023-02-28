from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.stationdata import MonitoringStation

stations = build_station_list()
update_water_levels(stations)



def stations_level_over_threshold(stations, p):
    names = []
    for station in stations:

        if station.typical_range_consistent():
            if station.relative_water_level() != None and station.relative_water_level() >= p:

                names.append((station.name, station.relative_water_level()))
                #print((station.name, station.relative_water_level()))
    return(names)

print(stations_level_over_threshold(stations, 0.8))