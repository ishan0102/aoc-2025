"""
Advent of Code 2025 - Day 12
https://adventofcode.com/2025/day/12

Part 1: Just check if the output area would fit enough presents with size 9 (cheap trick)
"""
PRESENT_SIZE = 9

with open("input.txt", "r") as file:
    content = file.read()
    content = content.split("\n\n")[-1]

lines = content.splitlines()
lines = [line.split(":") for line in lines]

areas, presents = zip(*lines)
areas = [int(a.split("x")[0]) * int(a.split("x")[1]) for a in areas]
presents = [sum([int(i) for i in p.split()]) for p in presents]

total = 0
for area, present in zip(areas, presents):
    if area >= present * PRESENT_SIZE:
        total += 1

print(total)