print('2024 - Day 3')

import re


with open('./2024/Day3/input.txt') as file:
    lines = [line.rstrip() for line in file]

ans=0
for line in lines:
    for match in re.findall('mul\(\d+,\d+\)',line):
        n1,n2 = [int(v) for v in match[4:-1].split(',')]
        ans+=n1*n2
        print(n1,n2)

print(ans)

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')