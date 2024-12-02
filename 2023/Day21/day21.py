print('2023 - Day 21')

def green(str):
    return f"\033[92m{str}\033[00m"
def red(str):
    return f"\033[91m{str}\033[00m"
def yellow(str):
    return f"\u001b[33m{str}\033[00m"

with open('./2023/Day21/input.ex') as file:
    lines = [line.rstrip() for line in file]

M=[]
for r,line in enumerate(lines):
    print(line)
    M.append(line)
    if 'S' in line:
        start=(r,line.find('S'))
    # print(line)
R = len(M)
C = len(M[0])

NEXT={start}

def wrap(r,c):
    if r>=R or r<0:
        r=r%R
    if c>=C or c<0:
        c=c%C
    return r,c
prev=0
dprev=0

steps0=R//2 # steps to get to first edge
steps1=R # steps to next edge

# Step to first edge, then N more
N=4
for _ in range(steps0+N*steps1):
    NEW=set()
    for r,c in NEXT:
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            rr,cc = r+dr,c+dc
            if M[rr%R][cc%C]!='#':
                NEW.add((rr,cc))
    # print(len(NEXT)-prev)
    # print(len(NEXT)-prev-dprev)
    # print(len(NEXT))
    # print('-'*50)
    dprev=len(NEXT)-prev
    prev=len(NEXT)
    NEXT=NEW

def checksquare(rr,cc):
    # Check square with lower corner at rr,cc
    ng=0
    for r in range(rr,rr+R):
        for c in range(cc,cc+C):
            if (r,c) in NEXT:
                ng+=1
    return ng

# for i in range(7):
#     # ng=0
#     # for r in range((i-1)*R,i*R):
#     #     for c in range(C):
#     #         if (r,c) in NEXT:
#     #             ng+=1
#     print(i,checksquare((i-1)*R,0))

# perimeter (outside the first 5 squares)
# start at C, R = 3*R, then C

# CORNERS, always add these
# Check range(-C,2*C) and range(-4*R,-2*R) <- Top corner
corner1 = checksquare(-4*R,-C)+checksquare(-4*R,0)+checksquare(-4*R,C)+checksquare(-3*R,-2*C)+checksquare(-3*R,-C)+checksquare(-3*R,0)+checksquare(-3*R,C)+checksquare(-3*R,2*C)
# Check range(-C,2*C) and range(3*R,5*R) <- Bottom corner
corner2 = checksquare(4*R,-C)+checksquare(4*R,0)+checksquare(4*R,C)+checksquare(3*R,-2*C)+checksquare(3*R,-C)+checksquare(3*R,0)+checksquare(3*R,C)+checksquare(3*R,2*C)
# Check range(-4*C,-2*C), r=0 <- Left corner
corner3 = checksquare(0,-5*C)+checksquare(0,-4*C)+checksquare(0,-3*C)
# Check range(3*C,5*C), r=0 <- Right corner
corner4 = checksquare(0,3*C)+checksquare(0,4*C)+checksquare(0,5*C)

# SLOPES
# Check range(2*C,4*C), r=-R <- Top right slope
slope1 = checksquare(0,2*C)+checksquare(0,3*C)+checksquare(0,4*C)
# Check range(2*C,4*C), r=R <- Bottom right slope
slope2 = checksquare(2*R,2*C)+checksquare(2*R,3*C)+checksquare(2*R,4*C)
# Check range(-3*C,-1*C), r=0 <- Top left slope
slope3 = checksquare(0,-4*C)+checksquare(0,-3*C)+checksquare(0,-2*C)
# Check range(-3*C,-1*C), r=R <- Bottom left slope
slope4 = checksquare(2*R,-4*C)+checksquare(2*R,-3*C)+checksquare(2*R,-2*C)

square1 = checksquare(0,0)
square2 = checksquare(C,0)
# How many slopes?! number of whole squares-3

n1=1
n2=0
for nn in range(N-1):
    n1+=4*sum([1 for _ in range(0,nn,2)])
    n2+=4*sum([1 for _ in range(1,nn,2)])
print(n1,n2)
print(n1*square1+n2*square2+corner1+corner2+corner3+corner4+(N-2)*(slope1+slope2+slope3+slope4))



# for nr,nc in [(-5,0),(-4,1),(-3,2),(-2,3),(-1,4),(0,5),(1,6),(2,7)]:
#     print(nr,nc,checksquare((nr)*R,(nc-3)*C),checksquare((nr)*R,(nc-2)*C),checksquare((nr)*R,(nc-1)*C),checksquare(nr*R,nc*C),checksquare((nr)*R,(nc+1)*C),checksquare((nr)*R,(nc+2)*C))



for r in range(-4*R,5*R):
    g=''
    for c in range(-5*C,6*C):
        if (r,c)==start:
            g+=red('X')
        elif (r,c) in NEXT:
            g+=green('O')
        else:
            g+=M[r%R][c%C]
    print(g)

print(R,C)
print('------------------------')
print('Part 1:',len(NEXT))
print('------------------------')
print('Part 2:',0)
print('------------------------')