import numpy as np

from utils import *


def optimize_ordering(lines):
    # Start with first line
    ordering = [0]
    reverses = set()
    remaining = set(range(1, len(lines)))
    prev = lines[0][-1]
    
    while len(remaining) > 0:
        # Find closest point
        remaining_list = list(remaining)
        dists = [sqdist(prev, lines[j][k]) 
                 for j in remaining_list for k in [0, -1]]
        closest = np.argmin(dists)
        closest_line = remaining_list[closest // 2]
        closest_reverse = closest % 2 == 1

        remaining.remove(closest_line)
        ordering.append(closest_line)
        if closest_reverse:
            reverses.add(closest_line)

        prev = lines[closest_line][0 if closest_reverse else -1]

    lines = [lines[i][::-1] if i in reverses else lines[i] for i in ordering]
    return lines
