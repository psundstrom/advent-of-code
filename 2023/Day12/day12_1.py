print('2023 - Day 12')

with open('./2023/Day12/input.txt') as file:
    lines = [line.rstrip() for line in file]

S=[]
A=[]
for line in lines:
    springs,arr = line.split()
    S.append(springs)
    A.append([int(n) for n in arr.split(',')])

def ispossible(springs,j,g):
    if j+g<=len(springs) and (j==0 or springs[j-1] in ['.','?']) and (j+g==len(springs) or springs[j+g] in ['.','?']) and g==springs[j:j+g].count('#')+springs[j:j+g].count('?'):
        return True
    else:
        return False

def possibilities(springs,arr0,arr,j,b=set()):
    if len(arr)==0:
        if springs in b:
            return 0
        elif [k.count('#') for k in springs.replace('?','.').split('.') if k!='']==arr0:
            b.add(springs)
            return 1
        else:
            return 1
    arr_=arr.copy()
    g=arr_.pop(0)
    if j+g>len(springs)-1:
        return 0 # Not possible
    n=0
    i=j
    while i+g<=len(springs):
        if ispossible(springs,i,g):
            n+=possibilities(springs[0:i]+'#'*g+springs[i+g:],arr0,arr_,j+g,b)
        else:
            pass
        i+=1
    return n

starts=[]
for g in A[0]:
    starts.append([])
    for j in range(len(S[0])):
        if ispossible(S[0],j,g):
            starts[-1].append(j)

ans=0
for i in range(len(A)):
    b=set()
    possibilities(S[i],A[i],A[i],0,b)
    ans+=len(b)

print('------------------------')
print('Part 1:',ans)
print('------------------------')