print('2023 - Day 1')

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


n = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0,
}

def find_first_digit(text):
    ifirst=1000
    for i,key in enumerate(n.keys()):
        if text.find(key)<ifirst and text.find(key)>-1:
            ifirst=text.find(key)
            out = n[key]

    for i,c in enumerate(text):
        if i>ifirst:
            break

        if c.isdigit() and i<ifirst:
            ifirst=i
            out=int(c)

    return out

def find_last_digit(text):
    ilast=-1000
    for i,key in enumerate(n.keys()):
        if text.find(key)>-1 and text.rindex(key)>ilast:
            ilast=text.rindex(key)
            out = n[key]

    for i,c in enumerate(text):

        if c.isdigit() and i>ilast:
            ilast=i
            out=int(c)

    return out

numbers1=[]
numbers2=[]

for line in lines:
    
    first=True
    firstdigit=0
    lastdigit=0
    for c in line:
        if c.isdigit() and first:
            firstdigit=c
            first=False
        elif c.isdigit():
            lastdigit=c
    if lastdigit==0:
        lastdigit=firstdigit
    numbers1.append(int(firstdigit+lastdigit))
    numbers2.append(find_first_digit(line)*10+find_last_digit(line))

for i,item in enumerate(numbers2):
    print(lines[i],item)

print('------------------------')
print('Part 1:',sum(numbers1))
print('------------------------')
print('Part 2:',sum(numbers2))
print('------------------------')