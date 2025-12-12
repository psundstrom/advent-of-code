print("2025 - Day 12")

with open("./2025/Day12/input.txt") as file:
    lines = [line.rstrip() for line in file]

solved = 0
unsolved = 0
secondpart = False
boxes = []
nextindex = 0
for line in lines:
    if "x" in line:
        secondpart = True
    if secondpart:
        parts = line.split(":")
        area = tuple(map(int, parts[0].split("x")))
        amounts = tuple(map(int, parts[1].split()))
        if (area[0] * area[1]) < sum([a * sum(b) for a, b in zip(amounts, boxes)]):
            unsolved += 1
        else:
            solved += 1
        continue
    if ":" in line:
        nextindex = int(line[:-1])
        boxes.append([])
    else:
        if line != "":
            boxes[nextindex].extend([1 if c == "#" else 0 for c in line])


print("------------------------")
print("Part 1:", solved)
print("------------------------")
