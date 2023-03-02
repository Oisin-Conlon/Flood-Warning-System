import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    
    low = [station.typical_range[0] for x in range(len(dates))]
    high = [station.typical_range[1] for x in range(len(dates))]
    
    
    # Plot
    plt.plot(dates, levels)
    plt.plot(dates, low)
    plt.plot(dates, high)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
    
def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    
    d = matplotlib.dates.date2num(dates)
    d = [d[x] - d0 for x in range(len(d))]
    
    plt.plot(d, poly(d))
    
   
    plot_water_levels(station, d, levels)
    
def plot_water_level_forcast(station,new_dates,new_levels):
    low = [station.typical_range[0] for x in range(len(new_dates))]
    high = [station.typical_range[1] for x in range(len(new_dates))]
    
    
    # Plot
    plt.plot(new_dates, new_levels)
    plt.plot(new_dates, low)
    plt.plot(new_dates, high)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()