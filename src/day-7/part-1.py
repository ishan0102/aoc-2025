"""
Advent of Code 2025 - Day 7
https://adventofcode.com/2025/day/7

Part 1: Keep track of tachyon indices in a set
"""
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    s_index = lines[0].find("S")
    lines = lines[2::2]

splitters = set()
splitters.add(s_index)

split_count = 0
for line in lines:
    for i, space in enumerate(line):
        if space == '.':
            continue
        
        if i in splitters:
            split_count += 1
            splitters.remove(i)
            splitters.add(i - 1)
            splitters.add(i + 1)
    
print(split_count)