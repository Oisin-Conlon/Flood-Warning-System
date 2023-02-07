from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""
    stations = build_station_list()
    raw = []
    raw = stations_within_radius(stations, (52.2053, 0.1218), 10) 
    rawnames= []
    for station in raw:
       rawnames.append(station.name)
    ordered = sorted(rawnames)
    print(ordered)






if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()