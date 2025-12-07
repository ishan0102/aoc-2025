"""
Advent of Code 2025 - Day 6
https://adventofcode.com/2025/day/6

Part 1: Input parsing
"""
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    
    rows = lines[:-1]
    rows = [[int(n) for n in row.split() if n] for row in rows]
    ops = lines[-1].split()

problems = list(zip(*rows))
total = 0
for i in range(len(problems)):
    problem, op = problems[i], ops[i]
    
    res = problem[0]
    for j in range(1, len(problem)):
        if op == '+':
            res += problem[j]
        elif op == '*':
            res *= problem[j]
    total += res

print(total)