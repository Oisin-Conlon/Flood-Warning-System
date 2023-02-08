from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()
inconsistent_stations = inconsistent_typical_range_stations(stations)

##Creates a new list of tuples that has the station and then the name so it can be sorted 

list_station_names = []
for i in range(len(inconsistent_stations)):
    station_name = (inconsistent_stations[i], inconsistent_stations[i].name)
    list_station_names.append(station_name)


##Sorts the list by name
station_name = sorted_by_key(list_station_names, 1)
list_of_inconsistent_stations = []

##Takes the names and creates a list of just the names


for i in range(len(station_name)):
    list_of_inconsistent_stations.append(station_name[i][0].name)

print(list_of_inconsistent_stations)

