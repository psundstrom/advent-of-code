print('2024 - Day 16')
from heapq import heappush, heappop
from collections import defaultdict

with open('./2024/Day16/input.ex3') as file:
    grid = [line.rstrip() for line in file]

for r,row in enumerate(grid):
    if 'S' in row:
        start = (r,row.index('S'))
    if 'E' in row:
        end = (r,row.index('E'))

R = len(grid)
C = len(grid[0])

print(start,end)

SEEN=set()
Q = []
# PREV = {}

dr,dc = 0,1
# start, end = end, start
# dr,dc = dc,dr

Q.append((0, start[0], start[1], dr, dc))

COST = defaultdict(lambda: 1e30) #[[1e30 for _ in range(C)] for __ in range(R)]
PREV = {}

COST[(start[0], start[1], dr, dc)]=0
COST[start] = 0
PATH=set()

def printmap(seen=False,visited=set()):
    for r,row in enumerate(grid):
        toprint=''
        for c,column in enumerate(row):
            if (r,c) == start:
                toprint+='S'
            elif (r,c) == end:
                toprint+='E'
            elif (r,c) in [(q[1],q[2]) for q in Q]:
                toprint+='Q'
            elif (r,c) in visited:
                toprint+='0'
            elif seen and (r,c) in [(q[1],q[2]) for q in SEEN]:
                toprint+='O'
            elif (r,c) in PATH:
                toprint+='O'
            else:
                toprint+=column
        print(toprint)

LEFT = {(-1,0): (0,-1), (1,0): (0,1), (0,-1): (1,0), (0,1): (-1,0)}
RIGHT = {(-1,0): (0,1), (1,0): (0,-1), (0,-1): (-1,0), (0,1): (1,0)}

# printmap()
while Q:
    _, r, c, dr, dc = heappop(Q)
    
    if (r,c) == end:
        if _ < COST[(r,c)]:
            COST[(r,c)] = _
        continue

    if (r,c,dr,dc) in SEEN:
        continue
    
    SEEN.add((r,c,dr,dc))
    
    # If straight
    nr = r+dr
    nc = c+dc

    if (nr,nc) == end:
        pass

    if 0<=nr<R and 0<=nc<C and grid[nr][nc]!='#':
        if COST[(r,c,dr,dc)]+1<COST[(nr,nc,dr,dc)]:
            COST[(nr,nc,dr,dc)] = COST[(r,c,dr,dc)]+1
            if COST[(r,c,dr,dc)]+1<COST[(nr,nc)]:
                COST[(nr,nc)] = COST[(r,c,dr,dc)]+1
                PREV[(nr,nc)] = [(r,c)] #.append((r,c))
            heappush(Q,(COST[(nr,nc,dr,dc)],nr,nc,dr,dc))
        elif COST[(r,c)]+1==COST[(nr,nc,dr,dc)]:
            PREV[(nr,nc)].append((r,c))
    for ndr,ndc in [LEFT[(dr,dc)],RIGHT[(dr,dc)]]:
        if COST[(r,c,dr,dc)]+1000<COST[(r,c,ndr,ndc)]:
            COST[(r,c,ndr,ndc)] = COST[(r,c,dr,dc)]+1000
            heappush(Q,(COST[(r,c,ndr,ndc)],r,c,ndr,ndc))
    pass

def backtrack(source, goal, path=[]):
    path = path + [source]
    if source == goal:
        return [path]
    if source not in PREV.keys():
        return [], set()
    paths = []
    for p in PREV[source]:
        if p not in path:
            newpaths = backtrack(p, goal, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

paths = backtrack(end, start)

visited=set()

for path in paths:
    print(path[0],path[-1])
    visited.update(path)

print(PREV[end])

print(COST[end])

printmap(visited=visited)
# 582 is too high

print('------------------------')
print('Part 1:',COST[end])
print('------------------------')
print('Part 2:',len(visited))
print('------------------------')