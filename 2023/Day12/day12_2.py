print('2023 - Day 12')
import functools

with open('./2023/Day12/input.txt') as file:
    lines = [line.rstrip() for line in file]

S=[]
A=[]
for line in lines:
    springs,arr = line.split()
    S.append(springs)
    A.append(tuple([int(n) for n in arr.split(',')]))

@functools.cache
def solve(springs,arr):
    if len(arr)==0:
        if '#' in springs:
            return 0
        else:
            return 1
        
    if len(springs)<sum(arr)+len(arr)-1:
        return 0
    
    if len(springs)<arr[0]:
        return 0

    if springs[0]=='#':
        n=pound(springs,arr)
    elif springs[0]=='.':
        n=dot(springs,arr)
    elif springs[0]=='?':
        n=pound(springs,arr)+dot(springs,arr)
    else:
        assert False
    return n

@functools.cache
def pound(springs,arr):
    n=arr[0]
    subst = springs[:n]
    subst=subst.replace('?','#')
    if subst.count('#')!=n:
        return 0
    if len(subst)==len(springs):
        return 1
    if len(arr)==1 and springs[n:].count('#')==0:
        return 1
    if springs[n] in ['?','.']:
        return solve(springs[n+1:],arr[1:])
    return 0

@functools.cache
def dot(springs,arr):
    return solve(springs[1:],arr)

ans1=0
for springs,arr in zip(S,A):
    n = solve(springs,arr)
    ans1+=n

ans2=0
for springs,arr in zip(S,A):
    n = solve('?'.join([springs for _ in range(5)]),arr*5)
    ans2+=n

print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',ans2)
print('------------------------')