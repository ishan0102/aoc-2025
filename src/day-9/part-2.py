"""
Advent of Code 2025 - Day 9
https://adventofcode.com/2025/day/9

Part 2: Pick two vertices and flood fill
"""
def get_size(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    size = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
    return size
    
def construct_grid(points):
    max_x = sorted(points, key=lambda x: x[0])[-1][0] + 1
    max_y = sorted(points, key=lambda x: x[1])[-1][1] + 1
    grid = [["." for _ in range(max_y)] for _ in range(max_x)]

    for x, y in points:
        grid[x][y] = "#"

    rotated = points[1:] + [points[0]]
    for p1, p2 in zip(points, rotated):
        pass

    return grid

def floodfill(grid, p1, p2):
    pass

def main():
    with open("input.txt", "r") as file:
        lines = [line.strip().split(",") for line in file.readlines()]
        points = [(int(line[0]) - 1, int(line[1]) - 1) for line in lines] # Remap to indices

    grid = construct_grid(points)
    for g in grid:
        print(g)

if __name__ == "__main__":
    main()