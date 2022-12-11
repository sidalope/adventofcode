#!/usr/env/bin python

"""
    1: rock
    2: paper
    3: scissors

    0: loss
    3: draw
    6: win

    X: rock
    Y: paper
    Z: scissors

    A: rock
    B: paper
    C: scissors
    """

import time


def decode(a, b):
    switch = {
        "A": "rock",
        "X": "rock",
        "B": "paper",
        "Y": "paper",
        "C": "scissors",
        "Z": "scissors",
    }
    return switch[a], switch[b]


#  -- Part 2 --
def decode_ultra(a, b):
    switch = {
        "A": "rock",
        "X": "rock",
        "B": "paper",
        "Y": "paper",
        "C": "scissors",
        "Z": "scissors",
    }
    return switch[a], switch[b]


def increment_score(rps):
    global score
    a, b = rps
    if a == b:
        score += 3

    if b == "rock":
        if a == "scissors":
            score += 7
        else:
            score += 1

    elif b == "paper":
        if a == "rock":
            score += 8
        else:
            score += 2

    else:
        if a == "paper":
            score += 9
        else:
            score += 3


if __name__ == "__main__":
    start = time.perf_counter()
    score = 0

    with open("input.txt") as f:
        for line in f.readlines():
            increment_score(decode(line[0], line[-2]))
    print(score)

    stop = time.perf_counter()
    print(f"elapsed: {stop-start}")
