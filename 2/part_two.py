#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations
from operator import itemgetter


def levenshtein(x, y):
    distances = range(len(x) + 1)
    for ixy, yc in enumerate(y):
        new_distances = [ixy + 1]
        for ixx, xc in enumerate(x):
            if xc == yc:
                new_distances.append(distances[ixx])
            else:
                new_distances.append(
                    1 + min((distances[ixx], distances[ixx + 1], new_distances[-1]))
                )
        distances = new_distances
    return distances[-1]


if __name__ == "__main__":
    with open("input.txt") as f:
        box_ids = f.read().strip().split("\n")
        for x, y in combinations(box_ids, 2):
            if levenshtein(x, y) == 1:
                common = map(itemgetter(0), filter(lambda x: x[0] == x[1], zip(x, y)))
                print("".join(common))
