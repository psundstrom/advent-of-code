print('2023 - Day 6')

with open('./2023/Day6/input.txt') as file:
    lines = [line.rstrip() for line in file]

times = [int(n) for n in lines[0].split(':')[1].split()]
distances = [int(n) for n in lines[1].split(':')[1].split()]
beats = [0]*len(times)

for i,(t,d) in enumerate(zip(times,distances)):
    for v in range(t):
        nd=v*(t-v)
        if nd>d:
            beats[i]+=1

r = 1
for item in beats:
    r*=item

time = int(''.join([n for n in lines[0].split(':')[1].split()]))
distance = int(''.join([n for n in lines[1].split(':')[1].split()]))

beat = 0
for v in range(time):
    nd=v*(time-v)
    if nd>distance:
        beat+=1

print('------------------------')
print('Part 1:',r)
print('------------------------')
print('Part 2:',beat)
print('------------------------')