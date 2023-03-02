from .stationdata import build_station_list, update_water_levels

from .station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    x = []
    for n in stations:
        if update_water_levels(stations) > tol:
            d = (n, n.update_water_levels())
            x.append(d)

def stations_highest_rel_level(stations, N):
    names = []
    numbers = []
    for station in stations:
        if station.relative_water_level() != None:
            numbers.append((station.relative_water_level()))

    numbers.sort()
    
    topN = []

    topN = numbers[-N:]


    

    for station in stations:
        if station.relative_water_level() in topN:
            names.append((station.name, station.relative_water_level()))
    return names        


