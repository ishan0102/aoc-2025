"""
Advent of Code 2025 - Day 2
https://adventofcode.com/2025/day/2

Part 2: Brute force
"""
with open("input.txt", "r") as file:
    ranges = file.readline()
    ranges = ranges.split(",")
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]

invalid_sum = 0
for n, m in ranges:
    # Walk each number in the range
    for i in range(n, m + 1):
        str_num = str(i)
        midpoint = len(str_num) // 2
        is_invalid = False

        # Walk each substring length
        for j in range(1, midpoint + 1):
            prev = str_num[:j]
            all_match = True
            
            # Walk each substring
            for k in range(0, len(str_num), j):
                curr = str_num[k:k+j]
                if prev != curr:
                    all_match = False
                    break

            if all_match:
                is_invalid = True

        if is_invalid:
            invalid_sum += i

print(invalid_sum)