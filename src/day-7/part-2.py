"""
Advent of Code 2025 - Day 7
https://adventofcode.com/2025/day/7

Part 2: Part 1 with recursion
"""
from functools import lru_cache

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    s_index = lines[0].find("S")
    lines = lines[2::2]

@lru_cache(None)
def traverse(row_i, beams):
    beams = set(beams)
    if row_i == len(lines):
        return len(beams)

    row = lines[row_i]
    new_beams = set()
    splits = 0

    for i in beams:
        if 0 <= i < len(row) and row[i] == '^':
            splits += traverse(row_i + 1, frozenset({i - 1}))
            splits += traverse(row_i + 1, frozenset({i + 1}))
        else:
            if 0 <= i < len(row):
                new_beams.add(i)

    total = splits
    if new_beams:
        total += traverse(row_i + 1, frozenset(new_beams))

    return total

count = traverse(0, frozenset({s_index}))
print(count)