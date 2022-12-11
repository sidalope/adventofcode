#!/usr/env/bin python

import time
import string


priorities = dict(zip(string.ascii_letters, range(1, 53)))

if __name__ == "__main__":
    start = time.perf_counter()

    total = 0

    with open("input.txt") as f:
        for line in f.readlines():
            first_half = line[: len(line) // 2]
            second_half = line[len(line) // 2 :]

            for letter in first_half:
                if second_half.find(letter) != -1:
                    total += priorities[letter]
                    break

    print(total)

    stop = time.perf_counter()
    print(f"elapsed: {stop-start}")
