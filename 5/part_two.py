#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from string import ascii_lowercase


def react(text):
    i = 0
    while i < len(text) - 1:
        if abs(ord(text[i]) - ord(text[i + 1])) == 32:
            del text[i : i + 2]
            i -= 1
        else:
            i += 1
        i = max(i, 0)
    return len(text)


if __name__ == "__main__":
    with open("input.txt") as f:
        text = list(f.read().strip())

    print(
        min(
            [
                react([unit for unit in text if unit.lower() != letter])
                for letter in ascii_lowercase
            ]
        )
    )
