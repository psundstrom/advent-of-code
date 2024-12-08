print('2024 - Day 7')

from itertools import combinations,combinations_with_replacement,permutations

with open('./2024/Day7/input.txt') as file:
    lines = [line.rstrip() for line in file]

def check1(v,result,values):
    if len(values)==0:
        return v==result
    k = values.pop(0)
    return check1(v*k,result,values.copy()) or check1(v+k,result,values.copy())

def check2(v,result,values):
    if len(values)==0:
        return v==result
    k = values.pop(0)
    return check2(v*k,result,values.copy()) or check2(v+k,result,values.copy()) or check2(int(str(v)+str(k)),result,values.copy())

ans1=0
ans2=0
for line in lines:
    result,rest = line.split(':')
    result=int(result)
    values = [int(v) for v in rest.split()]
    v = values.pop(0)
    if check1(v,result,values.copy()):
        ans1+=result
    if check2(v,result,values.copy()):
        ans2+=result

print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',ans2)
print('------------------------')