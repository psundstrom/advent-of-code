print('2023 - Day 20')

from collections import deque
import math

with open('./2023/Day20/input.txt') as file:
    lines = [line.rstrip() for line in file]

M={}
for line in lines:
    name,rest = line.split(' -> ')
    dest = [k.strip() for k in rest.split(',')]
    name=name.strip()
    if name=='broadcaster':
        type='b'
        state=None
    else:
        type=name[0]
        name=name[1:]
    if type=='&':
        state=[]
    if type=='%':
        state=0
    inputs=[]
    M[name]={'type':type,'dest':dest,'state':state,'inputs':[]}

keys = [k for k in M.keys()]
for key in keys:
    for dest in M[key]['dest']:
        if dest not in M.keys():
            M[dest]={'type':'r','dest':[],'state':[],'inputs':[dest]}
        M[dest]['inputs'].append(key)
        if M[dest]['type']=='&':
            M[dest]['state'].append(0)

def flipflop(module,pulse):
    assert M[module]['type']=='%'
    # Flip-flop modules (prefix %) are either on or off; they are initially off. If a flip-flop module receives a high pulse, it is ignored and nothing happens. However, if a flip-flop module receives a low pulse, it flips between on and off. If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.

    if pulse==1:
        return None
    else:
        if M[module]['state']==0:
            M[module]['state']=1
            return 1
        elif M[module]['state']==1:
            M[module]['state']=0
            return 0
        else:
            assert False

# if return is 1, pulses are sent

def conjunction(module,pulse,source):
    assert M[module]['type']=='&'

    if module=='zr':
        pass
    # Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules; they initially default to remembering a low pulse for each input. When a pulse is received, the conjunction module first updates its memory for that input. Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.

    M[module]['state'][M[module]['inputs'].index(source)]=pulse
    if sum(M[module]['state'])==len(M[module]['state']):
        return 0
    else:
        return 1

def printstates():
    g = ''
    for k,m in M.items():
        if m['type']=='&':
            state=m['state']
            g+=f'{k} ({sum(state)}):'
            g+=''.join([f'{s}' for s in m['state']])
            g+=' '
    print(g)

def getfullstate(M):
    return ''.join([getstate(m) for m in M.values()])

def getstate(m):
    if m['type']=='&':
        return ''.join([str(n) for n in m['state']])
    else:
        return m['state']

low=0
high=0
ans1=0

cycles = {}
seen = {}
presses=0
found = False
for i in range(1000000):
    if found:
        break
    presses+=1
    if i==1000:
        ans1=low*high
    low+=1
    Q=deque()
    for dest in M['broadcaster']['dest']:
        Q.append((dest,0,'broadcaster'))
    found=False

    nrx=0
    while Q:
        dest,pulse,source=Q.popleft()
        if dest=='zr' and pulse==1:
            if source not in seen:
                seen[source]=0
            else:    
                seen[source]+=1
            if source not in cycles:
                cycles[source] = presses
            else:
                assert presses == (seen[source]+1) * cycles[source]
            if all(seen.values()):
                x=1
                for cycle in cycles.values():
                    x = math.lcm(x,cycle)
                ans2=x
                found=True
                break
        if pulse==0:
            low+=1
        if pulse==1:
            high+=1
        if M[dest]['type']=='%':
            res = flipflop(dest,pulse)
            if res is not None:
                for t in M[dest]['dest']:
                    Q.append((t,res,dest))
        elif M[dest]['type']=='&':
            res = conjunction(dest,pulse,source)
            for t in M[dest]['dest']:
                Q.append((t,res,dest))
    
print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',ans2)
print('------------------------')