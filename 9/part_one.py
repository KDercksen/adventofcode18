#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


class Node:
    def __init__(self, marble):
        self.marble = marble
        self.next = None
        self.last = None


if __name__ == "__main__":
    with open("input.txt") as f:
        players, points = map(int, re.match(r"(\d+).*?(\d+).*", f.read()).groups())

    scores = [0] * players
    first = Node(0)
    second = Node(1)
    first.next = second
    first.last = second
    second.next = first
    second.last = first
    cur_node = second

    for marble in range(2, points + 1):
        if marble % 23 == 0:
            for _ in range(7):
                cur_node = cur_node.last
            scores[marble % players] += marble + cur_node.marble
            cur_node.last.next = cur_node.next
            cur_node = cur_node.next
        else:
            new_node = Node(marble)
            new_node.last = cur_node.next
            new_node.next = cur_node.next.next
            cur_node.next.next.last = new_node
            cur_node.next.next = new_node
            cur_node = new_node
    print(max(scores))
