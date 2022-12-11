#!/usr/env/bin python
import time
import string


priorities = dict(zip(string.ascii_letters, range(1, 53)))

# THERE SHOULD BE A SINGLE STRING COMPARISON FUNCTION, USED RECURSIVELY


def items_per_rucksack(line):
    midindex = len(line) // 2
    first_half = line[:midindex]
    second_half = line[midindex:]

    for letter in first_half:
        if second_half.find(letter) != -1:
            return priorities[letter]


def items_per_group(lines):
    one, two, three = lines
    intersection = []
    for letter in one:
        if two.find(letter) != -1:
            intersection.append(letter)
    for letter in intersection:
        if three.find(letter) != -1:
            return priorities[letter]


if __name__ == "__main__":
    start = time.perf_counter()

    total_by_rucksack = 0
    total_by_group = 0
    groups = [[]]

    with open("input.txt") as f:
        for line in f.readlines():
            # by rucksack
            total_by_rucksack += items_per_rucksack(line[:-1])

            # create the groups
            if len(groups[-1]) < 3:
                groups[-1].append(line[:-1])
            else:
                groups.append([line[:-1]])

        # count total group priorities
        for group in groups:
            total_by_group += items_per_group(group)

    print(f"Total by rucksack: {total_by_rucksack}")
    print(f"Total by group: {total_by_group}")

    stop = time.perf_counter()
    print(f"elapsed: {stop-start}")
