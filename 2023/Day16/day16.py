import functools

print('2023 - Day 16')

with open('./2023/Day16/input.txt') as file:
    lines = [line.rstrip() for line in file]

M=[]
for line in lines:
    M.append(line)
R = len(M)
C = len(M[0])

def printbeams(beams):
    bp = [(r,c) for (r,c),d in beams]
    for r,row in enumerate(M):
        g=''
        for c,char in enumerate(row):
            if (r,c) in bp:
                g+='#'
            else:
                g+=char
        print(g)

def step(p,d):
    return p[0]+d[0],p[1]+d[1]

def next(beams,visited=set()):
    out = set()
    while len(beams)>0:
        (current,d)=beams.pop()
        if (current,d) in visited:
            continue
        else:
            visited.add((current,d))
        if current[0]<0 or current[0]>R-1 or current[1]<0 or current[1]>C-1:
            continue
        c = M[current[0]][current[1]]
        if c == '.':
            out.add((step(current,d),d))
        elif c == '/':
            if d==(0,1):
                d=(-1,0)
            elif d==(0,-1):
                d=(1,0)
            elif d==(1,0):
                d=(0,-1)
            elif d==(-1,0):
                d=(0,1)
            else:
                assert False
            out.add((step(current,d),d))
        elif c == '\\':
            if d==(0,1):
                d=(1,0)
            elif d==(0,-1):
                d=(-1,0)
            elif d==(1,0):
                d=(0,1)
            elif d==(-1,0):
                d=(0,-1)
            else:
                assert False
            out.add((step(current,d),d))
        elif c == '-':
            if d[0]==0:
                out.add((step(current,d),d))
            else:
                out.add((step(current,(0,-1)),(0,-1)))
                out.add((step(current,(0,1)),(0,1)))
        elif c == '|':
            if d[1]==0:
                out.add((step(current,d),d))
            else:
                out.add((step(current,(1,0)),(1,0)))
                out.add((step(current,(-1,0)),(-1,0)))
    return out,visited

def solve(start,d):
    beams={(start,d)}
    visited=set()
    while True:
        beams,visited=next(beams,visited)
        if len(beams)==0:
            break
    return len(set([p for p,_ in visited if (0<=p[0]<R and 0<=p[1]<C)]))

start=(0,0)
d=(0,1)
ans1 = solve(start,d)

ans2 = 0
for i,start in enumerate([(r,0) for r in range(R)]):
    d=(0,1)
    n = solve(start,d)
    ans2=max(n,ans2) 
for i,start in enumerate([(r,C-1) for r in range(R)]):
    d=(0,-1)
    n = solve(start,d)
    ans2=max(n,ans2) 
for i,start in enumerate([(0,c) for c in range(C)]):
    d=(1,0)
    n = solve(start,d)
    ans2=max(n,ans2) 
for i,start in enumerate([(R-1,c) for c in range(C)]):
    d=(-1,0)
    n = solve(start,d)
    ans2=max(n,ans2) 

print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',ans2)
print('------------------------')