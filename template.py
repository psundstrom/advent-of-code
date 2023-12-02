print('<YEAR> - Day <DAY>')

with open('./<YEAR>/Day<DAY>/input.txt') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    print(line)

print('------------------------')
print('Part 1:',0)
print('------------------------')
print('Part 2:',0)
print('------------------------')