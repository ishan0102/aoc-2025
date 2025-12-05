"""
Advent of Code 2025 - Day 4
https://adventofcode.com/2025/day/4

Part 1: Nested loops
"""
with open("input.txt", "r") as file:
    grid = file.readlines()
    grid = [list(g.strip()) for g in grid]

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        square = grid[i][j]
        if square == '.':
            continue

        dirs = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
        dirs.remove((0, 0))
        indices = [(i + dx, j + dy) for dx, dy in dirs]
        indices = [(x, y) for x, y in indices if 0 <= x < len(grid) and 0 <= y < len(grid[0])]

        count = 0
        for x, y in indices:
            count += grid[x][y] == '@'
        
        if count < 4:
            total += 1

print(total)