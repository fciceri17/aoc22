with open('day9.txt','r') as f:
    text=f.read().splitlines()



hx,hy,tx,ty=0,0,0,0
visited={(0,0)}

adv = 0
while adv<len(text):
    step = text[adv].split(' ')
    dist = int(step[1])
    for _ in range(dist):
        if step[0] == 'R':
            hx+=1
        elif step[0] == 'L':
            hx -= 1
        elif step[0] == 'U':
            hy+=1
        else:
            hy-=1
        dx = hx-tx
        dy = hy-ty
        if abs(dx)>1:
            tx+=abs(dx)/dx
        elif abs(dx)==1:
            if abs(dy)>1:
                tx+=abs(dx)/dx
        if abs(dy)>1:
            ty+=abs(dy)/dy
        elif abs(dy)==1:
            if abs(dx)>1:
                ty += abs(dy) / dy
        visited.add((tx,ty))
    adv+=1

print(len(visited))