# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.utils import sorted_by_key

from haversine import haversine, Unit
def station_by_distance(stations, p):
    '''Calculates the distance from a point p and sorts them in descending proximity'''
    output = []
    for n in stations:
        s = (n,haversine(n.coord,p))
        output.append(s)
    output = sorted_by_key(output,1)  
    return(output)

def stations_within_radius(stations, centre, r):
    '''Compiles a list of stations a distance r from a specified centre'''
    output = []
    radii = []
    for n in stations:
        if haversine(n.coord, centre) <= float(r):
            radii.append(n)
    return(radii)        
            

def rivers_with_station(stations):
    rivers = []
    for n in stations:
        if n.river not in rivers:
            rivers.append(n.river)
    return(rivers)

def stations_by_river(stations):
    whichstations = {}
    rivers = rivers_with_station(stations)
    for n in rivers:
        
        whichstations[n] = []

    for station in stations:
        whichstations[station.river].append(station.name)
    return(whichstations)

def rivers_by_station_number(stations, N):
    dictionary = stations_by_river(stations)

    list = []

    for river in dictionary:
        list += [[len(dictionary[river]),river]]

    list.sort(reverse = True)

    for a in range(len(list)):
            temp = list[a][0]
            list[a][0] = list[a][1]
            list[a][1] = temp
    
    list_of_tuples = [tuple(x) for x in list]
    
    print (list_of_tuples[:N])