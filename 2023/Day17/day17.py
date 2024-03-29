print('2023 - Day 17')

from collections import deque

def green(str):
    return f"\033[92m{str}\033[00m"
def red(str):
    return f"\033[91m{str}\033[00m"
def yellow(str):
    return f"\u001b[33m{str}\033[00m"


with open('./2023/Day17/input.txt') as file:
    M = [[int(n) for n in line.rstrip()] for line in file]

H={}
# for row in M:
#     print(row)
#     H.append([100000]*len(row))
R=len(M)
C=len(M[0])

Q = []
# PREV = {}

start=((0,0),)
goal=(R-1,C-1)

SEEN={start}
# PATHS={start}
Q.append(start)
H[((0,0),)]=0

D={
    (1,0): [(1,0), (0,-1), (0,1)], 
    (-1,0): [(-1,0), (0,-1), (0,1)],
    (0,1): [(0,1), (-1,0), (1,0)],
    (0,-1): [(0,-1), (-1,0), (1,0)],
}

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

def getcost(path):
    ans=0
    for r,c in path[:-1]:
        ans+=M[r][c]
    return ans

while Q:
    # Q.sort(key=lambda x:H[x])
    hl=[H[x] for x in Q]
    current = Q.pop(hl.index(min(hl)))
    if current[0]==goal:
        break
    r,c = current[0]
    nod=[]
    currentdir=(0,0)
    if len(current)>1:
        currentdir = (current[0][0]-current[1][0],current[0][1]-current[1][1])
        nod.append((current[1][0]-current[0][0],current[1][1]-current[0][1]))
    if len(current)>10:
        # Check if all four is on a row or column
        rh = set([r for r,c in current[:11]])
        ch = set([c for r,c in current[:11]])
        if len(rh)==1:
            nod.extend([(0,1),(0,-1)])
        elif len(ch)==1:
            nod.extend([(1,0),(-1,0)])
    for dr,dc in [(dr,dc) for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)] if (dr,dc) not in nod]:
        
        if (dr,dc)!=currentdir:
            tc = ((r+4*dr,c+4*dc),(r+3*dr,c+3*dc),(r+2*dr,c+2*dc),(r+1*dr,c+1*dc))
            rr,cc=tc[0]
            if 0<=rr<R and 0<=cc<C and tc+current[:7] not in SEEN: #(rr,cc) not in [c[0] for c in SEEN]:
                tentative = H[current]+sum(M[r_][c_] for (r_,c_) in tc)
                # tentative = H[current]+M[rr][cc]
                if tc+current[:7] not in H.keys() or tentative<H[tc+current[:7]]:
                    H[tc+current[:7]]=tentative
                    Q.append(tc+current[:7])
        else:
            rr,cc=r+dr,c+dc
            if 0<=rr<R and 0<=cc<C and tc+current[:10] not in SEEN: #(rr,cc) not in [c[0] for c in SEEN]:
                tentative = H[current]+M[rr][cc]
                if ((rr,cc),)+current[:10] not in H.keys() or tentative<H[((rr,cc),)+current[:10]]:
                    H[((rr,cc),)+current[:10]]=tentative
                    Q.append(((rr,cc),)+current[:10])
            
    # PATHS.add(current)
    SEEN.add(current[:11])

    if len(Q)==0:
        print('fail')

# for path in PATHS:
#     if path[0]==goal:
#         # print(H[path])
#         print(getcost(path),path)
#         if getcost(path)==101:
#             print(getcost(path))

print(min([H[key] for key in H.keys() if key[0]==goal]))

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')