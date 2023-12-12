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

# for i in range(len(S)):
#     springs=S[i]
#     arr=A[i]
#     starts=[]
#     for ia,g in enumerate(arr):
#         print(arr)
#         for j in range(len(springs)):
#             print(springs,arr,j,g,ispossible(springs,j,g))

def possibilities(springs,arr0,arr,j,b=set()):
    if len(arr)==0:
        # print('end:',springs)
        if springs in b:
            return 0
        elif [k.count('#') for k in springs.replace('?','.').split('.') if k!='']==arr0:
            b.add(springs)
            return 1
        else:
            return 1
    arr_=arr.copy()
    g=arr_.pop(0)
    # print(arr,arr_,g)
    if j+g>len(springs)-1:
        return 0 # Not possible
    n=0
    i=j
    while i+g<=len(springs):
        if ispossible(springs,i,g):
            # print(arr,arr_,g)
            # print(springs,i,g,springs[i:i+g],'Possible')
            # print('Before:',springs)
            # print('After:',springs[0:i]+'#'*g+springs[i+g:])

            n+=possibilities(springs[0:i]+'#'*g+springs[i+g:],arr0,arr_,j+g,b)
        else:
            pass
            # print(springs,i,g,springs[i:i+g],'Not Possible')
        i+=1
    return n
        
# print(S[0])
# print(A[0])
starts=[]
for g in A[0]:
    # print('g:',g)
    starts.append([])
    for j in range(len(S[0])):
        if ispossible(S[0],j,g):
            starts[-1].append(j)
        # print(S[0],j,g,S[0][i:i+g],ispossible(S[0],j,g))
# print(starts)

# print(ispossible(S[0],0,A[0][0]))

ans=0
for i in range(len(A)):
    b=set() 
    # print(S[i],A[i])
    possibilities(S[i],A[i],A[i],0,b)
    ans+=len(b)
    # print(S[i],A[i],len(b))

print('------------------------')
print('Part 1:',ans)
print('------------------------')
print('Part 2:',0)
print('------------------------')