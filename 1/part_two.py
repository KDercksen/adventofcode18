#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from itertools import cycle


if __name__ == "__main__":
    with open("input.txt") as f:
        deviations = list(map(int, f.read().strip().split("\n")))

    current_freq = 0
    freq_counts = defaultdict(int)
    freq_counts[current_freq] += 1

    for dev in cycle(deviations):
        current_freq += dev
        freq_counts[current_freq] += 1
        if freq_counts[current_freq] == 2:
            break
    print(current_freq)
