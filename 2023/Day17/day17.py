print('2023 - Day 17')

from heapq import heappush, heappop

def green(str):
    return f"\033[92m{str}\033[00m"
def red(str):
    return f"\033[91m{str}\033[00m"
def yellow(str):
    return f"\u001b[33m{str}\033[00m"

with open('./2023/Day17/input.txt') as file:
    M = [[int(n) for n in line.rstrip()] for line in file]

R=len(M)
C=len(M[0])

SEEN=set()
Q = []
# PREV = {}

Q.append((0, 0, 0, 0, 0, 0))

while Q:
    hl, r, c, dr, dc, n = heappop(Q)
    
    if r==R-1 and c==C-1:
        break

    if (r,c,dr,dc,n) in SEEN:
        continue
    
    SEEN.add((r,c,dr,dc,n))
    
    # if r<0 or r>=R or c<0 or c>=C:
    #     continue

    if n<3 and (dr,dc) != (0,0):
        nr = r + dr
        nc = c + dc
        if 0<=nr<R and 0<=nc<C:
            heappush(Q,(hl + M[nr][nc], nr, nc, dr, dc, n+1))
    for ndr, ndc in [(0,1),(1,0),(0,-1),(-1,0)]:
        if (ndr,ndc) != (dr,dc) and (ndr,ndc) != (-dr,-dc):
            nr = r+ndr
            nc = c+ndc
            if 0<=nr<R and 0<=nc<C:
                heappush(Q,(hl + M[nr][nc],nr,nc,ndr,ndc,1))

print('------------------------')
print('Part 1:',hl)
print('------------------------')

SEEN=set()
Q = []
# PREV = {}

Q.append((0, 0, 0, 0, 0, 0))

while Q:
    hl, r, c, dr, dc, n = heappop(Q)
    
    if r==R-1 and c==C-1 and n>=4:
        break

    if (r,c,dr,dc,n) in SEEN:
        continue
    
    SEEN.add((r,c,dr,dc,n))
    
    # if r<0 or r>=R or c<0 or c>=C:
    #     continue

    if n<10 and (dr,dc) != (0,0):
        nr = r + dr
        nc = c + dc
        if 0<=nr<R and 0<=nc<C:
            heappush(Q,(hl + M[nr][nc], nr, nc, dr, dc, n+1))
    if n>=4 or (dr,dc)==(0,0):
        for ndr, ndc in [(0,1),(1,0),(0,-1),(-1,0)]:
            if (ndr,ndc) != (dr,dc) and (ndr,ndc) != (-dr,-dc):
                nr = r+ndr
                nc = c+ndc
                if 0<=nr<R and 0<=nc<C:
                    heappush(Q,(hl + M[nr][nc],nr,nc,ndr,ndc,1))

print('Part 2:',hl)
print('------------------------')