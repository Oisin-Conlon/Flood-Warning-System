from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1D"""
    stations = build_station_list()
    print(len(rivers_with_station(stations)))
    all = rivers_with_station(stations)
    alpha = sorted(all)
    first10 = alpha[:10]

    print(first10)
    rivers = stations_by_river(stations)

    def findstations(river):
        riverstations = rivers[river]
        return(riverstations)
    
    print(sorted(findstations('River Aire')), sorted(findstations('River Cam')), sorted(findstations('River Thames')))


   






if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()