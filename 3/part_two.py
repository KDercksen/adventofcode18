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
        f.seek(0)
        for line in f:
            match = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line.strip())
            claim, y, x, w, h = map(int, match.groups())
            if np.all(grid[x : x + h, y : y + w] == 1):
                print(claim)
