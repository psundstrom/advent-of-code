from copy import deepcopy

print('2023 - Day 22')

with open('./2023/Day22/input.ex') as file:
    lines = [line.rstrip() for line in file]

B=[]
R=[]
F=[]
for line in lines:
    brick=[[int(p) for p in a.split(',')] for a in line.split('~')]
    print(brick)
    if 1 in brick[0] or 1 in brick[1]:
        R.append(brick)
    else:
        F.append(brick)
print(F)
print(B)

def testcollision(bricks):
    # Test if two bricks occupy the same space
    p=[[[],[],[]],[[],[],[]]]
    for j,brick in enumerate(bricks):
        for i in 0,1,2:
            if brick[0][i]!=brick[1][i]:
                for n in range(min(brick[0][i],brick[1][i]),max(brick[0][i],brick[1][i])+1):
                    p[j][i].append(n)
                    for ix in [ix for ix in [0,1,2] if ix!=i]:
                        p[j][ix].append(brick[0][ix])
    
    collision=False
    for i,coord in enumerate(p[0]):
        for c in coord:
            if c in p[1][i]:
                collision=True
    return collision

def fall():
    F.sort(key=lambda x:min(x[0][2],x[1][2])) # Lowest z coordinate first
    for _ in range(len(F)):
        brick = F.pop(0)
        brick_ = deepcopy(brick)
        brick_[0][2]-=1
        brick_[1][2]-=1
        fcollision=False
        for brick2 in F:
            if testcollision([brick_,brick2]):
                fcollision=True
        rcollision=False
        for brick2 in R:
            if testcollision([brick_,brick2]) or brick_[0][2]==0 or brick_[1][2]==0:
                rcollision=True
        if rcollision:
            R.append(brick)
        elif fcollision:
            F.append(brick)
        else:
            F.append(brick_)

for item in F:
    print(item)

while len(F)>0:
    fall()
    print(F)
    print(R)

print('fallen')

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')