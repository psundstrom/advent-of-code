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
        rules=[]
        for item in parts[1].split(','):
            if '<' in item:
                op='<'
                var,rest = item.split('<')
                val,target = rest.split(':')
                val=int(val)
                rules.append([var,op,val,target])
            elif '>' in item:
                op='>'
                var,rest = item.split('>')
                val,target = rest.split(':')
                val=int(val)
                rules.append([var,op,val,target])
            else:
                op=''
                assert ':' not in item
                target=item
                rules.append([target])
        print(rules)
        W[name]=rules
    else:
        part=[0]*4
        for i,item in enumerate(line[1:-1].split(',')):
            part[i]=int(item.split('=')[1])
        P.append(part)

V={'x':0,'m':1,'a':2,'s':3}

def applyrule(part,rule):
    if len(rule)==1:
        return rule[0]
    var,op,val,target=rule
    if op=='<':
        if part[V[var]]<val:
            return target
        else:
            return None
    elif op == '>':
        if part[V[var]]>val:
            return target
        else:
            return None
    else:
        assert False    

def applyrule2(part,rule):
    # part is ranges [(low,high),(low,high),(low,high),(low,high)]
    # range means low:high -> high is not included in range, so (low,high) means low<=x<high
    # return set of parts with ranges with their corresponding targets
    if len(rule)==1:
        return part,rule[0]
    var,op,val,target=rule
    if op=='<':
        low,high = part[V[var]]
        if high<=val:
            return part,target
        if low>val:
            return [],'R'
        part[V[var]] = (low,val)
        return part,target
    elif op == '>':
        low,high = part[V[var]]
        if high<=val+1:
            return [],'R'
        if low>val:
            return part,target
        part[V[var]] = (val+1,high)
        return part,target
    else:
        assert False
    # in{
    #     part=[(0,4000),(0,4000),(0,4000),(0,4000)]
    
    #     m>1770:pm -> m=1771-4000 goes to pm -> (1771,4001)
    #    ,m>644:sz, -> m=645-1770 goes to sz -> (645,1771)
    #     nc} m=0-644 goes to nc -> (0,645)

    return parts,targets

def applyworkflow2(part,target):
    # parts as ranges -> [(low,high),(low,high),(low,high),(low,high)]
    workflow = W[target]
    ans=0
    for rule in workflow:
        newpart,newtarget=applyrule2(part,rule)
        if newtarget=='A':
            result=1
            for high,low in newpart:
                result*=(high-low)
            ans+=result
        elif newtarget=='R':
            ans+=0
        else:
            ans+=applyworkflow2(newpart,newtarget)
    return ans

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


#     applyworkflow([(1771,4000),(0,4000),(0,4000),(0,4000)],'pm')
#     applyworkflow([(645,1770),(0,4000),(0,4000),(0,4000)],'sz')
#     applyworkflow([(0,644),(0,4000),(0,4000),(0,4000)],'nc')

part=[(0,4001),(0,4001),(0,4001),(0,4001)]

print(applyworkflow2(part,'in'))
# 4672272366464 is too low

print('------------------------')
print('Part 1:',sum([sum(p) for p in A]))
print('------------------------')
print('Part 2:',0)
print('------------------------')