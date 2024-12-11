print('2024 - Day 11')

import functools

with open('./2024/Day11/input.txt') as file:
    lines = [line.rstrip() for line in file]

stones=[int(v) for v in lines[0].split()]

@functools.cache
def blinkstone(n):
    if n==0:
        return (1,)
    elif len(str(n))%2==0:
        st = str(n)
        n1 = int(st[:len(st)//2])
        n2 = int(st[len(st)//2:])
        return (n1,n2)
    else:
        return (n*2024,)

@functools.cache
def blink(stone,n):
    if n==0:
        return 1
    # stone - number on stone
    # n - how many times to blink
    newstones = blinkstone(stone)
    return sum([blink(s,n-1) for s in newstones])

print('------------------------')
print('Part 1:',sum([blink(s,25) for s in stones]))
print('------------------------')
print('Part 2:',sum([blink(s,75) for s in stones]))
print('------------------------')