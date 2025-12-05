"""
Advent of Code 2025 - Day 2
https://adventofcode.com/2025/day/2

Part 1: Brute force
"""
with open("input.txt", "r") as file:
    ranges = file.readline()
    ranges = ranges.split(",")
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]

invalid_sum = 0
for n, m in ranges:
    for i in range(n, m + 1):
        str_num = str(i)
        if len(str_num) % 2 != 0:
            continue

        midpoint = len(str_num) // 2
        if str_num[:midpoint] != str_num[midpoint:]:
            continue
        
        invalid_sum += i

print(invalid_sum)