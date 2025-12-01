with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]
    lines = [(line[0], int(line[1:])) for line in lines]

dial = 50
password = 0

for turn, distance in lines:
    step = 1 if turn == "R" else -1
    for _ in range(distance):
        dial = (dial + step) % 100
        if dial == 0:
            password += 1

print(password)
