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
D={'.':[(1,0),(-1,0),(0,1),(0,-1)],'<':[(0,-1)],'>':[(0,1)],'v':[(1,0)],'^':[(-1,0)]}
PATHS=[]
part2=True
while Q:
    # Q.sort(key=lambda x:DIST[x])
    current=Q.popleft()
    r,c=current[0]
    if (r,c) == goal:
        PATHS.append(current)
        print(DIST[(r,c)])
    for dr,dc in D['.' if part2 else M[r][c]]:
        rr=r+dr
        cc=c+dc
        if 0<=rr<R and 0<=cc<C and (rr,cc) not in current and M[rr][cc]!='#':
            if DIST[(r,c)]+1>DIST[(rr,cc)]:
                DIST[(rr,cc)]=DIST[(r,c)]+1
                Q.append(((rr,cc),)+current)
    SEEN.add(current)

ans = max([len(path)-1 for path in PATHS])
print(ans)

for path in PATHS:
    if len(path)-1==ans:
        longest=path

print(longest[0],goal)

for r,row in enumerate(M):
    g=''
    for c,ch in enumerate(row):
        if (r,c) in longest:
            g+=green('O')
        else:
            g+=ch
    print(g)

# print(SEEN)
# print(DIST[goal])

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')