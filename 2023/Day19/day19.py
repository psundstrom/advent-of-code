print('2023 - Day 19')

with open('./2023/Day19/input.txt') as file:
    lines = [line.rstrip() for line in file]

W={}
P=[]
getparts=False
for line in lines:
    if len(line)==0:
        getparts=True
        continue
    if not getparts:
        line = line[:-1]
        parts = line.split('{')
        name=parts[0]
        rules=parts[1].split(',')
        W[name]=rules
    else:
        part=[0]*4
        for i,item in enumerate(line[1:-1].split(',')):
            part[i]=int(item.split('=')[1])
        P.append(part)

V={'x':0,'m':1,'a':2,'s':3}

def applyrule(part,rule):
    if '<' in rule:
        var,rest = rule.split('<')
        val,target = rest.split(':')
        val=int(val)
        if part[V[var]]<val:
            return target
        else:
            return None
    elif '>' in rule:
        var,rest = rule.split('>')
        val,target = rest.split(':')
        val=int(val)
        if part[V[var]]>val:
            return target
        else:
            return None
    else:
        assert ':' not in rule
        return rule


def applyworkflow(part,w):
    workflow = W[w]
    for rule in workflow:
        next=applyrule(part,rule)
        if not next:
            continue
        if next in ['A','R']:
            return next
        else:
            return applyworkflow(part,next)

A=[]
for part in P:
    result=applyworkflow(part,'in')
    if result=='A':
        A.append(part)

print('------------------------')
print('Part 1:',sum([sum(p) for p in A]))
print('------------------------')
print('Part 2:',0)
print('------------------------')