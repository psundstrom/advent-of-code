print('2024 - Day 12')
from collections import deque

with open('./2024/Day12/input.txt') as file:
    grid = [line.rstrip() for line in file]

R = len(grid)
C = len(grid[0])

def printgrid(P):
    for r in range(R):
        s = ''
        for c in range(C):
            if P and (r,c) in P:
                s+='X'
            else:
                s+=grid[r][c]
        print(s)

SEEN=set()
PLOTS=[]

def fill(r,c):
    Q = deque()
    Q.append((r,c))
    T = grid[r][c]
    P = set()
    while Q:
        r,c = Q.popleft()
        if (r,c) not in P and grid[r][c]==T:
            P.add((r,c))
            for rr,cc in [(r+dr,c+dc) for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]]:
                if (rr,cc) not in P and 0 <= rr < R and 0 <= cc < C:
                    Q.append((rr,cc))
    return P


def score(P):
    area = len(P)
    perimeter = 0
    for (r,c) in P:
        for rr,cc in [(r+dr,c+dc) for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]]:
            if (rr,cc) not in P:
                perimeter+=1
    return area*perimeter

# def score2(P):
#     area = len(P)
#     perimeter=0
#     edge=set()
#     seen=set()
#     for (r,c) in P:
#         for dr,dc in [(1,0),(0,1)]:
#             while (r+dr,c+dc) in P:
#                 edge.add(r+dr,c+dc)
#                 seen.add(r+dr,c+dc)
#                 r=r+dr
#                 c=c+dr
        
#             if (r+dr,c+dc) in P and 
#         for rr,cc in [(r+dr,c+dc) for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]]:
#             if (rr,cc) not in P:
#                 perimeter+=1
#     return area*perimeter

for r in range(R):
    for c in range(C):
        if (r,c) not in SEEN:
            P = fill(r,c)
            SEEN.update(P)
            PLOTS.append(P)

print('------------------------')
print('Part 1:',sum([score(P) for P in PLOTS]))
print('------------------------')
print('Part 2:',0)
print('------------------------')