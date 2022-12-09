with open('day9.txt','r') as f:
    text=f.read().splitlines()


tail_len=9
loc ={e:[0,0] for e in list(range(tail_len + 1))}
visited={(0,0)}

adv = 0
while adv<len(text):
    step = text[adv].split(' ')
    dist = int(step[1])
    for _ in range(dist):
        if step[0] == 'R':
            loc[0][0]+=1
        elif step[0] == 'L':
            loc[0][0] -= 1
        elif step[0] == 'U':
            loc[0][1] +=1
        else:
            loc[0][1]-=1
        for fol in range(1, tail_len + 1):
            dx = loc[fol-1][0]-loc[fol][0]
            dy = loc[fol-1][1]-loc[fol][1]
            if abs(dx)>1:
                loc[fol][0]+=abs(dx)/dx
            elif abs(dx)==1:
                if abs(dy)>1:
                    loc[fol][0]+=abs(dx)/dx
            if abs(dy)>1:
                loc[fol][1]+=abs(dy)/dy
            elif abs(dy)==1:
                if abs(dx)>1:
                    loc[fol][1] += abs(dy) / dy
        visited.add((loc[tail_len][0], loc[tail_len][1]))
    adv+=1

print(len(visited))