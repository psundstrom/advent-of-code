print("2025 - Day 9")
from functools import cache

with open("./2025/Day9/input.txt") as file:
    points = [tuple(map(int, line.rstrip().split(","))) for line in file]

allpoints = set()

rmax = max([p[0] for p in points])+10
cmax = max([p[1] for p in points])+10

for i, p1 in enumerate(points):
    p2 = points[(i + 1) % len(points)]
    dr = (p2[0] - p1[0]) // max(1, abs(p2[0] - p1[0]))
    dc = (p2[1] - p1[1]) // max(1, abs(p2[1] - p1[1]))
    p = p1
    while p != p2:
        p = (p[0] + dr, p[1] + dc)
        allpoints.add(p)


@cache
def is_intersection(p1, p2):
    return (p1 in allpoints) != (p2 in allpoints)

@cache
def is_inside(p):
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        r,c = p
        check = False
        while 0<=r<rmax and 0<=c<cmax:
            if (r,c) in allpoints:
                check = True
                break
            r+=dr
            c+=dc
            if r==rmax or c==cmax:
                return False
        if check==False:
            return False
    return True        


@cache
def getarea(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

@cache
def intersects(p1, p2, p3, p4):
    if p1 == (6,5) and p2==(6,2):
        pass
    if p1 == p2:
        return False
    if p1[0] == p2[0]:
        if p3[0]==p4[0]:
            # Both are horizontal, no intersection
            return False
        if (((p3[0]>p1[0]) and (p4[0]<p1[0])) or ((p3[0]<p1[0]) and (p4[0]>p1[0]))) and min(p1[1],p2[1])<p3[1]<max(p1[1],p2[1]):
            return True
        return False
    if p1[1]==p2[1]:
        if p3[1]==p4[1]:
            # Both are vertical, no intersection
            return False
        if (((p3[1]>p1[1]) and (p4[1]<p1[1])) or ((p3[1]<p1[1]) and (p4[1]>p1[1]))) and min(p1[0],p2[0])<p3[0]<max(p1[0],p2[0]):
            return True
        return False
    assert False

@cache
def p2rect(p1, p2):
    r1 = (min(p1[0], p2[0]), min(p1[1], p2[1]))
    r2 = (min(p1[0], p2[0]), max(p1[1], p2[1]))
    r3 = (max(p1[0], p2[0]), max(p1[1], p2[1]))
    r4 = (max(p1[0], p2[0]), min(p1[1], p2[1]))
    return (r1, r2, r3, r4)


def rectpoints(rect):
    rp = set()
    for i, p1 in enumerate(rect):
        p2 = rect[(i + 1) % len(rect)]
        dr = (p2[0] - p1[0]) // max(1, abs(p2[0] - p1[0]))
        dc = (p2[1] - p1[1]) // max(1, abs(p2[1] - p1[1]))
        p = p1
        while p != p2:
            p = (p[0] + dr, p[1] + dc)
            rp.add(p)
    return rp

@cache
def line(p, p1, p2):
    # p1 - p2 along the order of the polygon - left side is inside
    # check if point p is on the inside side of the line
    # determine direction
    dr = (p2[0]-p1[0])//max(1,abs(p2[0]-p1[0]))
    dc = (p2[1]-p1[1])//max(1,abs(p2[1]-p1[1]))

    if p in allpoints:
        return True

    # Return True if point is more than 1 point from given line, can't determine status
    if dr == 0 and (abs(p[0]-p1[0])>1 or not min(p1[1],p2[1]) <= p[1] <= max(p1[1],p2[1])):
        return True
    if dc == 0 and (abs(p[1]-p1[1])>1 or not min(p1[0],p2[0]) <= p[0] <= max(p1[0],p2[0])):
        return True

    if dr>0:
        if p1[0]<=p[0]<=p2[0] and p[1]>p1[1]:
            return True
        elif p in allpoints:
            return True
        else:
            return False
    elif dr<0:
        if p2[0]<=p[0]<=p1[0] and p[1]<p1[1]:
            return True
        elif p in allpoints:
            return True
        else:
            return False
    elif dc>0:
        if p1[1]<=p[1]<=p2[1] and p[0]<p1[0]:
            return True
        elif p in allpoints:
            return True
        else:
            return False
    elif dc<0:
        if p2[1]<=p[1]<=p1[1] and p[0]>p1[0]:
            return True
        elif p in allpoints:
            return True
        else:
            return False
    else:
        assert False

@cache
def inside_rectangle(rect, p):
    return min([r[0] for r in rect]) < p[0] < max([r[0] for r in rect]) and min(
        [r[1] for r in rect]
    ) < p[1] < max([r[1] for r in rect])

@cache
def check_rectangle(p1, p2):
    rect = p2rect(p1, p2)

    for p in rect:
        if not is_inside(p): return False
    for i, pt1 in enumerate(rect):
        pt2 = rect[(i+1)%len(rect)]

        dr = (pt2[0]-pt1[0])//max(1,abs(pt2[0]-pt1[0]))
        dc = (pt2[1]-pt1[1])//max(1,abs(pt2[1]-pt1[1]))

        for p in [(pt1[0]+dr, pt1[1]+dc),(pt2[0]-dr, pt2[1]-dc)]:
            for j, pp1 in enumerate(points):
                pp2 = points[(j+1) % len(points)]
                if not line(p,pp1,pp2):
                    return False
    for i, rp1 in enumerate(rect):
        rp2 = rect[(i + 1) % len(rect)]
        for j, pp1 in enumerate(points):
            pp2 = points[(j+1) % len(points)]
            if intersects(rp1,rp2,pp1,pp2):
                return False
    
    return True

part1 = 0
part2 = 0
rectangles = []
for i, p1 in enumerate(points):
    for j, p2 in enumerate(points):
        if True:
            area = getarea(p1, p2)
            rectangles.append((area, p1, p2))
            if area > part1:
                part1 = area

print("------------------------")
print("Part 1:", part1)
print("------------------------")

for area, p1, p2 in sorted(rectangles, reverse=True):
    if check_rectangle(p1, p2):
        part2 = area
        part2p1 = p1
        part2p2 = p2
        print(area)
        break


print("Part 2:", part2)
print("------------------------")
