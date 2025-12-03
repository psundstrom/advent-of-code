print('2025 - Day 3')

from functools import cache

with open('./2025/Day3/input.txt') as file:
    lines = [line.rstrip() for line in file]

@cache
def get_largest(line,n):
    if n==1:
        return str(max([int(l) for l in line]))
    if n==len(line):
        return line
    if n>len(line):
        assert False
    m=-1
    for i in range(len(line)+1-n):
        m_ = line[i] + get_largest(line[i+1:],n-1)
        if int(m_)>int(m):
            m=m_
    return m

p1 = 0
p2 = 0
for i, line in enumerate(lines):
    p1 += int(get_largest(line, 2))
    p2 += int(get_largest(line, 12))

print('------------------------')
print('Part 1:', p1)
print('------------------------')
print('Part 2:', p2)
print('------------------------')