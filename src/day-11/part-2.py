"""
Advent of Code 2025 - Day 11
https://adventofcode.com/2025/day/11

Part 2: 
"""
from functools import lru_cache

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

graph = {}
for line in lines:
    a, b = line.split(":")
    graph[a.strip()] = b.strip().split()

@lru_cache(None)
def dfs(node, seen_dac, seen_fft):
    if node == "dac":
        seen_dac = True
    if node == "fft":
        seen_fft = True

    if node == "out":
        return 1 if (seen_dac and seen_fft) else 0

    return sum(
        dfs(neighbor, seen_dac, seen_fft)
        for neighbor in graph.get(node, [])
    )

print(dfs("svr", False, False))