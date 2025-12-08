print("2025 - Day 8")
import math

with open("./2025/Day8/input.txt") as file:
    boxes = [tuple(map(int, line.rstrip().split(","))) for line in file]


def get_distance(b1, b2):
    return math.sqrt((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2 + (b1[2] - b2[2]) ** 2)


distances = {}
for b1 in boxes:
    for b2 in boxes:
        if b1 == b2:
            continue
        if (b2, b1) in distances.keys():
            continue
        distances[(b1, b2)] = get_distance(b1, b2)

connectionsets = []
unconnected = [b for b in boxes]

p1 = 1
p2 = 0
for i, ((b1, b2), _) in enumerate(sorted(distances.items(), key=lambda x: x[1])):
    connected = False
    if b1 in unconnected and b2 in unconnected:
        connectionsets.append([b1, b2])
        unconnected.remove(b1)
        unconnected.remove(b2)
        connected = True
    elif (b1 not in unconnected) and (b2 not in unconnected):
        c1 = connectionsets[[b1 in c for c in connectionsets].index(True)]
        c2 = connectionsets[[b2 in c for c in connectionsets].index(True)]
        if c1 != c2:
            connectionsets.remove(c1)
            connectionsets.remove(c2)
            connectionsets.append(list(set(c1) | set(c2)))
        connected = True
    else:
        for c in connectionsets:
            if b1 in unconnected and b2 in c:
                c.append(b1)
                unconnected.remove(b1)
                connected = True
                break
            elif b2 in unconnected and b1 in c:
                c.append(b2)
                unconnected.remove(b2)
                connected = True
                break
    if i == 999:
        p1 = 1
        for item in sorted([len(c) for c in connectionsets], reverse=True)[:3]:
            p1 *= item
    if len(unconnected) == 0 and len(connectionsets) == 1:
        p2 = b1[0] * b2[0]
        break

print("------------------------")
print("Part 1:", p1)
print("------------------------")
print("Part 2:", p2)
print("------------------------")
