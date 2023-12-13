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

def find_vertical(p,skip=-1):
    i=1
    found=False
    while not found and i<len(p[0]):
        if i==skip:
            i+=1
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

def find_horizontal(p,skip=-1):
    i=1
    found=False
    while not found and i<len(p):
        if i==skip:
            i+=1
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

def flip(p,x,y):
    p_=p.copy()
    if p_[x][y]=='#':
        p_[x] = p_[x][:y]+'.'+p_[x][y+1:]
    else:
        p_[x] = p_[x][:y]+'#'+p_[x][y+1:]
    return p_

ans=0
for ip,p in enumerate(patterns):
    nv=find_vertical(p)
    nh=find_horizontal(p)
    if nv>-1:
        ans+=nv
    elif nh>-1:
        ans+=100*nh

print('------------------------')
print('Part 1:',ans)
print('------------------------')

ans=0
for ip,p in enumerate(patterns):
    nv=find_vertical(p)
    nh=find_horizontal(p)
    br=False
    for x in range(len(p)):
        for y in range(len(p[0])):
            p_ = flip(p,x,y)
            nv_=find_vertical(p_,nv)
            nh_=find_horizontal(p_,nh)
            if nv_>-1 or nh_>-1:
                br=True
                break
        if br:
            break
    if nv_>-1:
        ans+=nv_
    elif nh_>-1:
        ans+=100*nh_

print('Part 2:',ans)
print('------------------------')