print('2023 - Day 2')

with open('./2024/Day2/input.txt') as file:
    lines = [line.rstrip() for line in file]

reports=[]
for line in lines:
    reports.append([int(v) for v in line.split()])
    # print(line.split())

def checknumbers(n1,n2):
    return n2 > n1 and n2 - n1 < 4

def checklist(l):
    safe=True
    increasing=False
    if l[0]==l[1] or abs(l[0]-l[1])>3:
        safe = False
    elif l[1]>l[0]:
        increasing=True
    elif l[1]<l[0]:
        increasing=False
    else:
        assert False

    for i in range(1,len(l)):
        n1 = l[i-1]
        n2 = l[i]
        if n2==n1:
            safe = False
        elif abs(n2-n1)>3:
            safe = False
        elif n2>n1 and not increasing:
            safe = False
        elif n2<n1 and increasing:
            safe = False
    return safe

# def checklist(l, part2=False):
#     safe=True
#     safe2=True
#     for i in range(1,len(l)):
#         if not checknumbers(l[i-1], l[i]):
#             if not safe:
#                 safe2=False
#             safe=False
#     if part2:
#         return safe2
#     return safe

n2 = 0
for r in reports:
    if checklist(r):
        n2+=1
    else:
        for i in range(len(r)):
            if checklist(r[:i] + r[i+1:]):
                n2+=1
                break

print('------------------------')
print('Part 1:', sum([checklist(r) for r in reports]))
print('------------------------')
print('Part 2:', n2)
print('------------------------')