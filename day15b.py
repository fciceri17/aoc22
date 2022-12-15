with open('day15.txt','r') as f:
    text=f.read().splitlines()

detects = {}
for row in text:
    source,dest = row.split(':')
    src_x = source[12:].split(',')[0]
    src_y = source[12:].split('y=')[-1]
    dest_x = dest[24:].split(',')[0]
    dest_y = dest[24:].split('y=')[-1]
    detects[(int(src_x), int(src_y))] = (int(dest_x), int(dest_y))

for target in range(0,4000001):
    no_beacon = set()
    for src, dest in detects.items():
        rad = abs(src[0]-dest[0]) + abs(src[1]-dest[1])
        if -rad+src[1]<=target<=rad+src[1]+1:
            y=target-src[1]
            step = abs(y+rad) if y<=0 else abs(rad-y)
            no_beacon.add((src[0]-step, src[0]+step+1))

    nb = sorted(no_beacon)
    xmin, xmax = nb[0]
    for x_min,x_max in nb[1:]:
        if x_min<xmin<x_max:
            xmin=x_min
        if x_min<xmax<x_max:
            xmax=x_max

    if not(xmin<0 and xmax>=4000000):
        break

no_beacon = set()
for src, dest in detects.items():
    rad = abs(src[0]-dest[0]) + abs(src[1]-dest[1])
    if -rad + src[1] <= target <= rad + src[1] + 1:
        y=target-src[1]
        step = abs(y+rad) if y<=0 else abs(rad-y)
        for x in range(src[0]-step, src[0]+step+1):
            no_beacon.add((x,y+src[1]))

x_sol,y_sol = [(x,target) for x in range(0,4000001) if (x,target) not in no_beacon][0]
print(x_sol*4000000+y_sol)