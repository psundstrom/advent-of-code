print('2023 - Day 3')

with open('./2023/Day3/input.ex') as file:
    lines = [line.rstrip() for line in file]


# numbers = [[''.join(c for c in n if c.isdigit()) for n in line.replace('').split('.') if n!=''] for line in lines]

numbers=[]

for i,line in enumerate(lines):
    if i==10:
        pass
    stripped=''
    for c in line:
        if c.isdigit() or c=='.':
            stripped+=c
        else:
            stripped+='.'
    numbers.append([n for n in stripped.split('.') if n!=''])

# print(numbers[10])

for i,num in enumerate(numbers):
    for n in num:
        if not n.isnumeric():
            print('faaail',n,num)


# assert False


partnumbers = []
# print(numbers)
for i,line in enumerate(lines):
    print(i,line)
    print(numbers[i])
    if i==4:
        pass
    for number in numbers[i]:
        # print(number)
        start = line.find(number)
        neighbours = []
        end = start+len(number)-1
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

        #(''.join(neighbours))
print(partnumbers)
print(sum(partnumbers))   

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')