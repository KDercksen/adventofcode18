#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from functools import reduce
from operator import mul


if __name__ == "__main__":
    global_counter = Counter()
    track = [2, 3]
    with open("input.txt") as f:
        for line in f:
            line_counter = Counter(line.strip())
            for t in track:
                if any(x == t for x in line_counter.values()):
                    global_counter[t] += 1
    print(reduce(mul, global_counter.values()))
