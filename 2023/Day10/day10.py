print('2023 - Day 10')

with open('./2023/Day10/input.txt') as file:
    lines = [line.rstrip() for line in file]

for i,line in enumerate(lines):
    if 'S' in line:
        start=(i,line.find('S'))

# Direction changes from pipe
pipes={
    '|': {(1,0):(1,0), (-1,0):(-1,0)},
    '-': {(0,1):(0,1), (0,-1):(0,-1)},
    'L': {(1,0):(0,1), (0,-1):(-1,0)},
    'J': {(1,0):(0,-1), (0,1):(-1,0)},
    '7': {(-1,0):(0,-1), (0,1):(1,0)},
    'F': {(-1,0):(0,1), (0,-1):(1,0)},
    '.': {},
}

# Find points on right side of path
right={
    (1,0):(0,-1),
    (-1,0):(0,1),
    (0,1):(1,0),
    (0,-1):(-1,0),
    '|': {(1,0):(0,-1), (-1,0):(0,1)},
    '-': {(0,1):(1,0), (0,-1):(-1,0)},
    'L': {(1,0):(0,-1), (0,1):(1,0)},
    'J': {(-1,0):(0,1), (0,1):(1,0)},
    '7': {(-1,0):(0,1), (0,-1):(-1,0)},
    'F': {(1,0):(0,-1), (0,-1):(-1,0)},
}

def printposition(x,y):
    for xx in [-1,0,1]:
        p = ''
        for yy in [-1,0,1]: 
            p+=lines[x+xx][y+yy]
        print(p)

def printall(lines,tiles,enclosed):
    for x in range(len(lines)):
        g = ''
        for y in range(len(lines[0])):
            g+='O' if (x,y) in enclosed else lines[x][y] if (x,y) in tiles else '.'
        print(g)

def findenclosed(x0,y0,tiles):
    if (x0,y0) in tiles:
        return set([])
    Q=[(x0,y0)]
    contained=set()
    while len(Q)>0:
        x,y=Q.pop()
        if x<0 or x>len(lines) or y<0 or y>len(lines[0]):
            return set([]) # Nothing enclosed if we reach the outside edge
        elif (x,y) not in tiles:
            contained.add((x,y))
        for xx,yy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (x+xx,y+yy) not in tiles and (x+xx,y+yy) not in contained:
                    Q.append((x+xx,y+yy))
    return contained

# Find possible starting directions
dir = []
for pipe in pipes.values():
    for xx,yy in [(1,0),(-1,0),(0,1),(0,-1)]:
        if (xx,yy) in pipes[lines[start[0]+xx][start[1]+yy]].keys():
            if (xx,yy) not in dir:
                dir.append((xx,yy))

# Replace S with proper pipe
for key in pipes.keys():
    for i1,i2 in [(0,1),(1,0)]:
        d1 = tuple([-k for k in dir[i1]])
        d2 = tuple([k for k in dir[i2]])
        if (d1 in pipes[key].keys() and pipes[key][d1]==d2):
            lines[start[0]]=lines[start[0]].replace('S',key)

# Loop through in both directions and store shortest path to each point
dist={}
dist[start]=0
for dx,dy in dir:
    x=start[0]
    y=start[1]
    d=0
    while True:
        x=x+dx
        y=y+dy
        d+=1
        if (x,y)==start:
            break
        if (x,y) in dist.keys():
            dist[(x,y)] = min(dist[(x,y)],d)
        else:
            dist[(x,y)]=d
        dx,dy = pipes[lines[x][y]][(dx,dy)]

# Store path points
tiles=[k for k in dist.keys()]

# Start at center left and move right until path is found, start from there
x0=len(lines)//2
y0=0
while (x0,y0) not in tiles:
    y0+=1
x=x0
y=y0
if lines[x][y]=='L':
    dx=-1
    dy=0
elif lines[x][y]=='F':
    dx=0
    dy=1
elif lines[x][y]=='|':
    dx=-1
    dy=0
else:
    assert False

# Go through path and store points on inside/right side of path
ch=set()
while True:
    x=x+dx
    y=y+dy
    # Right side based on current direction
    dx_,dy_ = right[(dx,dy)]
    ch.add((x+dx_,y+dy_))
    dx,dy = pipes[lines[x][y]][(dx,dy)]
    # Right side based on pipe shape
    if (dx,dy) in right[lines[x][y]].keys():
        dx_,dy_ = right[lines[x][y]][(dx,dy)]
        ch.add((x+dx_,y+dy_))
    if (x,y)==(x0,y0):
        break

enclosed=set()
for x,y in ch:
    if (x,y) not in enclosed and (x,y) not in tiles:
        enclosed.update(findenclosed(x,y,tiles))

print('------------------------')
print('Part 1:',max(dist.values()))
print('------------------------')
print('Part 2:',len(enclosed))
print('------------------------')