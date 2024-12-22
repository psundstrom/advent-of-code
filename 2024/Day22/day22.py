print('2024 - Day 22')

with open('./2024/Day22/input.txt') as file:
    lines = [line.rstrip() for line in file]

from collections import defaultdict
from functools import cache

@cache
def mix(value,secret):
    return value^secret

@cache
def prune(secret):
    return secret%16777216

@cache
def evolve(secret):
    value=secret*64
    secret=mix(value,secret)
    secret=prune(secret)
    value=secret//32
    secret=mix(value,secret)
    secret=prune(secret)
    value=secret*2048
    secret=mix(value,secret)
    secret=prune(secret)
    return secret

def getones(n):
    return int(str(n)[-1])

ans1 = 0

PRICES = defaultdict(lambda: defaultdict(lambda: -100))

for line in lines:
    secret = int(line)
    hist=[]
    newsecret=secret
    for i in range(2000):
        newsecret=evolve(secret)
        diff = getones(newsecret)-getones(secret)
        if i>0:
            hist.append(diff)
            if len(hist)>4:
                hist.pop(0)
        if len(hist)==4 and PRICES[tuple(hist)][line]==-100:
            PRICES[tuple(hist)][line] = getones(newsecret)
        secret=newsecret
    ans1+=secret

TOTALS={}
for key in PRICES.keys():
    TOTALS[key]=0
    for line in lines:
        if PRICES[key][line]>0:
            TOTALS[key]+=PRICES[key][line]

maxseq=None
maxprice=-1
for key in TOTALS.keys():
    if TOTALS[key]>maxprice:
        maxprice=TOTALS[key]
        maxseq=key

print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',maxprice)
print('------------------------')