print('2024 - Day 14')

with open('./2024/Day14/input.txt') as file:
    lines = [line.rstrip() for line in file]

sizex=101
sizey=103

robots=[]
for line in lines:
    parts=line.split(',')
    robots.append((
        int(parts[0].split('=')[-1]),
        int(parts[1].split(' ')[0]),
        int(parts[1].split(' ')[1].split('=')[-1]),
        int(parts[2]),
    ))

def takesteps(robot,n):
    x0=robot[0]
    y0=robot[1]
    vx=robot[2]
    vy=robot[3]
    
    return (x0+vx*n)%sizex,(y0+vy*n)%sizey


def whichquadrant(x,y):
    midx = sizex//2
    midy = sizey//2
    if x<midx and y<midy:
        return 1
    elif x<midx and y>midy:
        return 2
    elif x>midx and y<midy:
        return 3
    elif x>midx and y>midy:
        return 4
    else:
        return 0

quadrants=[0,0,0,0,0]
for robot in robots:
    x,y = takesteps(robot,100)
    quadrants[whichquadrant(x,y)]+=1

print(quadrants)
ans1=1
for q in quadrants[1:]:
    ans1*=q
print(ans1)

def printmap(p):
    for y in range(sizey):
        toprint=''
        for x in range(sizex):
            if (x,y) in p:
                toprint+='X'
            else:
                toprint+='.'
        print(toprint)

SEEN=set()
# Very specific to my input!
for n in [7286]: #[1226+i*101 for i in range(500)]:
    p = [takesteps(robot,n) for robot in robots]
    if tuple(p) in SEEN:
        print('LOOP',n)
        break
    SEEN.add(tuple(p))
    print(n)
    printmap(p)

print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',7286)
print('------------------------')