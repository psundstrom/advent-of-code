print('2025 - Day 5')

with open('./2025/Day5/input.txt') as file:
    lines = [line.rstrip() for line in file]

ranges = []
ingredients = []

blank = False
for line in lines:
    if line == '':
        blank = True
        continue
    if blank:
        ingredients.append(int(line))
    else:
        ranges.append(tuple(map(int, line.split('-'))))

ranges.sort()

i = 0
while i < len(ranges) - 1:
    range1 = ranges[i]
    range2 = ranges[i+1]
    if range2[0] > range1[1]:
        i+=1
    else:
        ranges[i] = (range1[0], max(range2[1], range1[1]))
        ranges.pop(i+1)
        i=0

fresh = []
for i in ingredients:
    isfresh = False
    for r in ranges:
        if r[0] <= i <= r[1]:
            isfresh = True
            break
    if isfresh:
        fresh.append(i)

print('------------------------')
print('Part 1:',len(fresh))
print('------------------------')
print('Part 2:',sum([f[1] - f[0] + 1 for f in ranges]))
print('------------------------')