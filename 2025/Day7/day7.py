print("2025 - Day 7")
from functools import cache

with open("./2025/Day7/input.txt") as file:
    lines = [line.rstrip() for line in file]

for r, line in enumerate(lines):
    if "S" in line:
        beams = [(r, line.index("S"))]

@cache
def propagate(beam):
    r, c = beam
    if r == len(lines):
        return 1
    if lines[r][c] == "^":
        return propagate((r + 1, c - 1)) + propagate((r + 1, c + 1))
    else:
        return propagate((r + 1, c))


p2 = propagate(beams[0])

p1 = 0
for i, line in enumerate(lines):
    if not all([b[0] == i for b in beams]):
        assert False
    while any([b[0] == i for b in beams]):
        r, c = beams.pop(0)
        if lines[r][c] == "^":
            p1 += 1
            for cc in [c + 1, c - 1]:
                if 0 <= cc < len(lines[0]) and (r + 1, cc) not in beams:
                    beams.append((r + 1, cc))
        else:
            if (r + 1, c) not in beams:
                beams.append((r + 1, c))

print("------------------------")
print("Part 1:", p1)
print("------------------------")
print("Part 2:", p2)
print("------------------------")
