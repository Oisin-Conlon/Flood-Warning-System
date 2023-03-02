from floodsystem.stationdata import build_station_list
from floodsystem.geo import station_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from Task2B import stations_level_over_threshold

# all tests for A-D

def test_station_by_distance():
    stations = build_station_list()

    ntest = station_by_distance(stations,(0.0,0.0))
    assert ntest[0][1] < ntest[1][1]

def test_stations_within_radius():
    stations = build_station_list()
    assert len(stations_within_radius(stations, (0.0,0.0), 0.0) )== 0 
    assert len(stations_within_radius(stations, (0.0,0.0), 100000000000000000000000000000000000000000))== len(stations)

def test_rivers_with_station():
    stations = build_station_list()
    assert len(rivers_with_station(stations)) < len((stations))

def test_stations_by_river():
    stations = build_station_list()
    mtest = stations_by_river(stations)
    ptest = list(mtest.keys())
    assert ptest[0] in rivers_with_station(stations)

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    assert len(stations_highest_rel_level(stations,10)) == 10
    
def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    teststations = stations_level_over_threshold(stations, 0.8)
    assert teststations[0][1] < 0.8








