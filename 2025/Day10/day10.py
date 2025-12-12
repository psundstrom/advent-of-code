print("2025 - Day 10")
from itertools import combinations
from scipy.optimize import milp, LinearConstraint
import numpy as np

with open("./2025/Day10/input.txt") as file:
    lines = [line.rstrip() for line in file]

targets = []
wirings = []
joltages = []

for line in lines:
    parts = line.split()
    targets.append([c == "#" for c in parts[0][1:-1]])
    joltages.append(tuple(map(int, parts[-1][1:-1].split(","))))
    wirings.append([tuple(map(int, s[1:-1].split(","))) for s in parts[1:-1]])

sequences = [None for _ in targets]
for i, (target, wiring) in enumerate(zip(targets, wirings)):
    for n in range(len(wiring)):
        found = False
        for c in combinations(wiring, n + 1):
            lights = [False for _ in target]
            for s in c:
                for j in s:
                    lights[j] = not lights[j]
            if lights == target:
                sequences[i] = c
                break
        if sequences[i] is not None:
            break

p1 = sum([len(s) for s in sequences])


target = joltages[0]
wiring = wirings[0]

p2 = 0
for wiring, joltage in zip(wirings, joltages):
    # (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
    A = np.matrix([[0 for _ in wiring] for __ in joltage])
    b = np.array([x for x in joltage])
    for i, jolt in enumerate(joltage):
        for j, wire in enumerate(wiring):
            A[i, j] = 1 if i in wire else 0

    c = [1 for _ in wiring]
    integrality = c
    constraints = LinearConstraint(A, b, b)

    res = milp(c=c, constraints=constraints, integrality=integrality)
    p2 += int(sum(res.x))

print("------------------------")
print("Part 1:", p1)
print("------------------------")
print("Part 2:", p2)
print("------------------------")
