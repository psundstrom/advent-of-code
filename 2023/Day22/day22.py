from copy import deepcopy
import plotly.graph_objects as go
from itertools import product
from string import ascii_lowercase
from collections import defaultdict 

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]

print('2023 - Day 22')

with open('./2023/Day22/input.txt') as file:
    lines = [line.rstrip() for line in file]

B={}
R=[]
F=[]
S=defaultdict(list)
for i,line in enumerate(lines):
    start,end=[tuple([int(p) for p in a.split(',')]) for a in line.split('~')]
    lenx=end[0]-start[0]
    leny=end[1]-start[1]
    lenz=end[2]-start[2]
    # print(start,end,lenx,leny,lenz)
    points=[]
    points.append(start)
    if lenx>0:
        for n in range(lenx):
            points.append((points[n][0]+1,points[n][1],points[n][2]))
    elif leny>0:
        for n in range(leny):
            points.append((points[n][0],points[n][1]+1,points[n][2]))
    elif lenz>0:
        for n in range(lenz):
            points.append((points[n][0],points[n][1],points[n][2]+1))
    # print(points)
    name=keywords[i]
    # print(name,points,lenx,leny,lenz,line)
    B[name]=points
    F.append(name)

for i,item in enumerate(B.keys()):
    print(item,B[item],lines[i])


def testcollision(b1,b2):
    # Test if two bricks occupy the same space
    collision=False
    for point in b1:
        if point in b2:
            collision=True
    return collision

def fall(name):
    brick = B[name]
    collision=False
    while not collision:
        z = [p[2] for p in brick]
        if 1 in z:
            break
        # brick_ = deepcopy(brick)
        for i,p in enumerate(brick):
            brick[i]=(p[0],p[1],p[2]-1)
        # brick[0][2]-=1
        # brick[1][2]-=1
        # lower one step
        collision=False
        for name2 in [k for k in reversed(R) if k!=name]:
            brick2=B[name2]
            if testcollision(brick,brick2):
                collision=True
                break
        if collision:
            # Move back up because collision
            for i,p in enumerate(brick):
                brick[i]=(p[0],p[1],p[2]+1)

def check(brick,testbricks,d=1):
    brick_ = deepcopy(brick)
    brick_[0][2]+=d
    brick_[1][2]+=d
    ncollision=0
    for brick2 in testbricks:
        if brick2!=brick:
            if testcollision([brick_,brick2]):
                ncollision+=1
    return ncollision

F.sort(key=lambda x:min([p[2] for p in B[x]]))

for i,name in enumerate(F):
    fall(name)
    R.append(name)

print('fallen')

fig = go.Figure()

print(R)
for name in R:
    x=[p[0] for p in B[name]]
    y=[p[1] for p in B[name]]
    z=[p[2] for p in B[name]]
    print(x)
    print(y)
    print(z)    
    fig.add_trace(go.Scatter3d(x=x,y=y,z=z,name=name))

fig.show()

# for key in B.keys():
#     print(key,B[key])

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')