"""
Advent of Code 2025 - Day 3
https://adventofcode.com/2025/day/3

Part 1: Two-pointer
"""
with open("input.txt", "r") as file:
    banks = file.readlines()
    banks = [b.strip() for b in banks]

total_joltage = 0
for bank in banks:
    n, m = int(bank[0]), 0
    n_idx = 0
    for i in range(1, len(bank)):
        curr = int(bank[i])

        if curr > n and i < len(bank) - 1:
            n = curr
            n_idx = i
            m = 0

        if curr > m and i > n_idx:
            m = curr

    joltage = n * 10 + m
    total_joltage += joltage

print(total_joltage)