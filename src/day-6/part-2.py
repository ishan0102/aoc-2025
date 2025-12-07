"""
Advent of Code 2025 - Day 6
https://adventofcode.com/2025/day/6

Part 2: Transpose the whole input at the beginning!
"""
with open("input.txt", "r") as file:
    lines = file.readlines()

    rows = lines[:-1]
    cols = [list(col) for col in zip(*rows)]
    
    ops = lines[-1].split()

problems = []
problem = []
for c in cols:
    if all(x == " " or x == "\n" for x in c):
        problems.append(problem)
        problem = []
    
    num = 0
    power = 1
    for i in reversed(c):
        if i == " " or i == "\n":
            continue

        num += int(i) * power
        power *= 10

    if num > 0:
        problem.append(num)

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