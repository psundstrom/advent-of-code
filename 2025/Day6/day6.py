print('2025 - Day 6')

with open('./2025/Day6/input.txt') as file:
    lines = [line for line in file]

part1 = []

for i,line in enumerate(lines):
    if '*' not in line:
        part1.append(list(map(int, line.split())))
    else:
        part1.append(line.split())

p1 = 0
for i in range(len(part1[0])):
    if part1[-1][i] == '*':
        product = 1
        for j,line in enumerate(part1[:-1]):
            product *= line[i]
        p1 += product
    elif part1[-1][i] == '+':
        total=0
        for line in part1[:-1]:
            total += line[i]
        p1 += total
    else:
        assert False

p2 = 0
start = 0
for i in range(len(lines[0])):
    if i == len(lines[0])-1 or all([line[i] == ' ' for line in lines[:-1]]):
        end = i-1
        numbers = []
        for j in range(end,start-1,-1):
            s = ''
            for line in lines[:-1]:
                s += line[j]
            numbers.append(int(s.strip()))
        if lines[-1][start] == '+':
            p2 += sum(numbers)
        elif lines[-1][start] == '*':
            product = 1
            for n in numbers:
                product *= n
            p2 += product
        start=i+1

print('------------------------')
print('Part 1:', p1)
print('------------------------')
print('Part 2:', p2)
print('------------------------')