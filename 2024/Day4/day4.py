print('2024 - Day 4')

with open('./2024/Day4/input.txt') as file:
    lines = [line.rstrip() for line in file]
n1=0
for ll,line in enumerate(lines):
    rev = line[::-1]
    for i in range(len(line)):
        # Right
        if line[i:i+4]=='XMAS':
            n1+=1
        # Left
        if rev[i:i+4]=='XMAS':
            n1+=1
        # Down
        if ll+3<len(lines) and lines[ll][i]+lines[ll+1][i]+lines[ll+2][i]+lines[ll+3][i]=='XMAS':
            n1+=1
        # Up
        if ll>=3 and lines[ll][i]+lines[ll-1][i]+lines[ll-2][i]+lines[ll-3][i]=='XMAS':
            n1+=1
        # Down-Right
        if ll+3<len(lines) and i+3<len(line) and lines[ll][i]+lines[ll+1][i+1]+lines[ll+2][i+2]+lines[ll+3][i+3]=='XMAS':
            n1+=1
        # Up-Right
        if ll>=3 and i+3<len(line) and lines[ll][i]+lines[ll-1][i+1]+lines[ll-2][i+2]+lines[ll-3][i+3]=='XMAS':
            n1+=1
        # Down-Left
        if ll+3<len(lines) and i-3>=0 and lines[ll][i]+lines[ll+1][i-1]+lines[ll+2][i-2]+lines[ll+3][i-3]=='XMAS':
            n1+=1
        # Up-Left
        if ll>=3 and i-3>=0 and lines[ll][i]+lines[ll-1][i-1]+lines[ll-2][i-2]+lines[ll-3][i-3]=='XMAS':
            n1+=1

def checkpoint(r,c):
    if r>0 and c>0 and r+1<len(lines) and c+1<len(lines[0]):
        s1 = lines[r-1][c-1]+lines[r][c]+lines[r+1][c+1]
        s2 = lines[r+1][c-1]+lines[r][c]+lines[r-1][c+1]
        if (s1=='MAS' or s1[::-1]=='MAS') and (s2=='MAS' or s2[::-1]=='MAS'):
            return True
    return False

n2=0
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if checkpoint(r,c):
            n2+=1

print('------------------------')
print('Part 1:',n1)
print('------------------------')
print('Part 2:',n2)
print('------------------------')