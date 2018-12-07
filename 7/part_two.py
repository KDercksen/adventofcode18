#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from itertools import chain
from operator import itemgetter
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
    workers = [(None, 0)] * 5
    time_elapsed = 0
    while len(seq) < 26:
        for i, w in enumerate(workers):
            if w[1] == 0:
                if stack:
                    letter = stack.pop(0)
                    workers[i] = (letter, 60 + ord(letter) - 64)
                else:
                    workers[i] = (None, 0)
        shortest_task = min(filter(lambda x: x[0], workers), key=lambda x: x[1])
        seq += shortest_task[0]
        time_elapsed += shortest_task[1]
        workers = [(w[0], max(w[1] - shortest_task[1], 0)) for w in workers]
        for k, v in graph.items():
            if all(x in seq for x in v) and k not in chain(
                seq, stack, map(itemgetter(0), workers)
            ):
                stack.append(k)
        stack = sorted(stack)
    print(time_elapsed - 8)
