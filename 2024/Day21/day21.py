print('2024 - Day 21')

with open('./2024/Day21/input.ex') as file:
    lines = [line.rstrip() for line in file]

""" 
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+ 

Robot starts pointing at A
"""

PN = {
    '7': (0,0),
    '8': (0,1),
    '9': (0,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2),
    '0': (3,1),
    'A': (3,2),
}

""" 
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

Robot starts pointing at A
 """

PD = {
    '^': (0,1),
    'A': (0,2),
    '<': (1,0),
    'v': (1,1),
    '>': (1,2),
}

def getmotion(source, target, P):
    t = P[target]
    s = P[source]
    dr = t[0]-s[0]
    dc = t[1]-s[1]

    if dr>0: rm = 'v'*abs(dr)
    elif dr<0: rm = '^'*abs(dr)
    else: rm = ''
    if dc>0: cm = '>'*abs(dc)
    elif dc<0: cm = '<'*abs(dc)
    else: cm = ''
    return rm+cm

print(getmotion('A','^', PD))
print(getmotion('A','<', PD))
print(getmotion('<','A', PD))
print('----')

print(getmotion('0','2', PN))
print(getmotion('A','0', PN))
print(getmotion('2','9', PN))
print(getmotion('9','A', PN))

def getscore(s,debug=False):
    n = int(s[:-1])
    if debug:
        print(s)
    s = 'A' + s 
    seq = ''.join([getmotion(s[i],s[i+1],PN)+'A' for i in range(len(s)-1)])
    if debug:
        print(seq)
    s='A'+seq
    seq = ''.join([getmotion(s[i],s[i+1],PD)+'A' for i in range(len(s)-1)])
    if debug:
        print(seq)
    s='A'+seq
    seq = ''.join([getmotion(s[i],s[i+1],PD)+'A' for i in range(len(s)-1)])

    if debug:
        print(seq)
        print(len(seq))
    return len(seq)*n

ans1 = 0
for line in lines:
    ans1+=getscore(line,debug=True)

print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',0)
print('------------------------')