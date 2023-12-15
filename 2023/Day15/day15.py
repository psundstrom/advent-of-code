print('2023 - Day 15')

with open('./2023/Day15/input.txt') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    T=line.split(',')

def fs(s):
    value=0
    for char in s:
        value=(value+ord(char))*17%256
    return value

def run(inst):
    if '=' in inst:
        label,value = inst.split('=')
        i = fs(label)
        v = f'{label} {value}'
        found=False
        for ib,item in enumerate(B[i]):
            if label==item.split()[0]:
                B[i][ib]=v
                found=True
                break
        if not found:
            B[i].append(v)
    elif '-' in inst:
        label,value = inst.split('-')
        i = fs(label)
        v = f'{label} {value}'
        for item in B[i]:
            if label==item.split()[0]:
                B[i].remove(item)
                break
    else:
        assert False

ans1=0
for s in T:
    ans1+=fs(s)

B=[[] for _ in range(256)]
for inst in T:
    run(inst)

ans2=0
for i,b in enumerate(B):
    for il,l in enumerate(b):
        p = (1+i)*(il+1)*int(l.split()[1])
        label,value = l.split()
        ans2+=p

print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',ans2)
print('------------------------')

