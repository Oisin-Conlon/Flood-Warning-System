from floodsystem.stationdata import build_station_list
from floodsystem.geo import station_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

def test_rivers_by_station_number():
    stations = build_station_list()
    assert type(rivers_by_station_number(stations,9)) == list
