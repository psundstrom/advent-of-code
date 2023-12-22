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
    brick=[[int(p) for p in a.split(',')] for a in line.split('~')]
    name=keywords[i]
    B[name]=brick
    if brick[0][2]==1 or brick[1][2]==1:
        R.append(name)
    else:
        F.append(name)

def testcollision(b1,b2):
    bricks=[b1,b2]
    # Test if two bricks occupy the same space
    p=[[],[]] # list of points for each brick
    for j,brick in enumerate(bricks):
        for i in 0,1,2:
            if brick[0][i]!=brick[1][i]:
                for n in range(min(brick[0][i],brick[1][i]),max(brick[0][i],brick[1][i])+1):
                    point=[0,0,0]
                    point[i]=n
                    for ix in [ix for ix in [0,1,2] if ix!=i]:
                        point[ix]=brick[0][ix]
                    p[j].append(tuple(point))
    
    collision=False
    for point in p[0]:
        if point in p[1]:
            collision=True
    return collision

def fall(name):
    brick = B[name]
    collision=False
    while not collision:
        if brick[0][2]==1 or brick[0][2]==1:
            break
        brick_ = deepcopy(brick)
        brick_[0][2]-=1
        brick_[1][2]-=1

        collision=False
        for name2 in [k for k in reversed(R) if k!=name]:
            brick2=B[name2]
            if testcollision(brick_,brick2):
                collision=True
                break
        if not collision:
            brick[0][2]-=1
            brick[1][2]-=1

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

F.sort(key=lambda x:min(B[x][0][2],B[x][1][2]))

for i,name in enumerate(F):
    print(i,name)
    fall(name)
    R.append(name)

print('fallen')

fig = go.Figure()

for name in R:
    x=[B[name][0][0],B[name][1][0]]
    y=[B[name][0][1],B[name][1][1]]
    z=[B[name][0][2],B[name][1][2]]
    fig.add_trace(go.Scatter3d(x=x,y=y,z=z,name=name))

fig.show()

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')