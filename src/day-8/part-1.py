"""
Advent of Code 2025 - Day 8
https://adventofcode.com/2025/day/8

Part 1: Maintain adjacency lists with euclidean distances
"""
import copy
import math

from tqdm import tqdm

def connect_min(boxes, circuits):
    min_distance = float('inf')
    min_keys = [-1, -1]
    for i in range(len(boxes)):
        for j in range(i, len(boxes)):
            if i == j:
                continue

            if i in circuits.get(j, []):
                continue

            distance = math.dist(boxes[i], boxes[j])
            if distance < min_distance:
                min_distance = distance
                min_keys[0] = i
                min_keys[1] = j

    i, j = min_keys
    if i == -1 or j == -1:
        return

    circuits[i].append(j)
    circuits[j].append(i)

def count_circuits(circuits) -> int:
    circuits = copy.deepcopy(circuits)
    count = 0
    seen = set()
    for key, value in circuits.items():
        if key in seen or len(value) == 0:
            continue

        count += 1
        for v in value:
            seen.add(v)
    
    return count

def get_result(circuits):
    sorted_circuits = dict(sorted(circuits.items(), key=lambda x: len(x[1]), reverse=True))
    seen = set()
    top_3 = []
    for key, value in sorted_circuits.items():
        if key in seen:
            continue

        top_3.append(len(value) + 1)
        for v in value:
            seen.add(v)

    return top_3[0] * top_3[1] * top_3[2]

def main():
    with open("input.txt", "r") as file:
        boxes = [line.strip() for line in file.readlines()]
        boxes = [box.split(",") for box in boxes]
        boxes = [tuple([int(i) for i in box]) for box in boxes]

    circuits = {i: [] for i in range(len(boxes))}
    for _ in tqdm(range(1001)):
        connect_min(boxes, circuits)

    print(get_result(circuits))

if __name__ == "__main__":
    main()