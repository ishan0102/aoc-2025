"""
Advent of Code 2025 - Day 8
https://adventofcode.com/2025/day/8

Part 2: Same as part 1, but stop at a fully connected circuit (MST)
"""
import math

def preprocess(boxes: list[tuple]) -> list[tuple]:
    distances = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            a, b = boxes[i], boxes[j]
            distances.append((a, b, math.dist(a, b)))
    
    distances.sort(key=lambda x: x[2])
    return distances


def add_to_sets(sets: list[set], a, b) -> None:
    a_i, b_i = -1, -1
    for i, s in enumerate(sets):
        if a in s:
            a_i = i
        if b in s:
            b_i = i
    
    if a_i == -1 and b_i == -1:
        sets.append({a, b})
    elif a_i == -1:
        sets[b_i].add(a)
    elif b_i == -1:
        sets[a_i].add(b)
    elif a_i != b_i:
        if a_i > b_i:
            a_set = sets.pop(a_i)
            sets[b_i] |= a_set
        else:
            b_set = sets.pop(b_i)
            sets[a_i] |= b_set


def main():
    with open("input.txt", "r") as file:
        boxes = [line.strip() for line in file.readlines()]
        boxes = [box.split(",") for box in boxes]
        boxes = [tuple([int(i) for i in box]) for box in boxes]

    distances = preprocess(boxes)
    sets = []
    total = -1
    for a, b, _ in distances:
        add_to_sets(sets, a, b)
        if len(sets) == 1 and len(sets[0]) == len(boxes):
            total = a[0] * b[0]
            break

    print(total)


if __name__ == "__main__":
    main()