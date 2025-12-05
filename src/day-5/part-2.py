"""
Advent of Code 2025 - Day 5
https://adventofcode.com/2025/day/5

Part 2: Merge intervals
"""
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    blank_idx = lines.index("")

    ranges = lines[:blank_idx]
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]

ranges.sort(key=lambda x: x[0])
i = 0
while i < len(ranges) - 1:
    r1, r2 = ranges[i], ranges[i + 1]
    if r1[1] < r2[0]:
        i += 1
        continue

    ranges[i] = (r1[0], max(r1[1], r2[1]))
    ranges.pop(i + 1)

total = 0
for r in ranges:
    total += r[1] - r[0] + 1

print(total)