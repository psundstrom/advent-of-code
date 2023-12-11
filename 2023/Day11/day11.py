print('2023 - Day 11')

with open('./2023/Day11/input.txt') as file:
    lines = [line.rstrip() for line in file]

E = []
for i,line in enumerate(lines):
    if line.count('.')==len(line):
        E.append(i)
        # lines.insert(i,line)

for i in reversed(E):
    rep = '.'*len(lines[0])
    lines.insert(i,rep)

E=[]
for i,c in enumerate(lines[0]):
    col = ''.join([line[i] for line in lines])
    if col.count('.')==len(col):
        E.append(i)

for i in reversed(E):
    for j,line in enumerate(lines):
        lines [j] = line[:i]+'.'+line[i:]


G=[]
for x,line in enumerate(lines):
    for y,c in enumerate(line):
        if c=='#':
            G.append((x,y))

def dist(g1,g2):
    return abs(g1[0]-g2[0])+abs(g1[1]-g2[1])

D={}
for g1 in G:
    for g2 in G:
        if g1!=g2:
            if (g1,g2) in D.keys():
                D[(g1,g2)]=min(D[(g1,g2)],dist(g1,g2))
            elif (g2,g1) in D.keys():
                D[(g2,g1)]=min(D[(g2,g1)],dist(g2,g1))
            else:
                D[(g1,g2)]=dist(g1,g2)


print('------------------------')
print('Part 1:',sum(D.values()))
print('------------------------')
print('Part 2:',0)
print('------------------------')