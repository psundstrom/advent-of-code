print('2023 - Day 17')

from collections import deque

def green(str):
    return f"\033[92m{str}\033[00m"
def red(str):
    return f"\033[91m{str}\033[00m"
def yellow(str):
    return f"\u001b[33m{str}\033[00m"


with open('./2023/Day17/input.ex') as file:
    M = [[int(n) for n in line.rstrip()] for line in file]

H=[]
for row in M:
    print(row)
    H.append([100000]*len(row))
R=len(M)
C=len(M[0])

Q = []
PREV = {}

# start=(0,0,(1,0))
goal=(R-1,C-1)

Q.append((0,0,(1,0)))
Q.append((0,0,(0,1)))
SEEN={(0,0)}

H[0][0]=M[0][0]

D={
    (1,0): [(1,0), (0,-1), (0,1)], 
    (-1,0): [(-1,0), (0,-1), (0,1)],
    (0,1): [(0,1), (-1,0), (1,0)],
    (0,-1): [(0,-1), (-1,0), (1,0)],
}

def value(p):
    return H[p[0]][p[1]]

while Q:
    Q.sort(key=value)
    current = Q.pop(0)
    # if (current[0],current[1])==goal:
    #     pass
    r,c,d = current
    s=(r,c)
    history = [s]
    for i in range(3):
        if s in PREV.keys():
            history.append(PREV[s])
            s=PREV[s]
    if len(history)==4:
        rs = set([p[0] for p in history])
        cs = set([p[1] for p in history])

        if len(rs)==1:
            nod = [(0,1),(0,-1)]
        elif len(cs)==1:
            nod = [(1,0),(-1,0)]
    else:
        nod=[]

    for (rr,cc,dd) in [(r+dr,c+dc,(dr,dc)) for dr,dc in D[d] if (dr,dc) not in nod]:
        if 0<=rr<R and 0<=cc<C and (rr,cc) not in SEEN:
            tentative = H[r][c]+M[rr][cc]
            if tentative<H[rr][cc]:
                PREV[(rr,cc)]=(r,c)
                H[rr][cc]=tentative
                Q.append((rr,cc,dd))
    SEEN.add((r,c))
    # if (r,c)==goal:
    #     break
    if len(Q)==0:
        print('fail')

print(H)
print(H[R-1][C-1])
# print(PREV)

next=(R-1,C-1)
PATH=[next]
while next!=(0,0):
    PATH.append(PREV[next])
    next=PREV[next]

for r,row in enumerate(M):
    g=''
    for c,n in enumerate(row):
        if (r,c) in PATH:
            g+="\033[92m#\033[00m"
        elif (r,c) not in SEEN:
            g+=f"\033[91m{n}\033[00m"
        else:
            g+=str(n)
    print(g)


print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')