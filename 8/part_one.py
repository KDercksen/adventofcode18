#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def compute(data):
    if len(data) == 0:
        return [], 0
    children, entries = data[:2]
    rest = data[2:]
    entries_sum = 0
    for _ in range(children):
        rest, result = compute(rest)
        entries_sum += result
    entries_sum += sum(rest[:entries])
    rest = rest[entries:]
    return rest, entries_sum


if __name__ == "__main__":
    with open("input.txt") as f:
        data = list(map(int, f.read().split()))
    print(compute(data))
