import numpy as np
import matplotlib

def polyfit(dates,levels,p):

    d = matplotlib.dates.date2num(dates)
    
    if len(d) > 0:
        d0 = d[-1]

        d = [d[x] - d0 for x in range(len(d))]

        p_coeff = np.polyfit(d, levels, p)
    
        poly = np.poly1d(p_coeff)
    else: 
        poly = None
        d0 = None
    return poly,d0