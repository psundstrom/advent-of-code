from copy import deepcopy
import plotly.graph_objects as go

print('2023 - Day 22')

with open('./2023/Day22/input.ex') as file:
    lines = [line.rstrip() for line in file]

B=[]
R=[]
F=[]
for line in lines:
    brick=[[int(p) for p in a.split(',')] for a in line.split('~')]
    print(brick)
    if brick[0][2]==1 or brick[1][2]==1:
        R.append(brick)
    else:
        F.append(brick)
print(F)
print(B)

def testcollision(bricks):
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

def fall():
    F.sort(key=lambda x:min(x[0][2],x[1][2])) # Lowest z coordinate first
    for bn in range(len(F)):
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
            if brick_[0][2]==0 or brick_[1][2]==0:
                rcollision=True
                break
            if testcollision([brick_,brick2]):
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

fig = go.Figure()

for i,b in enumerate(R):
    print(b)
    x=[b[0][0],b[1][0]]
    y=[b[0][1],b[1][1]]
    z=[b[0][2],b[1][2]]
    fig.add_trace(go.Scatter3d(x=x,y=y,z=z,name=i))

fig.show()

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')