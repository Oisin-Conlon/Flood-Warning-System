from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import update_water_levels
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_forcast
import matplotlib

def stations_level_over_threshold(stations, tol):
    ##Create blank array to add stations to
    stations_tol = []
    ##Get the latest water levels
    update_water_levels(stations)



    for station in stations:
        ##Define a variable for the water level
        water_level = MonitoringStation.relative_water_level(station)
        ##If water level is a number and higher than tol, add to array
        if type(water_level) == float:
            if water_level > tol:
                stations_tol.append((station, water_level))
    ##Sort and return array
    stations_tol = sorted_by_key(stations_tol, 1, True)
    return stations_tol

def stations_highest_rel_level(stations, N, test = False):

    ##Get latest water levels
    if test == False:
        update_water_levels(stations)

    ##Blank array to make sorting by level easier
    station_levels = []

    ##Add all stations to array as (station, relative level) if relative level is a float
    for station in stations:
        water_level = MonitoringStation.relative_water_level(station)
        if type(water_level) == float:
            station_levels.append((station, water_level))
    ##Sorts by relative level
    station_levels = sorted_by_key(station_levels, 1, True)

    sorted_stations = []
    for station_level in station_levels:
        sorted_stations.append(station_level[0])
    return sorted_stations[:N]

def forcast(station,plot = False):
    if MonitoringStation.typical_range_consistent(station) == True:
        dt = 10
        f = 3
        p = 4
        
        dates,levels = fetch_measure_levels(station.measure_id, timedelta(dt))
        new_levels = []
        
        poly, d0 = polyfit(dates, levels, p)
        if poly != None:
                
            d = matplotlib.dates.date2num(dates)
            d = [d[x] - d0 for x in range(len(d))]
            
            new_d = []
            
            for a in range(dt + f):
                new_levels.append(poly(a))
                new_d.append(a)
            
            if plot == True:
                plot_water_level_forcast(station,new_d,new_levels)
            
            return new_levels[-1]
        else:
            return None
def warning(station, now = False):
    p = 4
    dates, levels = fetch_measure_levels(station.measure_id, timedelta(10), now)
    if MonitoringStation.typical_range_consistent(station) == True:  
        high = station.typical_range[1]
        low = station.typical_range[0]
        typ_avg = abs((high+low)/2)
        
        score = 0

        if forcast(station)!= None:
            if forcast(station) > high: #if the forcasted water level is greater than the typical value the station is more likely to flood
                score += 1
            
        avg = 0 
        
        for a in range(len(levels)):
            avg += levels[a]
            
        if len(levels) > 0:
            avg = avg/len(levels)
        
        if avg > high: #if the average water level in the last 10 days is greater than the typical value the station is more likely to flood
            score += 1
            
        m = 0
        
        poly, d0 = polyfit(dates, levels, p)
        if poly != None:
            d = matplotlib.dates.date2num(dates)
            d = [d[x] - d0 for x in range(len(d))]
            
            d2 = d[0] 
            d1 = d[100]
            l1 = poly(d1)
            l2 = poly(d2)
            
            m = (l2 - l1)/(d2-d1) 
            m = m/typ_avg #scaled m
            
            
            if m >= 0.01:
                score += 1 #if the water level is rising then it is more likely to flood
            elif m <= -0.01:
                score -= 1 #if the water level is falling then it is less likely to flood
                
                #0.01 as a treshhold to determine weather it is rising/falling significantly
                
            if score == 3:
                return "severe"
            elif score == 2:
                return "high"
            elif score == 1:
                return "moderate"
            else:
                return "low"
            