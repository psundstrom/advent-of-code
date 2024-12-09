print("2024 - Day 8")

from collections import defaultdict
from itertools import combinations

with open("./2024/Day8/input.txt") as file:
    lines = [line.rstrip() for line in file]

R = len(lines)
C = len(lines[0])

for line in lines:
    print(line)

antennas = defaultdict(list)

for r in range(R):
    for c in range(C):
        if lines[r][c] != ".":
            antennas[lines[r][c]].append((r, c))

print(antennas)


def getantinodes1(a1, a2):
    r1, c1 = a1
    r2, c2 = a2
    dr = r2 - r1
    dc = c2 - c1
    nodes = []
    node1 = (r2 + dr, c2 + dc)
    node2 = (r1 - dr, c1 - dc)
    if 0 <= node1[0] < R and 0 <= node1[1] < C:
        nodes.append(node1)
    if 0 <= node2[0] < R and 0 <= node2[1] < C:
        nodes.append(node2)
    return nodes


def getantinodes2(a1, a2):
    r1, c1 = a1
    r2, c2 = a2
    dr = r2 - r1
    dc = c2 - c1
    nodes = []

    newnode = (r2, c2)
    while 0 <= newnode[0] < R and 0 <= newnode[1] < C:
        nodes.append(newnode)
        newnode = (newnode[0] + dr, newnode[1] + dc)
    newnode = (r1, c1)
    while 0 <= newnode[0] < R and 0 <= newnode[1] < C:
        nodes.append(newnode)
        newnode = (newnode[0] - dr, newnode[1] - dc)

    return nodes


antinodes1 = set()
for k in antennas.keys():
    for a1, a2 in combinations(antennas[k], 2):
        for node in getantinodes1(a1, a2):
            antinodes1.add(node)

antinodes2 = set()
for k in antennas.keys():
    for a1, a2 in combinations(antennas[k], 2):
        for node in getantinodes2(a1, a2):
            antinodes2.add(node)


def printgrid():
    for r, l in enumerate(lines):
        toprint = ""
        for c, v in enumerate(l):
            if (r, c) in antinodes2:
                toprint += "#"
            elif (r, c) in antennas.items():
                toprint += "A"
            else:
                toprint += v
        print(toprint)


print("------------------------")
print("Part 1:", len(antinodes1))
print("------------------------")
print("Part 2:", len(antinodes2))
print("------------------------")
