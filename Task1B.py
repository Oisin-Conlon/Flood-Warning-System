from floodsystem.stationdata import build_station_list
from floodsystem.geo import station_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    all = station_by_distance(stations,(52.2053, 0.1218))
    answer = []
    for station, distance in all:
        individual = (station.name, station.town, distance)
        answer.append(individual)
    print(answer[:10],answer[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
