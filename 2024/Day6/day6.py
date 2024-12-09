print("2024 - Day 6")

with open("./2024/Day6/input.txt") as file:
    lines = [line.rstrip() for line in file]

for r, line in enumerate(lines):
    for c, v in enumerate(line):
        if v == "^":
            start = (r, c)
            lines[r] = line.replace("^", ".")

print(start)

turn = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}

obst = (-1, -1)
n = 0
ans1 = None
for ir in range(len(lines)):
    for ic in range(len(lines[0])):
        SEEN = set()
        SEEN2 = set()
        d = (-1, 0)
        (r, c) = start
        SEEN.add(start)
        SEEN2.add((start, d))
        obst = (ir, ic)
        while 0 <= r < len(lines) and 0 <= c < len(lines[0]):
            rr = r + d[0]
            cc = c + d[1]
            if ((rr, cc), d) in SEEN2:
                n += 1
                break
            if not (0 <= rr < len(lines) and 0 <= cc < len(lines[0])):
                if not ans1:
                    ans1 = len(SEEN)
                break
            if lines[rr][cc] == "." and (rr, cc) != obst:
                r = rr
                c = cc
                SEEN.add((r, c))
            else:
                d = turn[d]
            SEEN2.add(((r, c), d))


def printmap():
    for r, line in enumerate(lines):
        toprint = ""
        for c, v in enumerate(line):
            if (r, c) in SEEN:
                toprint += "X"
            else:
                toprint += lines[r][c]
        print(toprint)

print("------------------------")
print("Part 1:", ans1)
print("------------------------")
print("Part 2:", n)
print("------------------------")