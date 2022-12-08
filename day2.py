with open('day2.txt','r') as f:
    text=f.readlines()

plays=[x.split() for x in text]
def scoreA(opp, you):
    score = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }.get(you)
    o,y = ord(opp),ord(you)
    y-=ord('X')-ord('A')
    if o>y and opp!='A' or opp=='A' and you=='Z':
        pass
    elif y>o and opp!='C' or opp=='C' and you=='X':
        score+=6
    else:
        score+=3
    return score

def scoreT(pair):
    score = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }.get(pair.strip().split()[-1])
    score+={
        'A X':3,
        'A Y':6,
        'A Z':0,
        'B X':0,
        'B Y':3,
        'B Z':6,
        'C X':6,
        'C Y':0,
        'C Z':3
    }.get(pair.strip())
    return score

def scoreZ(pair):
    score = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }.get(pair.strip().split()[-1])
    score += {
        'A X': 3,
        'A Y': 1,
        'A Z': 2,
        'B X': 1,
        'B Y': 2,
        'B Z': 3,
        'C X': 2,
        'C Y': 3,
        'C Z': 1
    }.get(pair.strip())
    return score

print(sum(scoreT(x) for x in text))
print(sum(scoreZ(x) for x in ['A Y', 'B X', 'C Z']))
print(sum(scoreZ(x) for x in text))
