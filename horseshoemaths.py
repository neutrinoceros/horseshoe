import numpy as np


def get_centered(vector, center) :
    return vector - center

def get_rotated(vector, angle) :
    a = -angle
    x, y = vector
    xr = x * np.cos(a) - y * np.sin(a)
    yr = x * np.sin(a) + y * np.cos(a)
    return np.array([xr,yr])
