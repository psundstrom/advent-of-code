print('2023 - Day 3')

with open('./2023/Day3/input.txt') as file:
    lines = [line.rstrip() for line in file]


# numbers = [[''.join(c for c in n if c.isdigit()) for n in line.replace('').split('.') if n!=''] for line in lines]

numbers=[]

for i,line in enumerate(lines):
    if i==39:
        pass
    stripped=''
    for c in line:
        if c.isdigit() or c=='.':
            stripped+=c
        else:
            stripped+='.'
    numbers.append([n for n in stripped.split('.') if n!=''])

partnumbers = []
# print(numbers)
for i,line in enumerate(lines):
    # print(i,line)
    # print(numbers[i])
    s0 = 0
    if i==39:
        pass
    for number in numbers[i]:
        # print(number)
        start = line.find(number,s0)
        neighbours = []
        end = start+len(number)-1
        s0=end+1
        if end>=len(line)-1:
            end-=1
        else:
            neighbours.append(line[end+1])
        if start==0:
            start+=1
        else:
            neighbours.append(line[start-1])
        if i>0:
            neighbours.extend(lines[i-1][start-1:end+2])
        if i<len(lines)-1:
            neighbours.extend(lines[i+1][start-1:end+2])
        part=False
        for item in neighbours:
            if item.isdigit() or item=='.':
                pass
            else:
                part=True
        if part:
            partnumbers.append(int(number))
            if i==39:
                print('Part number at line',i+1)
                if i>0:
                    print(lines[i-1][start-1:end+2])
                print(line[start-1:end+2])
                if i<len(line)-1:
                    print(lines[i+1][start-1:end+2])
        else:
            print('Non part at line',i+1)
            if i>0:
                print(lines[i-1][start-1:end+2])
            print(line[start-1:end+2])
            if i<len(line)-1:
                print(lines[i+1][start-1:end+2])

print('------------------------')
print('Part 1:',sum(partnumbers))
print('------------------------')
print('Part 2:',0)
print('------------------------')