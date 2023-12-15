print('2023 - Day 15')

with open('./2023/Day15/input.txt') as file:
    lines = [line.rstrip() for line in file]


for line in lines:
    T=line.split(',')
    # print(line)

def f(value,char):
    value+=ord(char)
    value*=17
    value=value%256
    return value

def fs(s):
    value=0
    for char in s:
        value=f(value,char)
    return value


def run(inst):
    # print(inst)
    if '=' in inst:
        label,value = inst.split('=')
        i = fs(label)
        v = f'{label} {value}'
        found=False
        print('Adding',inst)
        print(i,B[i])
        for ib,item in enumerate(B[i]):
            if label in item:
                B[i][ib]=v
                found=True
                break
        if not found:
            B[i].append(v)
        print(i,B[i])
    elif '-' in inst:
        label,value = inst.split('-')
        i = fs(label)
        v = f'{label} {value}'
        for item in B[i]:
            if label in item:
                print('Removing',inst)
                print(i,B[i])
                B[i].remove(item)
                print(i,B[i])
                break
    else:
        assert False



ans1=0
for s in T:
    ans1+=fs(s)

B=[[] for _ in range(256)]
for inst in T: #'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'.split(','):
    run(inst)

ans2=0
for i,b in enumerate(B):
    print(i,b)
    for il,l in enumerate(b):
        p = (1+i)*(il+1)*int(l.split()[1])
        label,value = l.split()
        ans2+=p
        print(f"{l}: (box {i+1}) * {il+1} (slot) * {value} (focal length) = {p}, total={ans2}")

print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',ans2)
print('------------------------')

