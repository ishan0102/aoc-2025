"""
Advent of Code 2025 - Day 9
https://adventofcode.com/2025/day/9

Part 1: Check all rectangles (brute force convex hull)
"""
def get_size(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    size = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
    return size

def main():
    with open("input.txt", "r") as file:
        lines = [line.strip().split(",") for line in file.readlines()]
        points = [(int(line[0]), int(line[1])) for line in lines]

    max_size = 0
    for p1 in points:
        for p2 in points:
            max_size = max(max_size, get_size(p1, p2))

    print(max_size)

if __name__ == "__main__":
    main()