print('2025 - Day 1')

with open('./2025/Day1/input.txt') as file:
    lines = [line.rstrip() for line in file]

s = {'L': -1, 'R': 1}

value = 50

p1 = 0
p2 = 0

def zerocrossing(v, n):
    r = 0
    # If we're not at zero
    #  And we get to zero
    #  OR
    #  We cross zero with the move % 100
    #  -> add 1
    if n != 0 and ((v + n) % 100 == 0 or (v != 0 and ((-99 < v + (n//abs(n)*(abs(n) % 100)) < 0) or (99 < v + ((n//abs(n))*(abs(n) % 100)) < 199)))):
        r = 1
    # Add all complete rotations
    return r + abs(n) // 100

for line in lines:
    sign = line[0]
    inc = int(line[1:])
    p2 += zerocrossing(value, s[sign] * inc, True)
    value = value + s[sign] * inc
    value = value % 100
    if value == 0:
        p1+=1

print('------------------------')
print('Part 1:',p1)
print('------------------------')
print('Part 2:',p2)
print('------------------------')