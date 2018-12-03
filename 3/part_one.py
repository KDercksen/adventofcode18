#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import re

if __name__ == "__main__":
    grid = np.zeros((1000, 1000))
    with open("input.txt") as f:
        for line in f:
            match = re.match(r".*?@ (\d+),(\d+): (\d+)x(\d+)", line.strip())
            y, x, w, h = map(int, match.groups())
            grid[x : x + h, y : y + w] += 1
    print(np.sum(grid > 1))
