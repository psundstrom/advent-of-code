print('2023 - Day 12')

with open('./2023/Day12/input.txt') as file:
    lines = [line.rstrip() for line in file]

S=[]
A=[]
for line in lines:
    springs,arr = line.split()
    S.append(springs)
    A.append([int(n) for n in arr.split(',')])

def getlocked(springs,n,istart):
    locked=[]
    for i,c in enumerate(springs):
        if i+n<=len(springs):
            # print(springs[max(0,i-1):min(i+n+1,len(springs))])
            if springs[i:i+n]=='#'*n and (i+n==len(springs) or springs[i+n] in ['.','?']) and (i==0 or springs[i-1] in ['.','?']):
                # print(springs[max(0,i-1):min(len(springs),i+n+1)],'#'*n,springs[i+n+1],springs[i+n] in ['.','?'])
                if i>=istart:
                    locked.append(i)
                # print('group',i,springs[max(0,i-1):min(i+n+1,len(springs))])
    return locked

def getpossible(springs,n):
    p = []
    for i,c in enumerate(springs):
        if i+n<=len(springs):
            if all([k in ['#','?'] for k in springs[i:i+n]]) and (i==0 or springs[i-1] in ['.','?']) and (i+n==len(springs) or springs[i+n] in ['.','?']):
                p.append(i)
    return p

def replace(springs,n,ic):
    # Insert n*'#' starting at ic, pad with '.'
    if ic==0:
        ir1=0
        s1=''
    else:
        ir1=ic-1
        s1='.'
    if ic+n==len(springs):
        ir2=len(springs)
        s2=''
    else:
        ir2=ic+n+1
        s2='.'
    return springs[:ir1]+s1+'#'*n+s2+springs[ir2:]

def solve(springs,istart,arr):
    # print(springs,'---')
    a=arr.copy()
    n=a.pop(0)
    offset=0 if istart>0 else 0
    IL = getlocked(springs,n,istart)
    I = [istart+ip+offset for ip in getpossible(springs[istart+offset:],n)]
    if len(IL)==1 and IL[0] in I:
        # print(a,n)
        # print(IL[0]+istart,I,istart)
        # print('>',springs,istart+IL[0],n)
        I=IL
    if len(I)==0:
        return 0
    elif len(a)==0:
        return len(I)
    else:
        return sum([solve(replace(springs,n,ic),ic+n,a) for ic in I])

# start at i=0
# if arr is empty:
#   return 1?
# pop one n from arr
# if no possible positions
#   return 0
# for all possible positions of n:
# replace string with .#*#., pass remaining string recursively with the rest of n
ans=0
for i in range(len(S)):
    springs=S[i]
    arr=A[i]
    # print(springs,arr,solve(springs,0,arr))
    ans+=solve(springs,0,arr)
# print('          0123')
# print('01234567891111')
# print(springs)
# print(getlocked(springs,3))

print('------------------------')
print('Part 1:',ans)
print('------------------------')
print('Part 2:',0)
print('------------------------')