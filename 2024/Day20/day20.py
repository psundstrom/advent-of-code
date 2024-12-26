print('2024 - Day 20')
from collections import deque, defaultdict
from heapq import heappop, heappush

with open('./2024/Day20/input.ex') as file:
    grid = [line.rstrip() for line in file]

for r,row in enumerate(grid):
    if 'S' in row:
        start = (r,row.index('S'))
    if 'E' in row:
        end = (r,row.index('E'))
    print(row)

R = len(grid)
C = len(grid[0])

def printmap(seen):
    for r,row in enumerate(grid):
        toprint=''
        for c,column in enumerate(row):
            if (r,c) == start:
                toprint+='S'
            elif (r,c) == end:
                toprint+='E'
            elif (r,c) in seen:
                toprint+='0'
            else:
                toprint+=column
        print(toprint)

def printcost():
    for r,row in enumerate(grid):
        toprint=''
        for c,column in enumerate(row):
            if (r,c) == start:
                toprint+='S '
            elif (r,c) == end:
                toprint+='E '
            elif COST[r][c]<10000:
                toprint+=f"{str(COST[r][c]):>2}" 
            else:
                toprint+=column+' '
        print(toprint)

D = []

DIST=defaultdict(lambda: 1000)

cheats = []

Q = [(0,0,start)]
SEEN = set()

while Q:
    dist,cheat,pos = heappop(Q)
    r,c = pos
    # if cheat==1 and DIST[(r,c)]<1000 and dist<DIST[(r,c)]:
    #     cheats.append(DIST[(r,c)]-dist)
    #     continue
    if pos==end:
        D.append(dist)
        continue
    if (pos,cheat) in SEEN:
        continue
    SEEN.add((pos,cheat))
    for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        if nr<0 or nr>=R or nc<0 or nc>=C:
            continue
        if grid[nr][nc] in ['.','E']: # and COST[nr][nc]>dist+1:
            if (dist+1,cheat,(nr,nc)) not in Q:
                if cheat==0:
                    DIST[(nr,nc)]=dist+1
                heappush(Q,(dist+1,cheat,(nr,nc)))
        # else:
        #     if cheat==0:
        #         if (dist+1,1,(nr,nc)) not in Q:
        #             heappush(Q,(dist+1,1,(nr,nc)))

# Q = [(0,0,start)]

SEEN = set()
Q = [(DIST[k],0,k) for k in DIST.keys()]
while Q:
    dist,cheat,pos = heappop(Q)
    r,c = pos

    if pos==end:
        D.append(dist)
        continue
    if pos in DIST.keys() and dist>DIST[pos]:
        continue
    # if (pos,cheat) in SEEN:
    #     continue
    # SEEN.add((pos,cheat))
    for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        if nr<0 or nr>=R or nc<0 or nc>=C:
            continue
        if grid[nr][nc] in ['.']: continue# and COST[nr][nc]>dist+1:
        if cheat==0:
            heappush(Q,(dist+1,1,(nr,nc)))

# printmap(SEEN)
print(D)


print(Q)

# for k in DIST.keys():
#     print(k)


# print(cheats)

# printcost()

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')