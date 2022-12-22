import re
with open('day22.txt','r') as f:
    text=f.read().split('\n\n')

# text='''        ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.
# 
# 10R5L5R10L4R5L5'''.split('\n\n')

grid = text[0].split('\n')
instr = text[1]

dir=(1,0)
x,y=0,0
for i, v in enumerate(grid[0]):
    if v=='.':
        x=i
        break

newdir = {
    (1,0):{'R':(0,1),'L':(0,-1)},
    (-1,0):{'R':(0,-1),'L':(0,1)},
    (0,1):{'R':(-1,0),'L':(1,0)},
    (0,-1):{'R':(1,0),'L':(-1,0)},
}

moves = re.findall('[0-9]+', instr)
turns = re.findall('[LR]', instr)

for i,m in enumerate(moves):
    a=1
    for tiles in range(int(m)):
        newx,newy=x+dir[0], y+dir[1]
        if newx==len(grid[0]):
            newx=0
        elif newx<0:
            newx=len(grid[0])-1
        if newy==len(grid):
            newy=0
        elif newy<0:
            newy=len(grid)-1
        if grid[newy][newx]=='.':
            x,y = newx, newy
        elif grid[newy][newx]==' ':
            # find dot on opposite side
            if dir[0]==1:
                newx = min(k for k,v in enumerate(grid[y]) if v!=' ')
            elif dir[0]==-1:
                newx = max(k for k,v in enumerate(grid[y]) if v!= ' ')
            elif dir[1]==1:
                newy = min(k for k,v in enumerate(grid) if v[x] != ' ')
            else:
                newy = max(k for k,v in enumerate(grid) if v[x] != ' ')
            if grid[newy][newx]=='.':
                x,y = newx, newy
            else:
                # wall?
                break
        else:
            # hit a wall
            break
    if i<len(turns):
        dir = newdir[dir][turns[i]]

dirscore = {
    (1,0):0,
    (0,1):1,
    (-1,0):2,
    (0,-1):3
}

score = (y+1)*1000+(x+1)*4+dirscore[dir]
print(score)