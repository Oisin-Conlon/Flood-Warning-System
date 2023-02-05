# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
def station_by_distance(stations, p):
    output = []
    for n in stations:
        s = (n,haversine(n.coord,p))
        output.append(s)
    output = sorted_by_key(output,1)  
    return(output)

