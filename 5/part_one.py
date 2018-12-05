#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open("input.txt") as f:
        text = list(f.read().strip())
    i = 0
    while i < len(text) - 1:
        if abs(ord(text[i]) - ord(text[i + 1])) == 32:
            del text[i : i + 2]
            i -= 1
        else:
            i += 1
        i = max(i, 0)
    print(len(text))
