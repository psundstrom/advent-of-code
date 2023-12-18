print('2023 - Day 18')

with open('./2023/Day18/input.txt') as file:
    lines = [line.rstrip() for line in file]

# Each hexadecimal code is six hexadecimal digits long. 
# The first five hexadecimal digits encode the distance 
# in meters as a five-digit hexadecimal number. The last 
# hexadecimal digit encodes the direction to dig: 0 means 
# R, 1 means D, 2 means L, and 3 means U.

I=[]
for line in lines:
    parts=line.split()
    I.append((parts[0],int(parts[1]),parts[2][1:-1]))

pos=(0,0)
SEEN=set()
SEEN.add(pos)

for inst in I:
    for _ in range(inst[1]):
        if inst[0]=='U':
            pos=(pos[0]-1,pos[1])
        elif inst[0]=='D':
            pos=(pos[0]+1,pos[1])
        elif inst[0]=='L':
            pos=(pos[0],pos[1]-1)
        elif inst[0]=='R':
            pos=(pos[0],pos[1]+1)
        else:
            assert False
        SEEN.add(pos)

rs = [p[0] for p in SEEN]
cs = [p[1] for p in SEEN]

Q=[]
Q.append((55,16))
FILLED=set()
while Q:
    (r,c) = Q.pop(0)
    if (r,c) not in SEEN and (r,c) not in FILLED:
        FILLED.add((r,c))
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            rr,cc = r+dr,c+dc
            Q.append((rr,cc))

def printmap():
    for r in range(min(rs),max(rs)+1):
        g=''
        for c in range(min(cs),max(cs)+1):
            if (r,c)==(315,14):
                pass
            if (r,c) in SEEN:
                g+='#'
            elif (r,c) in FILLED:
                g+='O'
            else:
                g+='.'
        print(g)

print('------------------------')
print('Part 1:',len(FILLED)+len(SEEN))
print('------------------------')
print('Part 2:',0)
print('------------------------')