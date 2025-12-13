"""
Advent of Code 2025 - Day 11
https://adventofcode.com/2025/day/11

Part 1: DFS on a graph
"""
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

graph = {}
for line in lines:
    a, b = line.split(":")
    graph[a.strip()] = b.strip().split()

def dfs(node):
    if node == "out":
        return 1

    total = 0
    for neighbor in graph.get(node, []):
        total += dfs(neighbor)
    return total

print(dfs("you"))