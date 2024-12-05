print('2024 - Day 5')

with open('./2024/Day5/input.txt') as file:
    lines = [line.rstrip() for line in file]

rules = []
updates = []
for line in lines:
    if '|' in line:
        rules.append(list(map(int,line.split('|'))))
    elif len(line)>0:
        updates.append(list(map(int,line.split(','))))

def checkrule(update,rule):
    first=rule[0]
    last=rule[1]
    if first in update and last in update:
        return update.index(first)<update.index(last)
    return True
        
def checkupdate(update,rules):
    ok = True
    for rule in rules:
        if not checkrule(update,rule):
            ok=False
    return ok

ans1=0
for update in updates:
    if checkupdate(update,rules):
        ans1+=update[len(update)//2]

def fixupdate(update,rules):
    while not checkupdate(update,rules):
        for rule in rules:
            # print(rule)
            if not checkrule(update,rule):
                if rule[0] in update and rule[1] in update:
                    update.remove(rule[0])
                    update.insert(update.index(rule[1]),rule[0])
    assert checkupdate(update,rules)

ans2 = 0
for update in updates:
    if not checkupdate(update,rules):
        fixupdate(update,rules)
        ans2+=update[len(update)//2]

print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',ans2)
print('------------------------')