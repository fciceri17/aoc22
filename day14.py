with open('day14.txt','r') as f:
    text=f.read().splitlines()

# text='''498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9'''.splitlines()

explored = set()

for rows in text:
    draw = rows.split('->')
    points = [tuple(int(x) for x in point.split(',')) for point in draw]
    for i in range(len(points)-1):
        (x1,y1),(x2,y2) = points[i:i+2]
        if x1==x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                explored.add((x1,y))
        else:
            for x in range(min(x1,x2),max(x1,x2)+1):
                explored.add((x,y1))

stone = len(explored)
maxy = max(el[1] for el in explored)
can_stop=True

while can_stop:
    x, y = 500, 0
    exploring=True
    while exploring:
        if y>maxy or (x,y) in explored:
            can_stop=False
            exploring=False
            break
        curr_x, curr_y = x,y
        if (x,y+1) not in explored:
            x,y=x,y+1
        elif (x-1,y+1) not in explored:
            x,y=x-1,y+1
        elif (x+1, y+1) not in explored:
            x,y=x+1,y+1
        else:
            break
    if exploring:
        explored.add((x,y))
print(len(explored)-stone)