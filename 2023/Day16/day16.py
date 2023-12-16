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

def next(beams):
    addbeams=[]
    removebeams=[]
    for i,(current,d) in enumerate(beams):
        if current[0]<0 or current[0]>R-1 or current[1]<0 or current[1]>C-1:
            removebeams.append(i)
            continue
        c = M[current[0]][current[1]]
        if c == '.':
            beams[i] = (step(current,d),d)
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
            beams[i] = (step(current,d),d)
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
            beams[i] = (step(current,d),d)
        elif c == '-':
            if d[0]==0:
                beams[i] = (step(current,d),d)
            else:
                beams[i] = (step(current,(0,-1)),(0,-1))
                addbeams.append((step(current,(0,1)),(0,1)))
        elif c == '|':
            if d[1]==0:
                beams[i] = (step(current,d),d)
            else:
                beams[i] = (step(current,(1,0)),(1,0))
                addbeams.append((step(current,(-1,0)),(-1,0)))
    for j in reversed(sorted(removebeams)):
        del beams[j]
    beams.extend(addbeams)
    beams=list(set(beams))
    return beams

def solve(start,d):
    energized={start}
    beams=[(start,d)]
    upd=[-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
    for i in range(10000):
        beams=next(beams)
        energized.update([p for p,_ in beams if (0<=p[0]<R and 0<=p[1]<C)])
        upd.pop(0)
        upd.append(len(energized))
        if len(set(upd))==1:
            break
        if len(beams)==0:
            break
    return len(energized)

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