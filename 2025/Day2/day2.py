print('2025 - Day 2')

with open('./2025/Day2/input.txt') as file:
    lines = [line.rstrip() for line in file]

def checkrange1(start,stop):
    invalids = []
    for id in range(start,stop+1):
        id = str(id)
        if id[:len(id)//2] == id[len(id)//2:]:
            invalids.append(int(id))
    return invalids

def checkrange2(start,stop):
    invalids = []
    for id in range(start,stop+1):
        id = str(id)
        for n in range(1,len(id)//2+1):
            a = id[:n]
            invalid = True
            i = 0
            while invalid and i<len(id):
                if a != id[i:i+n]:
                    invalid = False
                    break
                i+=n
                if i>=len(id):
                    break
            if i==len(id) and invalid:
                invalids.append(int(id))
                break   
    return invalids

p1 = []
p2 = []

for line in lines[0].split(','):
    start,stop = line.split('-')
    start = int(start)
    stop = int(stop)
    p1.extend(checkrange1(start,stop))
    p2.extend(checkrange2(start,stop))

print('------------------------')
print('Part 1:',sum(p1))
print('------------------------')
print('Part 2:',sum(p2))
print('------------------------')