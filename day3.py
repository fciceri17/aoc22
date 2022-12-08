with open('day3.txt','r') as f:
    sacks=[list(x.strip()) for x in f.readlines()]

def c_prio(c):
    if c.isupper():
        prio=26
    else:
        prio=0
    prio +=ord(c.lower())-ord('a')+1
    return prio

roll=0
for sack in sacks:
    mid = len(sack)//2
    sack_prio = sum(c_prio(x) for x in set(sack[:mid]).intersection(sack[mid:]))
    roll+=sack_prio

print(roll)

roll=0
for i in range(len(sacks)//3):
    curr_sack = sacks[i*3:i*3+3]
    group_prio = sum(c_prio(x) for x in set(curr_sack[0]).intersection(curr_sack[1]).intersection(curr_sack[2]))
    roll+=group_prio

print(roll)