#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict


def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def calc_counts(bound):
    region = 0
    counts = defaultdict(int)
    grid = [
        ["." for x in range(min_x - bound, max_x + bound)]
        for y in range(min_y - bound, max_y + bound)
    ]
    for row in range(min_y - bound, max_y + bound):
        for col in range(min_x - bound, max_x + bound):
            distances = {}
            for i in range(len(coordinates)):
                distances[i] = manhattan([col, row], coordinates[i])
            if sum(distances.values()) < 1e4:
                region += 1
            closest_val = min(distances.values())
            closest_coord = [k for k, v in distances.items() if v == closest_val]
            if len(closest_coord) == 1:
                grid[(row - min_y) - bound][(col - min_x) - bound] = closest_coord[0]
                counts[closest_coord[0]] += 1
    return counts, region


if __name__ == "__main__":
    coordinates = []
    with open("input.txt") as f:
        for line in f:
            x, y = map(int, line.split(", "))
            coordinates.append((x, y))

    coordinates = sorted(coordinates, key=lambda k: (k[0], k[1]))
    min_x = coordinates[0][0]
    min_y = sorted(coordinates, key=lambda k: k[1])[0][1]
    max_x = coordinates[-1][0]
    max_y = sorted(coordinates, key=lambda k: k[1])[-1][1]

    counts1, _ = calc_counts(10)
    counts2, region = calc_counts(20)
    finite_counts = []
    for k, v in counts1.items():
        if counts2[k] == v:
            finite_counts.append(v)

    print(f"Largest Finite Area(pt1): {max(finite_counts)}, Region(pt2): {region}")
