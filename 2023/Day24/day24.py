print('2023 - Day 24')

with open('./2023/Day24/input.txt') as file:
    lines = [line.rstrip() for line in file]
pmin=200000000000000
pmax=400000000000000
S=[]
for line in lines:
    pos,vel = line.split('@')
    pos = [int(c) for c in pos.split(',')]
    vel = [int(v) for v in vel.split(',')]
    x,y,z=pos
    vx,vy,vz=vel
    S.append((x,y,z,vx,vy,vz))

def intersect(p1,p2):
    x1,y1,z1,vx1,vy1,vz1=p1
    x2,y2,z2,vx2,vy2,vz2=p2
    a1 = vy1/vx1
    b1 = -1
    c1 = -a1*x1+y1
    a2 = vy2/vx2
    b2 = -1
    c2 = -a2*x2+y2
    x=(b1*c2-b2*c1)/(a1*b2-a2*b1)
    y=(a2*c1-a1*c2)/(a1*b2-a2*b1)
    return x,y

# print(intersect(S[0],S[2]))
def checkdirection(p,x,y):
    towards=True
    if (p[0]<x and p[3]<0 or p[0]>x and p[3]>0):
        towards=False
    if (p[1]<y and p[4]<0 or p[1]>y and p[4]>0):
        towards=False
    return towards
    


ans=0
SEEN=set()
for p1 in S:
    for p2 in S:
        if p1[4]/p1[3]!=p2[4]/p2[3] and (p1,p2) not in SEEN and (p2,p1) not in SEEN:
            x,y = intersect(p1,p2)
            if pmin<=x<=pmax and pmin<=y<=pmax and checkdirection(p1,x,y) and checkdirection(p2,x,y):
                ans+=1
                SEEN.add((p1,p2))
print(ans)

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')