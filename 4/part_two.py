#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from datetime import datetime
import numpy as np
import re


def get_info(s):
    guard_line = re.match(r"\[(.*?)\] Guard #(\d+).*", s)
    if guard_line:
        date = datetime.strptime(guard_line.group(1), "%Y-%m-%d %H:%M")
        guard_id = int(guard_line.group(2))
        return {"type": "guard", "date": date, "id": guard_id}
    sleep_line = re.match(r"\[(.*?)\] (\w+).*", s)
    date = datetime.strptime(sleep_line.group(1), "%Y-%m-%d %H:%M")
    wakes_up = sleep_line.group(2) == "wakes"
    return {"type": "sleep", "date": date, "wakes_up": wakes_up}


def make_sleep_array(sleep_entries):
    sleep_arr = np.zeros(60)
    for cur, nxt in zip(sleep_entries, sleep_entries[1:]):
        cur_min = cur["date"].minute
        nxt_min = nxt["date"].minute
        sleep_arr[cur_min:nxt_min] = nxt["wakes_up"]
    return sleep_arr


if __name__ == "__main__":
    entries = []
    with open("input.txt") as f:
        for line in f:
            entries.append(get_info(line.strip()))
    entries = list(sorted(entries, key=lambda x: x["date"]))

    # Make guard indices
    guard_idx = [x for x in range(len(entries)) if entries[x]["type"] == "guard"]

    # Collect total amount of sleeping minutes per guard
    sleep_sums = defaultdict(lambda: np.zeros(60))
    for cur, nxt in zip(guard_idx, guard_idx[1:]):
        sleep_entries = entries[cur + 1 : nxt]
        sleep_arr = make_sleep_array(sleep_entries)
        sleep_sums[entries[cur]["id"]] += sleep_arr

    # Find guard with highest frequency of same minute asleep
    sleepy_guard, sleep_arr = max(sleep_sums.items(), key=lambda x: np.max(x[1]))
    best_minute = np.argmax(sleep_arr)
    print(f"{sleepy_guard * best_minute}")
