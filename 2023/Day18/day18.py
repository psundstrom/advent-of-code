print('2023 - Day 18')

with open('./2023/Day18/input.txt') as file:
    lines = [line.rstrip() for line in file]

I1=[]
I2=[]
D = {0:'R',1:'D',2:'L',3:'U'}
for line in lines:
    parts=line.split()
    hx=parts[2][2:-1]
    d2=D[int(hx[-1])]
    n2=int(hx[:-1],16)
    I1.append((parts[0],int(parts[1])))
    I2.append((d2,n2))

def corner(p1,p2,p3):
    x1,y1=p1
    x2,y2=p2
    x3,y3=p3
    if (y1<y2 and x3>x2) or (x1<x2 and y3<y2) or (y1>y2 and x3<x2) or (x1>x2 and y3>y2):
        return 1
    else:
        return -1

def shoelace(points):
    ans=0
    ans2=0
    ans3=0
    corners1=0
    corners2=0
    steps=0
    for i,p2 in enumerate(points):
        p1=points[i-1]
        p3=points[(i+1)%len(points)]
        if corner(p1,p2,p3)==1:
            corners1+=1
        elif corner(p1,p2,p3)==-1:
            corners2+=1
        steps+=abs(p2[0]-p1[0]+p2[1]-p1[1])-1
        ans3+=(p2[0])*(p3[1]-p1[1])

    return int(abs(ans3//2)+max(corners1,corners2)*0.75+min(corners1,corners2)*0.25+steps//2)


def getcorners(I):
    pos=(0,0)
    corners=[]
    
    for inst in I:
        if inst[0]=='U':
            pos=(pos[0]-inst[1],pos[1])
        elif inst[0]=='D':
            pos=(pos[0]+inst[1],pos[1])
        elif inst[0]=='L':
            pos=(pos[0],pos[1]-inst[1])
        elif inst[0]=='R':
            pos=(pos[0],pos[1]+inst[1])
        else:
            assert False
        corners.append(pos)
    return corners

corners1 = getcorners(I1)
corners2 = getcorners(I2)

print('------------------------')
print('Part 1:',shoelace(corners1))
print('------------------------')
print('Part 2:',shoelace(corners2))
print('------------------------')