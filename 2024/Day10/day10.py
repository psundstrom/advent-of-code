print('2024 - Day 10')

from collections import deque

with open('./2024/Day10/input.txt') as file:
    grid = [[int(c) if c.isnumeric() else -1 for c in line.rstrip()] for line in file]

R = len(grid)
C = len(grid[0])

starts=[]

for r,row in enumerate(grid):
    for c, val in enumerate(row):
        if val==0:
            starts.append((r,c))

SEEN=set()
def findpaths1(r,c):
    if grid[r][c]==9 and (r,c) not in SEEN:
        SEEN.add((r,c))
        return 1
    dirs = [(dr,dc) for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)] if 0 <= r+dr < R and 0 <= c+dc < C and grid[r+dr][c+dc]==grid[r][c]+1]
    if len(dirs)==0:
        return 0
    return sum([findpaths1(r+dr,c+dc) for dr,dc in dirs])

def findpaths2(r,c):
    if grid[r][c]==9:
        return 1
    dirs = [(dr,dc) for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)] if 0 <= r+dr < R and 0 <= c+dc < C and grid[r+dr][c+dc]==grid[r][c]+1]
    if len(dirs)==0:
        return 0
    return sum([findpaths2(r+dr,c+dc) for dr,dc in dirs])

total1=0
for start in starts:
    SEEN = set()
    score = findpaths1(*start)
    total1+=score

total2=0
for start in starts:
    score = findpaths2(*start)
    total2+=score

print('------------------------')
print('Part 1:',total1)
print('------------------------')
print('Part 2:',total2)
print('------------------------')