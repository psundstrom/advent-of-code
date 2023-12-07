print('2023 - Day 7')

with open('./2023/Day7/input.txt') as file:
    lines = [line.rstrip() for line in file]

hands=[]
bids=[]
H=[]

for line in lines:
    h,b = line.split()
    hands.append(list(h))
    bids.append(int(b))
    H.append((list(h),int(b)))

print(hands)
print(H)

val1 = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
val2 = {'A':13, 'K':12, 'Q':11, 'J':0, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}

def find_score(hand,part2):
    score=-1
    for card in hand:
        if card!='J' and part2:
            n =  hand.count(card)+hand.count('J')
        else:
            n = hand.count(card)
        if n==5:
            if score<7:
                score=7 
        elif n==4:
            if score<6:
                score=6
        elif n==3:
            hand_ = hand.copy()
            for _ in range(hand.count(card)):
                hand_.remove(card)
            for _ in range(hand.count('J')):
                if 'J' in hand_ and part2:
                    hand_.remove('J')
            if hand_[0]==hand_[1]:
                if score<5:
                    score=5
            else:
                if score<4:
                    score=4
        elif n==2:
            hand_ = hand.copy()
            for _ in range(hand.count(card)):
                hand_.remove(card)
            for _ in range(hand.count('J')):
                if 'J' in hand_ and part2:
                    hand_.remove('J')
            for c in hand_:
                if hand_.count(c)==2:
                    if score<3:
                        score=3
            if score<2:
                score=2
        else:
            if score<1:
                score=1
    return score

# scores = [find_score(h) for h in hands]

# alldata = [(hand,bid) for hand,bid in zip(hands,bids)]

H1= sorted(H, key = lambda e:(find_score(e[0],False),val1[e[0][0]],val1[e[0][1]],val1[e[0][2]],val1[e[0][3]],val1[e[0][4]]))
H2= sorted(H, key = lambda e:(find_score(e[0],True),val2[e[0][0]],val2[e[0][1]],val2[e[0][2]],val2[e[0][3]],val2[e[0][4]]))

ans1=0 
for i,(hand,bid) in enumerate(H1):
    ans1+=(i+1)*bid
    print(i+1,hand,bid,bids[hands.index(hand)],find_score(hand,False),val1[hand[0]])

ans2=0 
for i,(hand,bid) in enumerate(H2):
    ans2+=(i+1)*bid
    print(i+1,hand,bid,bids[hands.index(hand)],find_score(hand,False),val1[hand[0]])

print('------------------------')
print('Part 1:',ans1)
print('------------------------')
print('Part 2:',ans2)
print('------------------------')