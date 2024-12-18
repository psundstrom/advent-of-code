print('2024 - Day 16')
from heapq import heappush, heappop

with open('./2024/Day16/input.ex2') as file:
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

COST = [[1e30 for _ in range(C)] for __ in range(R)]
PREV =  {}

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
            elif (r,c) in [(q[1],q[2]) for q in Q]:
                toprint+='Q'
            elif seen and (r,c) in [(q[0],q[1]) for q in SEEN]:
                toprint+='O'
            elif (r,c) in PATH:
                toprint+='O'
            else:
                toprint+=column
        print(toprint)

LEFT = {(-1,0): (0,-1), (1,0): (0,1), (0,-1): (1,0), (0,1): (-1,0)}
RIGHT = {(-1,0): (0,1), (1,0): (0,-1), (0,-1): (-1,0), (0,1): (1,0)}

printmap()
while Q:
    cost, r, c, dr, dc = heappop(Q)
    
    if (r,c) == end:
        continue

    if (r,c,dr,dc) in SEEN:
        continue
    
    SEEN.add((r,c,dr,dc))
    
    for ndr, ndc in [LEFT[(dr,dc)],RIGHT[(dr,dc)],(dr,dc)]:
        nr = r+ndr
        nc = c+ndc
        if grid[nr][nc]=='#': continue
        # if (ndr,ndc)==(-dr,-dc): continue
        if 0<=nr<R and 0<=nc<C:
            if (ndr,ndc)==(dr,dc) and cost + 1 < COST[nr][nc]:
                COST[nr][nc] = cost + 1
                PREV[(nr,nc)] = [(r,c)]
                heappush(Q,(COST[nr][nc],nr,nc,ndr,ndc))
            if (ndr,ndc)==(dr,dc) and cost + 1 == COST[nr][nc]:
                if (r,c) not in PREV[(nr,nc)]:
                    PREV[(nr,nc)].append((r,c))
                heappush(Q,(COST[nr][nc],nr,nc,ndr,ndc))
            elif (ndr,ndc) != (dr,dc) and cost + 1001 < COST[nr][nc]:
                # COST[nr][nc] = COST[r][c] + 1001
                # PREV[nr][nc] = (r,c)
                heappush(Q,(COST[r][c]+1000,r,c,ndr,ndc))
        printmap(seen=True)
        print(Q)
        print([COST[r][c] for _,r,c,_,_ in Q])
        input()

        pass

# PATHS = [end]
next = PREV[end]
PATH = set()

PATH.add(end)
Q = list(PREV[end])
PREV[start]=[]
while Q:
    r,c = heappop(Q)
    PATH.add((r,c))
    for nr,nc in PREV[(r,c)]:
        heappush(Q,(nr,nc))

# print('ALL:', len(ALL))

# while next:
#     if len(next)>1:
#         pass
#     for r,c in next:
#         if (r,c) in [(11, 133),(9, 115),(49, 83),(51, 133),(85, 139),(37, 29),(113, 127),(39, 51),(29, 1),(131, 79),(55, 3),(15, 21),(65, 15),(61, 19),(95, 85),(135, 21),(77, 31),(79, 29)]:
#             pass
#         ALL.add((r,c))
#     next = [x for xs in [PREV[n] for n in next] for x in xs if x!=start]

print('visited:',len(PATH))

for k,p in PREV.items():
    if len(p)>1:
        print(k,p)
# print(PREV.items())
# PATH.append(start)

printmap()
# print(len(PATH))

# for r,row in enumerate(COST):
#     for c,cost in enumerate(row):
#         if 0<COST[end[0]][end[1]]-cost<10:
#             print(r,c,cost)

print(COST[end[0]][end[1]])

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')