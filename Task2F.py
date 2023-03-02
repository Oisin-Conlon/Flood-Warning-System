from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level

def run():
    
    stations = build_station_list()
    highest = stations_highest_rel_level(stations, 5)

    dates, levels = [[] for a in range(len(highest))],[[] for b in range(len(highest))]

    for s in range(len(highest)):
        dates[s], levels[s] = fetch_measure_levels(highest[s].measure_id, timedelta(2))
        plot_water_level_with_fit(highest[s], dates[s], levels[s], 4)
        
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()