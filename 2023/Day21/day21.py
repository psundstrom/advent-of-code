print('2023 - Day 21')

with open('./2023/Day21/input.ex') as file:
    lines = [line.rstrip() for line in file]

M=[]
for r,line in enumerate(lines):
    M.append(line)
    if 'S' in line:
        start=(r,line.find('S'))
    # print(line)
R = len(M)
C = len(M[0])

NEXT={start}

def wrap(r,c):
    if r>=R or r<0:
        r=r%R
    if c>=C or c<0:
        c=c%C
    return r,c

for _ in range(50):
    NEW=set()
    for r,c in NEXT:
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            rr,cc = r+dr,c+dc
            if M[r%R][c%C]!='#':
                NEW.add((rr,cc))

    NEXT=NEW

for r in range(-3*R,1*R):
    g=''
    for c in range(-1*C,2*C):
        if (r,c) in NEXT:
            g+='O'
        else:
            g+=M[r%R][c%C]
    print(g)

print('------------------------')
print('Part 1:',print(len(NEXT)))
print('------------------------')
print('Part 2:',0)
print('------------------------')