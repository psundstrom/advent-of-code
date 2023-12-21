print('2023 - Day 18')

def green(str):
    return f"\033[92m{str}\033[00m"
def red(str):
    return f"\033[91m{str}\033[00m"
def yellow(str):
    return f"\u001b[33m{str}\033[00m"

with open('./2023/Day18/input.ex') as file:
    lines = [line.rstrip() for line in file]

def determinant(p1,p2):
    #det([a,b;c d])=ad-bc
    #det([x1 x2;y1 y2])=x1*y2-x2*y1
    print(f'{p1[0]}*{p2[1]}-{p1[1]}*{p2[0]}=',p1[0]*p2[1]-p1[1]*p2[0])
    return p1[0]*(p2[1])-(p1[1])*(p2[0])

def shoelace(points):
    ans=0
    ans2=0
    ans3=0
    for i,p2 in enumerate(points):
        p1=points[i-1]
        p3=points[(i+1)%len(points)]
        # ans+=(p2[0]-p1[0]+(0 if p2[0]!=p1[0] else 0))*(p1[1]+p2[1])//2
        ans+=determinant(p2,p1)
        # print(ans,p1,p2,p2[0]-p1[0],(p1[1]+p2[1])//2)
        ans2+=(p2[1]-1)*(p1[0]-p3[0])
        ans3+=(p2[0]-1)*(p3[1]-p1[1])
        print(ans//2,ans2//2,ans3//2)

    return ans//2,ans2//2,ans3//2

# Each hexadecimal code is six hexadecimal digits long. 
# The first five hexadecimal digits encode the distance 
# in meters as a five-digit hexadecimal number. The last 
# hexadecimal digit encodes the direction to dig: 0 means 
# R, 1 means D, 2 means L, and 3 means U.

I=[]
for line in lines:
    parts=line.split()
    I.append((parts[0],int(parts[1]),parts[2][1:-1]))

pos=(0,0)
SEEN=set()
SEEN.add(pos)

PATH=[pos]

CORNERS=[pos]
STEPS=0

for inst in I:
    for _ in range(inst[1]):
        if inst[0]=='U':
            pos=(pos[0]-1,pos[1])
        elif inst[0]=='D':
            pos=(pos[0]+1,pos[1])
        elif inst[0]=='L':
            pos=(pos[0],pos[1]-1)
        elif inst[0]=='R':
            pos=(pos[0],pos[1]+1)
        else:
            assert False
        SEEN.add(pos)
        PATH.append(pos)
    CORNERS.append(pos)
    STEPS+=inst[1]*{'D':1, 'U':-1, 'R':1,'L':-1}[inst[0]]
rs = [p[0] for p in SEEN]
cs = [p[1] for p in SEEN]

Q=[]
Q.append((1,1)) #(55,16))
FILLED=set()
while Q:
    (r,c) = Q.pop(0)
    if (r,c) not in SEEN and (r,c) not in FILLED:
        FILLED.add((r,c))
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            rr,cc = r+dr,c+dc
            Q.append((rr,cc))

def printmap():
    for r in range(min(rs),max(rs)+1):
        g=''
        for c in range(min(cs),max(cs)+1):
            if (r,c)==(315,14):
                pass
            if (r,c) in SEEN:
                if (r,c) in CORNERS:
                    g+=green('#')
                else:
                    g+=red('#')

            elif (r,c) in FILLED:
                g+=yellow('O')
            else:
                g+='.'
        print(g)

# ans=0
# for i,p2 in enumerate(CORNERS):
#     p1=CORNERS[i-1]
#     # ans+=(p2[0]-p1[0]+(0 if p2[0]!=p1[0] else 0))*(p1[1]+p2[1])//2
#     ans+=determinant(p2,p1)
#     # print(ans,p1,p2,p2[0]-p1[0],(p1[1]+p2[1])//2)
# print(ans//2)



print(shoelace(CORNERS))
print(len(FILLED))
print(len(SEEN))

print(shoelace([(0,0),(0,2),(2,2),(2,0)]))

printmap()

print(CORNERS)

print('------------------------')
print('Part 1:',len(FILLED)+len(SEEN))
print('------------------------')
print('Part 2:',0)
print('------------------------')