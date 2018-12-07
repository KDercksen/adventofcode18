#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from itertools import chain
import re


if __name__ == "__main__":
    graph = defaultdict(list)
    with open("input.txt") as f:
        for line in f:
            first, after = re.match(r".*?\s(\w)\s.*?\s(\w)\s.*", line).groups()
            graph[after].append(first)

    stack = [v[0] for v in graph.values() if len(v) == 1]
    for v in graph.values():
        for x in v:
            if x not in chain(graph.keys(), stack):
                stack.append(x)
    stack = sorted(stack)
    seq = ""
    for i in range(26):
        seq += stack.pop(0)
        for k, v in graph.items():
            if all(x in seq for x in v) and k not in chain(seq, stack):
                stack.append(k)
        stack = sorted(stack)
    print(seq)
