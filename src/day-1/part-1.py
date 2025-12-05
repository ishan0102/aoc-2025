"""
Advent of Code 2025 - Day 1
https://adventofcode.com/2025/day/1

Part 1: Clean modulo solution
"""
with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    lines = [(line[0], line[1:]) for line in lines]

dial = 50
password = 0
for line in lines:
    turn = line[0]
    distance = int(line[1])
    
    if turn == "R":
        dial += distance
    else:
        dial -= distance
    
    dial %= 100
    if dial == 0:
        password += 1

print(password)