print('2024 - Day 1')

with open('./2024/Day1/input.txt') as file:
    lines = [line.rstrip() for line in file]

LEFT=[]
RIGHT=[]

for line in lines:
    parts = line.split()
    LEFT.append(int(parts[0]))
    RIGHT.append(int(parts[1]))

LEFT.sort()
RIGHT.sort()

DIFFS = [abs(l-r) for l,r in zip(LEFT,RIGHT)]

ans2=0
for item in LEFT:
    ans2+=item*RIGHT.count(item)

print('------------------------')
print('Part 1:',sum(DIFFS))
print('------------------------')
print('Part 2:',ans2)
print('------------------------')