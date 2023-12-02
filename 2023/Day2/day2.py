print('2023 - Day 2')

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

#12 red, 13 green, 14 blue

possible =[1]*len(lines)
powers = [0]*len(lines)
for game,line in enumerate(lines):
    g = line.split(': ')

    sets = g[1].split(';')

    maxred=0
    maxgreen=0
    maxblue=0
    for s in sets:
        parts = s.strip().split(', ')
        for i,item in enumerate(parts):
            n = int(item.split(' ')[0])
            c = item.split(' ')[1].strip()
            if c=='red' and n>maxred:
                maxred=n
            if c=='green' and n>maxgreen:
                maxgreen=n
            if c=='blue' and n>maxblue:
                maxblue=n
            if c=='red' and n>12:
                possible[game]=0
            if c=='green' and n>13:
                possible[game]=0
            if c=='blue' and n>14:
                possible[game]=0
    powers[game]=maxred*maxgreen*maxblue

print('------------------------')
print('Part 1:',sum([i+1 for i,item in enumerate(possible) if item==1]))
print('------------------------')
print('Part 2:',sum(powers))
print('------------------------')