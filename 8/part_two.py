#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def compute(data):
    if len(data) == 0:
        return [], 0
    children, entries = data[:2]
    rest = data[2:]
    if children == 0:
        return rest[entries:], sum(rest[:entries])
    child_vals = []
    for _ in range(children):
        rest, result = compute(rest)
        child_vals.append(result)
    val = sum(child_vals[i - 1] for i in rest[:entries] if i <= len(child_vals))
    rest = rest[entries:]
    return rest, val


if __name__ == "__main__":
    with open("input.txt") as f:
        data = list(map(int, f.read().split()))
    print(compute(data))
