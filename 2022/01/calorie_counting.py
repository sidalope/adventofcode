#!/usr/bin.env python

import time


start = time.perf_counter()

elf_inv = [0]

with open("input.txt") as f:
    for line in f.readlines():
        if line != "\n":
            elf_inv[-1] += int(line)
        else:
            elf_inv.append(0)

elf_inv.sort(reverse=True)
print(f"largest: {elf_inv[0]}")

# -- Part 2 --
print(f"largest 3: {elf_inv[0]+elf_inv[1]+elf_inv[2]}")


stop = time.perf_counter()
print(f"elapsed: {stop-start}")


if __name__ == "__main__":
    pass
