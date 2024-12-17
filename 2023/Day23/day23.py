from collections import deque, defaultdict

def green(str):
    return f"\033[92m{str}\033[00m"
def red(str):
    return f"\033[91m{str}\033[00m"
def yellow(str):
    return f"\u001b[33m{str}\033[00m"

print('2023 - Day 23')

with open('./2023/Day23/input.txt') as file:
    M = [line.rstrip() for line in file]

R = len(M)
C = len(M[0])
start=(0,M[0].find('.'))
goal=(len(M)-1,M[-1].find('.'))

# for line in M:
#     print(line)

print(start,goal)

Q = deque()
Q.append((start,))

SEEN=set()
DIST=defaultdict(lambda:-1) #=0?
DIST[start]=0
D={'.':[(0,-1),(-1,0),(0,1),(1,0)],'<':[(0,-1)],'>':[(0,1)],'v':[(1,0)],'^':[(-1,0)]}
PATHS=[]
part2=True

EDGES={}

# From this intersection, find the rest

# START
# Search for an intersection
# Find intersection
# Store distance from start to intersection
# Search in all directions for intersections
# Find intersection -> store distance from previous intersection to the current one
INT = set()

# Start
# Distance to next intersection from here

def is_intersection(r,c):
    n=0
    for dr,dc in D['.' if part2 else M[r][c]]:
        rr=r+dr
        cc=c+dc
        if 0<=rr<R and 0<=cc<C and (rr,cc) and M[rr][cc]!='#':
            n+=1
            if DIST[(r,c)]+1>DIST[(rr,cc)]+10:
                DIST[(rr,cc)]=DIST[(r,c)]+1
                Q.append(((rr,cc),)+current)
    if n>2:
        return True
    return False   

# def next_intersection(start,direction):
#     r,c = start
#     dr,dc = direction
#     rr=r+dr
#     cc=c+dc
#     while not is_intersection(rr,cc):        
#         for ddr,ddc in D['.' if part2 else M[r][c]]:
#             if (ddr,ddc)!=(-dr,-dc):
#                 rrr=rr+dr
#                 ccc=cc+dc
#                 if 0<=rrr<R and 0<=ccc<C and M[rrr][ccc]!='#':
#                     rr=rrr
#                     cc=ccc
#                     continue                    
#     return rr,cc

while Q:
    # Q.sort(key=lambda x:DIST[x])
    current=Q.popleft()
    r,c=current[0]
    if (r,c) == goal:
        PATHS.append(current)
        # print(DIST[(r,c)])
    
    n=0
    for dr,dc in D['.' if part2 else M[r][c]]:
        rr=r+dr
        cc=c+dc
        if 0<=rr<R and 0<=cc<C and (rr,cc) not in current and M[rr][cc]!='#':
            n+=1
            if DIST[(r,c)]+1>DIST[(rr,cc)]:
                DIST[(rr,cc)]=DIST[(r,c)]+1
            Q.append(((rr,cc),)+current)
    if n>1:
        INT.add((r,c))
        # print(f'intersection at {r},{c}')
    # print('--')
    # for item in Q:
    #     print(item[0])
    # SEEN.add(current)
print(INT)
ans = max([len(path)-1 for path in PATHS])
print(ans)
print(DIST[goal])
for path in PATHS:
    if len(path)-1==ans:
        longest=path

# print(longest[0],goal)

# for r,row in enumerate(M):
#     g=''
#     for c,ch in enumerate(row):
#         if M[r][c]=='.' and is_intersection(r,c):
#             g+=red('X')
#         elif (r,c) in longest:
#             if is_intersection(r,c):
#                 g+=red('X')
#             else:
#                 g+=green('O')
#         else:
#             g+=ch
#     print(g)

# print(SEEN)
# print(DIST[goal])

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')