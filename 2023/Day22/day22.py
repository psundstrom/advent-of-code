from copy import deepcopy
from itertools import product
from string import ascii_lowercase
from collections import defaultdict, deque

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]

print('2023 - Day 22')

with open('./2023/Day22/input.txt') as file:
    lines = [line.rstrip() for line in file]

B={}
R=[]
F=[]
SUPPORTEDBY=defaultdict(set)
SUPPORTS=defaultdict(set)
for i,line in enumerate(lines):
    start,end=[tuple([int(p) for p in a.split(',')]) for a in line.split('~')]
    lenx=end[0]-start[0]
    leny=end[1]-start[1]
    lenz=end[2]-start[2]
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
    name=keywords[i]
    B[name]=points
    F.append(name)

def testcollision(b1,b2):
    # Test if two bricks occupy the same space
    collision=False
    for point in b1:
        if point in b2:
            collision=True
            break
    return collision

def fall(name):
    brick = B[name]
    collision=False
    while not collision:
        z = [p[2] for p in brick]
        if 1 in z:
            break
        for i,p in enumerate(brick):
            brick[i]=(p[0],p[1],p[2]-1)
        collision=False
        for name2 in [k for k in reversed(R) if k!=name]:
            brick2=B[name2]
            if testcollision(brick,brick2):
                collision=True
                SUPPORTEDBY[name].add(name2)
                SUPPORTS[name2].add(name)
                # break
        if collision:
            # Move back up because collision
            for i,p in enumerate(brick):
                brick[i]=(p[0],p[1],p[2]+1)

F.sort(key=lambda x:min([p[2] for p in B[x]]))

for i,name in enumerate(F):
    fall(name)
    R.append(name)

DIS=set()
for name in B.keys():
    if len(SUPPORTS[name])==0:
        DIS.add(name)
    else:
        red=True
        for name2 in SUPPORTS[name]:
            if len(SUPPORTEDBY[name2])==1:
                red=False
        if red:
            DIS.add(name)

RES={}
for name in B.keys():
    FALLS=set()
    FALLS.add(name)
    Q=deque()
    Q.append(name)
    while Q:
        name1=Q.popleft()
        for name2 in SUPPORTS[name1]:
            if len(SUPPORTEDBY[name2].intersection(FALLS))==len(SUPPORTEDBY[name2]):
                FALLS.add(name2)
                Q.append(name2)
    RES[name]=len(FALLS)-1

print('------------------------')
print('Part 1:',len(DIS))
print('------------------------')
print('Part 2:',sum(RES.values()))
print('------------------------')