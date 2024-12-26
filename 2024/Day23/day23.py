print('2024 - Day 23')

from collections import defaultdict

with open('./2024/Day23/input.txt') as file:
    lines = [line.rstrip() for line in file]

C = defaultdict(list)

for line in lines:
    c1,c2 = line.split('-')
    if c2 not in C[c1]:
        C[c1].append(c2)
    if c1 not in C[c2]:
        C[c2].append(c1)

CT = set()
for c1 in C.keys():
    for c2 in C[c1]:
        for c3 in C[c2]:
            if c3 in C[c1]:
                if c1[0]=='t' or c2[0]=='t' or c3[0]=='t':
                    CT.add(tuple(sorted([c1,c2,c3])))

def findparty(c):
    if len(c)==1:
        for con in C[c[0]]:
            return findparty(c+[con])
    s = C[c[0]]
    first=True
    for item in c:
        s = [x for x in s if x in C[item]]
    if len(s)==0:
        return c
    return findparty(s+c)

def check(connected):
    good=True
    for c in connected:
        if not all([c in C[k] for k in connected if k!=c]):
            good = False
    return good

lens = []
maxlen = -1
CON = []
for computer in C.keys():
    connected = findparty([computer])
    CON.append(connected)
    if check(connected) and len(connected)>maxlen:
        maxlen = len(connected)
        maxc = connected

print(len(connected))
print('------------------------')
print('Part 1:',len(CT))
print('------------------------')
print('Part 2:',','.join(sorted(list(maxc))))
print('------------------------')