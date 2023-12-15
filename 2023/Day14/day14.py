print('2023 - Day 14')

def reset():
    with open('./2023/Day14/input.txt') as file:
        lines = [line.rstrip() for line in file]
    out=[]
    for line in lines:
        out.append(list(line))
    r=len(out)
    c=len(out[0])

    return out

def flatten(M):
    return ''.join([''.join(row) for row in M])

def load(M,x,y):
    if M[x][y]=='O':
        return len(M)-x
    else:
        return 0

def roll(M,d,x,y):
    if M[x][y]!='O':
        return False
    xx=x+d[0]
    yy=y+d[1]
    if 0<=xx<len(M) and 0<=yy<len(M[0]) and M[xx][yy] not in ['#','O']:
        M[x][y]='.'
        M[xx][yy]='O'
        return True

def rollall(M,d):
    moved=True
    while moved:
        moved=False
        for x in range(len(M)):
            for y in range(len(M[0])):
                if roll(M,d,x,y):
                    moved=True

def cycle(M):
    for d in ((-1,0),(0,-1),(1,0),(0,1)):
        rollall(M,d)

def getload(M):
    ans=0
    for x in range(len(M)):
        for y in range(len(M[0])):
            ans+=load(M,x,y)
    return ans

M=reset()
rollall(M,(-1,0))
ans1=getload(M)

SEEN = {}
r=0
r0=0
found1=False
found2=False
key0=None
key1=None
for i in range(1000):
    cycle(M)
    if found1 and not key1 and ''.join([''.join(row) for row in M]) == key0:
        # print('>2',i,i-r0)
        key1=''.join([''.join(row) for row in M])
        # print(key1)
        found2=True
        r=i-r0
        break
    if not key0 and ''.join([''.join(row) for row in M]) in SEEN.keys():
        # print('>1',i)
        key0=''.join([''.join(row) for row in M])
        r0=i
        found1=True

    SEEN[''.join([''.join(row) for row in M])]=i

M=reset()

for i in range(r0+(1000000000-r0)%r):
    cycle(M)
ans2=getload(M)

print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',ans2)
print('------------------------')