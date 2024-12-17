print('2024 - Day 16')
from heapq import heappush, heappop

with open('./2024/Day16/input.txt') as file:
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

Q.append((0, start[0], start[1], 0, 1))

COST = [[1e30 for _ in range(C)] for __ in range(R)]
PREV = [[None for _ in range(C)] for __ in range(R)]

COST[start[0]][start[1]]=0
PATH=set()

def printmap(seen=False):
    for r,row in enumerate(grid):
        toprint=''
        for c,column in enumerate(row):
            if (r,c) == start:
                toprint+='S'
            elif (r,c) == end:
                toprint+='E'
            elif seen and (r,c) in [(q[0],q[1]) for q in SEEN]:
                toprint+='O'
            elif (r,c) in PATH:
                toprint+='O'
            elif (r,c) in [(q[1],q[2]) for q in Q]:
                toprint+='Q'
            else:
                toprint+=column
        print(toprint)

printmap()
while Q:
    cost, r, c, dr, dc = heappop(Q)
    
    if (r,c) == end:
        continue

    if (r,c,dr,dc) in SEEN:
        continue
    
    SEEN.add((r,c,dr,dc))
    
    for ndr, ndc in [(1,0),(0,1),(-1,0),(0,-1)]:
        nr = r+ndr
        nc = c+ndc
        if grid[nr][nc]=='#': continue
        if (ndr,ndc)==(-dr,-dc): continue
        if 0<=nr<R and 0<=nc<C:

            if (ndr,ndc)==(dr,dc) and cost + 1 <= COST[nr][nc]:
                COST[nr][nc] = cost + 1
                PREV[nr][nc] = (r,c)
                heappush(Q,(COST[nr][nc],nr,nc,ndr,ndc))
            elif (ndr,ndc) != (dr,dc) and cost + 1001 <= COST[nr][nc]:
                # COST[nr][nc] = COST[r][c] + 1001
                # PREV[nr][nc] = (r,c)
                heappush(Q,(COST[r][c]+1000,r,c,ndr,ndc))
        # printmap()
        pass

PATH = [end]
next = PREV[end[0]][end[1]]
while next!=start:
    nr,nc = next
    PATH.append(next)
    next = PREV[nr][nc]
PATH.append(start)

printmap()

print(COST[end[0]][end[1]])

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')