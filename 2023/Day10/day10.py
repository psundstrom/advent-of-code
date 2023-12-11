print('2023 - Day 10')

with open('./2023/Day10/input.txt') as file:
    lines = [line.rstrip() for line in file]

for i,line in enumerate(lines):
    if 'S' in line:
        start=(i,line.find('S'))
    print(line)

print('Start at ({},{})'.format(start[0],start[1]),lines[start[0]][start[1]])

startx=start[0]
starty=start[1]

pipes={
    '|': {(1,0):(1,0), (-1,0):(-1,0)},
    '-': {(0,1):(0,1), (0,-1):(0,-1)},
    'L': {(1,0):(0,1), (0,-1):(-1,0)},
    'J': {(1,0):(0,-1), (0,1):(-1,0)},
    '7': {(-1,0):(0,-1), (0,1):(1,0)},
    'F': {(-1,0):(0,1), (0,-1):(1,0)},
    '.': {},
}

right={
    (1,0):(0,-1),
    (-1,0):(0,1),
    (0,1):(1,0),
    (0,-1):(-1,0),
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

printposition(*start)
dir = []
for pipe in pipes.values():
    for xx,yy in [(1,0),(-1,0),(0,1),(0,-1)]:
        if (xx,yy) in pipes[lines[start[0]+xx][start[1]+yy]].keys():
            if (xx,yy) not in dir:
                dir.append((xx,yy))

print(dir)

dist={}
dist[start]=0
d=0
ch=[]
for dx,dy in dir:
    R=dx!=0
    x=start[0]
    y=start[1]
    d=0
    while True:
        if R:
            dx_,dy_ = right[(dx,dy)]
            ch.append((x+dx_,y+dy_))
        x=x+dx
        y=y+dy
        d+=1
        if lines[x][y]=='S':
            break
        if (x,y) in dist.keys():
            dist[(x,y)] = min(dist[(x,y)],d)
        else:
            dist[(x,y)]=d
        if lines[x][y]=='.':
            print('Fail')
            break
        if x<0 or x>=len(lines):
            print('Out of bounds x',x)
            break
        dx,dy = pipes[lines[x][y]][(dx,dy)]
        if R:
            dx_,dy_ = right[(dx,dy)]
            ch.append((x+dx_,y+dy_))

print(len(dist.keys()))

def findenclosed(x0,y0,tiles):
    if (x0,y0) in tiles:
        return set([])
    # print(x0,y0)
    Q=[(x0,y0)]
    contained=set()
    while len(Q)>0:
        x,y=Q.pop()
        # print(x,y)
        if x<0 or x>len(lines) or y<0 or y>len(lines[0]):
            # print('BLA----',len(contained))
            pass
            # return set([]) # Nothing enclosed if we reach the outside edge
        elif (x,y) not in tiles:
            # print('enclosed tile')
            contained.add((x,y))
            # print(contained)
        for xx,yy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (x+xx,y+yy) not in tiles and (x+xx,y+yy) not in contained:
                    Q.append((x+xx,y+yy))
    # if len(contained)==1:
    #     for item in contained:
    #         printposition(*item)
    # print('HALLOOO',len(contained))
    return contained

tiles=[k for k in dist.keys()]
# print(ch)
# print(len(ch))

# print(len([lines[x][y] for x,y in dist.keys() if lines[x][y] in ['-','|']]))

dx,dy=dir[0]
x=start[0]
y=start[1]
ch=[]
while True:
    dx_,dy_ = right[(dx,dy)]
    ch.append((x+dx_,y+dy_))
    x=x+dx
    y=y+dy
    if lines[x][y]=='S':
        break
    dx,dy = pipes[lines[x][y]][(dx,dy)]
    dx_,dy_ = right[(dx,dy)]
    ch.append((x+dx_,y+dy_))

# assert(False)
enclosed=set()
for x,y in ch:
    if (x,y) not in enclosed:
        enclosed.update(findenclosed(x,y,tiles))

# enclosed=set()
# for x,line in enumerate(lines):
#     inside=False
#     for y,c in enumerate(line):
#         if (x,y) in tiles and c in ['S','|','L','F','J','7']:
#             inside=not inside
#         if inside and (x,y) not in tiles:
#             enclosed.add((x,y))

# printall(lines,[],[])
# print('-')
printall(lines,tiles,enclosed)
# print('-')
# printall(lines,tiles,ch)
# print('-')
# # print(enclosed)
print(len(enclosed))

print('------------------------')
print('Part 1:',max(dist.values()))
print('------------------------')
print('Part 2:',0)
print('------------------------')