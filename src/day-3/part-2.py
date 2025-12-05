"""
Advent of Code 2025 - Day 3
https://adventofcode.com/2025/day/3

Part 2: Remove the most useless digit, preserve top-12 in order
"""
with open("input.txt", "r") as file:
    banks = file.readlines()
    banks = [b.strip() for b in banks]

total_joltage = 0
for bank in banks:
    while len(bank) > 12:
        for i in range(len(bank) - 1):
            if bank[i] < bank[i+1]:
                bank = bank[:i] + bank[i+1:]
                break
        else:
            bank = bank[:-1]

    joltage = int(bank)
    total_joltage += joltage

print(total_joltage)