print('2023 - Day 16')

with open('./2023/Day16/input.txt') as file:
    lines = [line.rstrip() for line in file]

M=[]
for line in lines:
    M.append(line)
    print(line)
R = len(M)
C = len(M[0])


def printbeams():
    bp = [(r,c) for (r,c),d in beams]
    for r,row in enumerate(M):
        g=''
        for c,char in enumerate(row):
            if (r,c) in bp:
                g+='#'
            else:
                g+=char
        print(g)

def step(p,d):
    return p[0]+d[0],p[1]+d[1]

def next(beams):
    addbeams=[]
    removebeams=[]
    for i,(current,d) in enumerate(beams):
        if current[0]<0 or current[0]>R-1 or current[1]<0 or current[1]>C-1:
            removebeams.append(i)
            continue
        c = M[current[0]][current[1]]
        if c == '.':
            beams[i] = (step(current,d),d)
        elif c == '/':
            if d==(0,1):
                d=(-1,0)
            elif d==(0,-1):
                d=(1,0)
            elif d==(1,0):
                d=(0,-1)
            elif d==(-1,0):
                d=(0,1)
            else:
                assert False
            beams[i] = (step(current,d),d)
        elif c == '\\':
            if d==(0,1):
                d=(1,0)
            elif d==(0,-1):
                d=(-1,0)
            elif d==(1,0):
                d=(0,1)
            elif d==(-1,0):
                d=(0,-1)
            else:
                assert False
            beams[i] = (step(current,d),d)
        elif c == '-':
            if d[0]==0:
                beams[i] = (step(current,d),d)
            else:
                beams[i] = (step(current,(0,-1)),(0,-1))
                addbeams.append((step(current,(0,1)),(0,1)))
        elif c == '|':
            if d[1]==0:
                beams[i] = (step(current,d),d)
            else:
                beams[i] = (step(current,(1,0)),(1,0))
                addbeams.append((step(current,(-1,0)),(-1,0)))
    for j in reversed(sorted(removebeams)):
        del beams[j]
    beams.extend(addbeams)
    beams=list(set(beams))
    return beams

energized={(0,0)}
start=(0,0)
d=(0,1)
beams=[(start,d)]

for (r,c),d in beams:
    print(r,c,d)

# while all([(0<=p[0]<R and 0<=p[1]<C) for p,_ in beams]):

upd=[-6,-5,-4,-3,-2,-1]

for i in range(10000):
    beams=next(beams)
    energized.update([p for p,_ in beams if (0<=p[0]<R and 0<=p[1]<C)])
    upd.pop(0)
    upd.append(len(energized))
    if len(set(upd))==1:
        print('end',i)
        break
    # print(i,len(beams),len(energized))
    # printbeams()
    if len(beams)==0:
        print('end',i)
        break

# for r,row in enumerate(M):
#     g=''
#     for c,char in enumerate(row):
#         if (r,c) in energized:
#             g+='#'
#         else:
#             g+=char
#     print(g)

print(len(beams))
print(len(set(beams)))

print(upd)
print('------------------------')
print('Part 1:',len(energized))
print('------------------------')
print('Part 2:',0)
print('------------------------')