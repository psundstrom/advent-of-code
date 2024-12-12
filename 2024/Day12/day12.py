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

def score(P,part2=False):
    area = len(P)
    perimeter = 0
    edges={
        (1,0):[],
        (-1,0):[],
        (0,1):[],
        (0,-1):[],
    }

    for (r,c) in P:
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            rr,cc = r + dr, c + dc
            if (rr,cc) not in P:
                if (rr,cc) in edges[(dr,dc)]:
                    print('duplicate')
                edges[(dr,dc)].append((rr,cc))
                perimeter+=1
    if not part2:
        return area*perimeter
    
    # consolidate edges
    nedges=0
    for d in [(1,0),(-1,0),(0,1),(0,-1)]:
        rows = set([v[0] for v in edges[d]])
        columns = set([v[1] for v in edges[d]])
        if d in [(1,0),(-1,0)]:
            for row in rows:
                c = [v[1] for v in edges[d] if v[0]==row]
                c.sort()
                pre = -1000
                for v in c:
                    if v-pre==1:
                        pre=v
                        continue
                    else:
                        nedges+=1
                        pre=v
        elif d in [(0,1),(0,-1)]:
            for column in columns:
                r = [v[0] for v in edges[d] if v[1]==column]
                r.sort()
                pre = -1000
                for v in r:
                    if v-pre==1:
                        pre=v
                        continue
                    else:
                        nedges+=1
                        pre=v
    return area*nedges

for r in range(R):
    for c in range(C):
        if (r,c) not in SEEN:
            P = fill(r,c)
            SEEN.update(P)
            PLOTS.append(P)

print('------------------------')
print('Part 1:',sum([score(P) for P in PLOTS]))
print('------------------------')
print('Part 2:',sum([score(P,part2=True) for P in PLOTS]))
print('------------------------')