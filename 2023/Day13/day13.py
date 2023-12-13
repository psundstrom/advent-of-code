print('2023 - Day 13')

with open('./2023/Day13/input.ex') as file:
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

def flip(p,x,y):
    if p[x][y]=='#':
        p[x] = p[x][:y]+'.'+p[x][y+1:]
    else:
        p[x] = p[x][:y]+'#'+p[x][y+1:]
    return p

ans=0

nc=0
nn=0
for ip,p in enumerate(patterns):
    nx=len(p)
    ny=len(p[0])
    nn+=nx*ny

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

ans=0
for ip,p in enumerate(patterns):
    for l in p:
        print(l)

    nv=find_vertical(p)
    nh=find_horizontal(p)

    br=False
    for x in range(len(p)):
        for y in range(len(p[0])):
            p_ = flip(p,x,y)
            nv_=find_vertical(p_)
            nh_=find_horizontal(p_)

            if nv_!=nv or nh_!=nh:
                br=True
                print('br',nv_,nh_,x,y)
                if nv_!=nv:
                    nv=nv_
                    nh=-1
                elif nh_!=nh:
                    nh=nh_
                    nv=-1
                break
        if br:
            break

    if nv>-1:
        print('v:',nv)
        print_vertical(p_,nv)
        nc+=1
        ans+=nv
    elif nh>-1:
        print('h:',nh)
        print_horizontal(p,nh_)
        nc+=1
        ans+=100*nh

print('Part 2:',ans)
print('------------------------')