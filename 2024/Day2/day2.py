print('2023 - Day 2')

with open('./2024/Day2/input.txt') as file:
    lines = [line.rstrip() for line in file]

reports=[]
for line in lines:
    reports.append([int(v) for v in line.split()])
    # print(line.split())

def checknumbers(n1,n2):
    return n2 > n1 and n2 - n1 < 4


def checklist(l, part2=False):
    safe=True
    safe2=True
    for i in range(1,len(l)):
        if not checknumbers(l[i-1], l[i]):
            if not safe:
                safe2=False
            safe=False
    if part2:
        return safe2
    return safe

for r in reports:
    print(r)
    print(checklist(r))

print('------------------------')
print('Part 1:', sum([checklist(r) or checklist(r[-1::-1]) for r in reports]))
print('------------------------')
print('Part 2:', sum([checklist(r, part2=True) or checklist(r[-1::-1], part2=True) for r in reports]))
print('------------------------')