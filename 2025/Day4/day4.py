print('2025 - Day 4')

with open('./2025/Day4/input.txt') as file:
    lines = [line.rstrip() for line in file]

lines = [list(line) for line in lines]

p1=0
def get_available():
    available = []
    for r, line in enumerate(lines):
        for c, k in enumerate(line):
            adj = 0
            if lines[r][c]!='@':
                continue
            for dr, dc in [(-1,0),(-1, -1),(0, -1),(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]:
                rr = r + dr
                cc = c + dc
                if 0<=rr<len(lines) and 0<=cc<len(line):
                    if lines[rr][cc]=='@':
                        adj+=1
            if adj<4:
                available.append((r,c))
    return available

available = get_available()
p1 = len(available)
p2 = p1
while len(available)>0:
    for r,c in available:
        lines[r][c]='.'
    available = get_available()
    p2 += len(available)

print('------------------------')
print('Part 1:',p1)
print('------------------------')
print('Part 2:',p2)
print('------------------------')