print('2025 - Day 10')
from itertools import combinations
with open('./2025/Day10/input.txt') as file:
    lines = [line.rstrip() for line in file]

targets=[]
wirings=[]
joltages=[]

for line in lines:
    parts = line.split()
    targets.append([c == '#' for c in parts[0][1:-1]])
    joltages.append(tuple(map(int, parts[-1][1:-1].split(','))))
    wirings.append([tuple(map(int, s[1:-1].split(','))) for s in parts[1:-1]])

sequences=[None for _ in targets]
for i,(target, wiring) in enumerate(zip(targets, wirings)):
    for n in range(len(wiring)):
        found=False
        for c in combinations(wiring, n+1):
            lights = [False for _ in target]
            for s in c:
                for j in s:
                    lights[j]=not lights[j]
            if lights == target:
                sequences[i] = c
                break
        if sequences[i] is not None:
            break

p1 = sum([len(s) for s in sequences])

print('------------------------')
print('Part 1:',p1)
print('------------------------')
print('Part 2:',0)
print('------------------------')