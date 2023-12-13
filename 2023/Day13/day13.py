print('2023 - Day 13')

with open('./2023/Day13/input.txt') as file:
    lines = [line.rstrip() for line in file]

patterns=[]
patterns.append([])
for line in lines:
    if len(line)>0:
        patterns[-1].append(line)   
    else:
        patterns.append([])

def find_vertical(p):
    i=1
    found=False
    while not found and i<len(p[0]):
        for l in p:
            length=len(l[i:min(len(l),i+len(l[:i]))])
            s1=l[max(0,i-length):i]
            s2=l[i:min(len(l),i+len(l[:i]))]
            if s1==s2[::-1]:
                found=True
            else:
                found=False
                i+=1
                break
    if found and i<len(p[0]):
        return i
    else:
        return -1

def find_horizontal(p):
    i=1
    found=False
    while not found and i<len(p):
        for j,_ in enumerate(p[0]):
            l = ''.join([line[j] for line in p])
            length=len(l[i:min(len(l),i+len(l[:i]))])
            s1=l[max(0,i-length):i]
            s2=l[i:min(len(l),i+len(l[:i]))]
            if s1==s2[::-1]:
                found=True
            else:
                found=False
                i+=1
                break
    if found and i<len(p):
        return i
    else:
        return -1

def print_vertical(p,n):
    for l in p:
        print(l[:n],'|',l[n:])

def print_horizontal(p,n):
    for i,l in enumerate(p):
        if i==n:
            print('-'*len(l))
        print(l)

ans=0

nc = 0
for ip,p in enumerate(patterns):
    print(ip)

    for l in p:
        print(l)

    nv=find_vertical(p)
    nh=find_horizontal(p)

    if nv>-1:
        print(nv)
        print_vertical(p,nv)
        nc+=1
        ans+=nv
    elif nh>-1:
        print(nh)
        print_horizontal(p,nh)
        nc+=1
        ans+=100*nh

print('------------------------')
print('Part 1:',ans)
print('------------------------')
print('Part 2:',0)
print('------------------------')