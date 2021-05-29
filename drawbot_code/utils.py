import numpy as np
import shapely


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


def dist(a, b):
    return np.sqrt(sqdist(a, b))


def sqdist(a, b):
    return (b.x - a.x)**2 + (b.y - a.y)**2


def mls_to_lines(mls):
    return [[Point(c[0], c[1]) for c in l.coords] for l in mls]


def mls_normalize(mls):
    min_x, min_y, max_x, max_y = mls.bounds
    length = max(max_x - min_x, max_y - min_y)
    mls = shapely.affinity.translate(mls, xoff=-min_x, yoff=-min_y)
    mls = shapely.affinity.scale(mls, xfact=(1 / length), yfact=(1 / length),
                                 origin=(0,0))
    return mls