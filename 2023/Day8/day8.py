print('2023 - Day 8')

import math

with open('./2023/Day8/input.txt') as file:
    lines = [line.rstrip() for line in file]

M = {}
D = lines.pop(0)
lines.pop(0)
for line in lines:

    parts = line.split('=')
    n = parts[0]
    k = parts[1].strip().split()
    M[parts[0].strip()]=[k[0][1:-1],k[1][:-1]]

L = 'AAA'
i=0

while L != 'ZZZ':
    d = D[i%len(D)]
    im = {'L':0, 'R':1}[d]
    # print(i,d,im,L,M[L])
    L = M[L][im]
    i+=1

print('------------------------')
print('Part 1:',i)
print('------------------------')

starts = [a for a in M.keys() if a[2]=='A']

N = [0]*len(starts)
for ni,L in enumerate(starts):
    i=0
    while L[2]!='Z':
        d = D[i%len(D)]
        im = {'L':0, 'R':1}[d]
        # print(i,d,im,L,M[L])
        L = M[L][im]
        i+=1
    ir = i
    N[ni]=i

print('Part 2:',math.lcm(*N))
print('------------------------')