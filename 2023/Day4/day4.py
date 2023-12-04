print('2023 - Day 4')

with open('./2023/Day4/input.txt') as file:
    lines = [line.rstrip() for line in file]

tickets=[]
draws=[]

for line in lines:
    parts = line.split(':')
    winners,numbers = parts[1].split('|')
    winners = [int(n) for n in winners.strip().split(' ') if n!='']
    numbers = [int(n) for n in numbers.strip().split(' ') if n!='']
    tickets.append(numbers)
    draws.append(winners)

N=[1]*len(tickets)

scores=[0]*len(tickets)
for i,ticket in enumerate(tickets):
    n=0
    for num in ticket:
        if num in draws[i]:
            n+=1
            if scores[i]==0:
                scores[i]=1
            else:
                scores[i]*=2
    for j in range(i+1,i+n+1):
        if j>len(N)-1:
            break
        N[j]+=N[i]

print('------------------------')
print('Part 1:',sum(scores))
print('------------------------')
print('Part 2:',sum(N))
print('------------------------')