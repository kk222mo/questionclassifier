import numpy as np

alpha = 0.00001

def eucl(a, b):
    delta = 1.2
    return np.linalg.norm(a - b) < delta


def cosDistAndCheckDelta(a, b, delta):
    return 1 - delta - alpha < cosDist(a, b) <= 1 + alpha


def cosDist(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))