print('2023 - Day 9')


with open('./2023/Day9/input.txt') as file:
    lines = [line.rstrip() for line in file]

vectors = [[int(n) for n in line.split()] for line in lines]

def extend(g):
    v = g.copy()
    ends = []
    while not all(b == 0 for b in v):
        ends.append(v[-1])
        v = [v[a]-v[a-1] for a in range(1,len(v))]
    ends.reverse()
    val = v[-1]
    for item in ends:
        val = item+val
    return val

def prepend(g):
    v = g.copy()
    starts = []
    while not all(b == 0 for b in v):
        starts.append(v[0])
        v = [v[a]-v[a-1] for a in range(1,len(v))]
    starts.reverse()
    val = v[1]
    for item in starts:
        val = item-val
    return val

print('------------------------')
print('Part 1:',sum(extend(v) for v in vectors))
print('------------------------')
print('Part 2:',sum(prepend(v) for v in vectors))
print('------------------------')