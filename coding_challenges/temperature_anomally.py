# Python code below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

import numpy as np


def anomaly(allyears):
    # Your code goes here.
    refmean =  0.5 * (np.mean(allyears[65:76]['TMIN']) + np.mean(allyears[65:76]['TMAX']))
    anomaly = 0.5 * (np.mean(allyears['TMIN'], axis=1) + np.mean(allyears['TMAX'], axis=1) - refmean)

    return np.round(anomaly, 2)

