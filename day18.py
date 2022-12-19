with open('day18.txt','r') as f:
    text=f.read().splitlines()

# text='''2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5'''.splitlines()

occupied = set()
for a in text:
    e1, e2, e3 = a.split(',')
    e = (int(e1),int(e2),int(e3))
    occupied.add(e)

vs = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
def adj(e, ra=vs):
    return [(e[0]+v1,e[1]+v2,e[2]+v3) for v1,v2,v3 in ra]

minx, miny, minz = min(x[0] for x in occupied),min(x[1] for x in occupied), min(x[2] for x in occupied)
maxx, maxy, maxz = max(x[0] for x in occupied),max(x[1] for x in occupied), max(x[2] for x in occupied)

def bounded(e):
    e1,e2,e3 = e
    return minx-1<=e1<=maxx+1 and miny-1<=e2<=maxy+1 and minz-1<=e3<=maxz+1

check=[(minx-1,miny-1,minz-1)]
exposed = set()
while check:
    elem = check.pop(0)
    exposed.add(elem)
    for x in adj(elem):
        if x not in occupied and x not in exposed and x not in check and bounded(elem):
            check.append(x)

free=0
exp=0
for x in range(minx-1, maxx + 2):
    for y in range(miny-1, maxy + 2):
        for z in range(minz-1, maxz + 2):
            hit = sum(1 for e in adj((x,y,z)) if e in occupied)
            if (x,y,z) not in occupied and hit:
                free+=hit
                if (x,y,z) in exposed:
                    exp+=hit

print(free)
print(exp)