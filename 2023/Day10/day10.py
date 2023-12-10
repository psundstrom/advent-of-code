print('2023 - Day 10')

with open('./2023/Day10/input.txt') as file:
    lines = [line.rstrip() for line in file]

for i,line in enumerate(lines):
    if 'S' in line:
        start=[i,line.find('S')]
    print(line)

print('Start at ({},{})'.format(start[0],start[1]),lines[start[0]][start[1]])

startx=start[0]
starty=start[1]

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.

pipes={
    '|': {(1,0):(1,0), (-1,0):(-1,0)},
    '-': {(0,1):(0,1), (0,-1):(0,-1)},
    'L': {(1,0):(0,1), (0,-1):(-1,0)},
    'J': {(1,0):(0,-1), (0,1):(-1,0)},
    '7': {(-1,0):(0,-1), (0,1):(1,0)},
    'F': {(-1,0):(0,1), (0,-1):(1,0)},
    '.': {},
}

def printposition(x,y):
    for xx in [-1,0,1]:
        p = ''
        for yy in [-1,0,1]: 
            p+=lines[x+xx][y+yy]
        print(p)

printposition(startx,starty)
# for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
# # for dx in [-1,0,1]:
# #     # p = ''
# #     for dy in [-1,0,1]:
#     v = lines[startx+dx][starty+dy] 
#     # p+=lines[startx+dx][starty+dy]
#     if (dx,dy) in pipes[v].keys():
#         print((dx,dy),v)

x=start[0]
y=start[1]
dx=0
dy=1
dist={}
visited=[(x,y)]
dist[(x,y)]=0
print('At',x,y)
d=0

for dx,dy in [(0,1),(-1,0)]:
    x=start[0]
    y=start[1]
    d=0
    while True:
        # printposition(x,y)
        # x_=x
        # y_=y
        x=x+dx
        y=y+dy
        d+=1
        if lines[x][y]=='S':
            break
        if (x,y) in dist.keys():
            dist[(x,y)] = min(dist[(x,y)],d)
            # print('redist',x,y,lines[x][y],dist[(x,y)],d)
        else:
            # if (x,y) in dist.keys():
            #     print(d,dist[(x,y)])
            # print('dist',x,y,lines[x][y],d)
            dist[(x,y)]=d
        if lines[x][y]=='.':
            print('Fail')
            break
        # print('At',lines[x][y],dx,dy)
        visited.append((x,y))
        if x<0 or x>=len(lines):
            print('Out of bounds x',x)
            break

        dx,dy = pipes[lines[x][y]][(dx,dy)]

        # for xx in [-1,0,1]:
        #     for yy in [-1,0,1]:
        # for xx,yy in [(1,0),(-1,0),(0,1),(0,-1)]:
        #     if 0<=x+xx<len(lines)-1 and 0<=y+yy<len(lines[0])-1:
        #         v = lines[x+xx][y+yy]
        #         if (x+xx,y+yy) not in visited and (dx,dy) in pipes[v].keys():
        #             print(x,y,(xx,yy),v)
        #             dx=xx
        #             dy=yy

#   1. Set Q to the empty queue or stack.
#   2. Add node to the end of Q.
#   3. While Q is not empty:
#   4.   Set n equal to the first element of Q.
#   5.   Remove first element from Q.
#   6.   If n is Inside:
#          Set the n
#          Add the node to the west of n to the end of Q.
#          Add the node to the east of n to the end of Q.
#          Add the node to the north of n to the end of Q.
#          Add the node to the south of n to the end of Q.
#   7. Continue looping until Q is exhausted.
#   8. Return.

enclosed={}
tiles = [k for k in dist.keys()]
for x0 in range(len(lines)):
    for y0 in range(len(lines[0])):
        if (x0,y0) in tiles:
            enclosed[(x0,y0)]=False
            break
        # enclosed[(x0,y0)]=True
        Q = [(x0,y0)]
        x,y = Q.pop()
        if (x,y) in tiles:
            pass
        elif x<0 or x>len(lines) or y<0 or y>len(lines[0]):
            enclosed[(x0,y0)]=False
        else:
            for xx,yy in [(1,0),(-1,0),(0,1),(0,-1)]:
                Q.append((x+xx,y+yy))

print(len(enclosed),len(lines)*len(lines[0]))

print(sum([1 for key in enclosed.keys() if enclosed[key]]))

print(enclosed)

print('------------------------')
print('Part 1:',max(dist.values()))
print('------------------------')
print('Part 2:',0)
print('------------------------')