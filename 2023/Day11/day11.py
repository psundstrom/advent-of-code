print('2023 - Day 11')

with open('./2023/Day11/input.txt') as file:
    lines = [line.rstrip() for line in file]

ER = []
for i,line in enumerate(lines):
    if line.count('.')==len(line):
        ER.append(i)

EC=[]
for i,c in enumerate(lines[0]):
    col = ''.join([line[i] for line in lines])
    if col.count('.')==len(col):
        EC.append(i)

G=[]
for x,line in enumerate(lines):
    for y,c in enumerate(line):
        if c=='#':
            G.append((x,y))

def dist(g1,g2,ext):
    r1 = min(g1[0],g2[0])
    r2 = max(g1[0],g2[0])
    c1 = min(g1[1],g2[1])
    c2 = max(g1[1],g2[1])
    
    nr = len([r for r in ER if r1<r<r2])
    nc = len([c for c in EC if c1<c<c2])
    return abs(r2-r1)+abs(c2-c1)+nr*ext+nc*ext

D={}
ext=1
for g1 in G:
    for g2 in G:
        if g1!=g2:
            if (g1,g2) in D.keys():
                D[(g1,g2)]=min(D[(g1,g2)],dist(g1,g2,ext))
            elif (g2,g1) in D.keys():
                D[(g2,g1)]=min(D[(g2,g1)],dist(g2,g1,ext))
            else:
                D[(g1,g2)]=dist(g1,g2,ext)
D2={}
ext=999999
for g1 in G:
    for g2 in G:
        if g1!=g2:
            if (g1,g2) in D2.keys():
                D2[(g1,g2)]=min(D2[(g1,g2)],dist(g1,g2,ext))
            elif (g2,g1) in D2.keys():
                D2[(g2,g1)]=min(D2[(g2,g1)],dist(g2,g1,ext))
            else:
                D2[(g1,g2)]=dist(g1,g2,ext)


print('------------------------')
print('Part 1:',sum(D.values()))
print('------------------------')
print('Part 2:',sum(D2.values()))
print('------------------------')