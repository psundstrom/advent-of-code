print('2024 - Day 3')

import re

with open('./2024/Day3/input.txt') as file:
    lines = [line.rstrip() for line in file]

ans1=0
for line in lines:
    for match in re.findall(r'mul\([0-9]+,[0-9]+\)',line):
        n1,n2 = [int(v) for v in match[4:-1].split(',')]
        ans1+=n1*n2

tokens=[]
dont=[]
do=True
for line in lines:
    for match in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)",line):
        if match=='do()':
            do=True
        elif match=="don't()":
            do=False
        else:
            if do:
                tokens.append(match)
            else:
                dont.append(match)

ans2=0
for s in tokens:
    n1,n2 = [int(v) for v in s[4:-1].split(',')]
    ans2+=n1*n2

print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',ans2)
print('------------------------')