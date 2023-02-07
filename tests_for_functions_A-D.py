from floodsystem.stationdata import build_station_list
from floodsystem.geo import station_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

#all tests for A-D

def test_station_by_distance():
    stations = build_station_list()

    ntest = station_by_distance(stations)
    assert ntest[0][1] < ntest[1][1]

def test_stations_within_radius():
    stations = build_station_list()
    assert len(stations_within_radius(stations, (0.0,0.0), 0.0) )== 0 
    assert len(stations_within_radius(stations, (0.0,0.0), 100000000000000000000000000000000000000000))== len(stations)

def test_rivers_with_station():
    stations = build_station_list()
    assert len(rivers_with_station(stations)) < len(stations(stations))

def test_stations_by_river():
    stations = build_station_list()
    mtest = stations_by_river(stations)
    assert mtest.keys()[0] in rivers_with_station(stations)







