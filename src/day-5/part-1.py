"""
Advent of Code 2025 - Day 5
https://adventofcode.com/2025/day/5

Part 1: Brute force
"""
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    blank_idx = lines.index("")

    ranges = lines[:blank_idx]
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]

    ingredients = lines[blank_idx + 1:]
    ingredients = [int(i) for i in ingredients]

fresh_count = 0
for i in ingredients:
    for r in ranges:
        if r[0] <= i <= r[1]:
            fresh_count += 1
            break

print(fresh_count)