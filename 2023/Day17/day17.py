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

start=((0,0),)
goal=(R-1,C-1)

SEEN={start}
Q.append(start)
H[0][0]=M[0][0]

D={
    (1,0): [(1,0), (0,-1), (0,1)], 
    (-1,0): [(-1,0), (0,-1), (0,1)],
    (0,1): [(0,1), (-1,0), (1,0)],
    (0,-1): [(0,-1), (-1,0), (1,0)],
}

def value(p):
    print('p:',p)
    return H[p[0][0]][p[0][1]]

def printq(current):
    # c is ((),(),(),())
    for r,row in enumerate(M):
        g=''
        for c,n in enumerate(row):
            if (r,c)==current[0]:
                g+=green(str(n))
            elif (r,c) in current[1:]:
                g+=yellow('o')
            else:
                g+=str(n)
        print(g)
    

def printmap():
    for r,row in enumerate(M):
        g=''
        for c,n in enumerate(row):
            if (r,c) in [c[0] for c in SEEN]:
                g+=green(str(n))
            elif (r,c) in [c[0] for c in Q]:
                g+=yellow('o')
            else:
                g+=str(n)
        print(g)

# Keep track of travelled paths
# State = current,current-1,current-2,current-3
# Add (current,current-1,current-2,current-3) to Q
# current is the node we are investigating
# check previous directions to know what positions are allowed
# add neighbours as usual, for each state in queue
# Set tentative as usual

print(Q)
while Q:
    print(Q)
    Q.sort(key=value)
    current = Q.pop(0)
    if (current[0][0],current[0][1])==goal:
        break
    r,c = current[0]
    nod=[]
    if len(current)>1:
        nod.append((current[1][0]-current[0][0],current[1][1]-current[0][1]))
    if len(current)>3:
        # Check if all four is on a row or column
        rh = set([r for r,c in current])
        ch = set([c for r,c in current])
        if len(rh)==1:
            nod.extend([(0,1),(0,-1)])
        elif len(ch)==1:
            nod.extend([(1,0),(-1,0)])
    for dr,dc in [(dr,dc) for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)] if (dr,dc) not in nod]:
        rr=r+dr
        cc=c+dc
        if 0<=rr<R and 0<=cc<C and ((rr,cc),)+current[1:] not in SEEN:
            tentative = H[r][c]+M[rr][cc]
            if tentative<H[rr][cc]:
                PREV[(rr,cc)]=(r,c)
                H[rr][cc]=tentative
                Q.append(((rr,cc),)+current[:3])
    SEEN.add(current)
    printmap()
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