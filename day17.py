from collections import defaultdict
from copy import copy
with open('day17.txt','r') as f:
    text=f.read().strip()

# text='''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''

heads = [-1 for _ in range(7)]
step=0
fallen=0
shapes = [['..####.'],['...#...','..###..','...#...'],['....#..','....#..','..###..'],['..#....','..#....','..#....','..#....'],['..##...','..##...']]
grid = ['.......']
no_rep = True

def impact(shape, grid, curry):
    if curry==0:
        return True
    for j, row in enumerate(shape[::-1]):
        if len(grid) > curry - 1 +j:
            for i,c in enumerate(row):
                if c=='#' and grid[curry-1+j][i]=='#':
                    return True
    return False

def cross(grid, shape, curry, dir):
    for j, row in enumerate(shape[::-1]):
        if len(grid) > curry + j:
            for i,c in enumerate(row):
                if c=='#' and grid[curry+j][i+dir]=='#':
                    return True
    return False

gridstate={}
exp=0
while fallen<2022 or no_rep:
    curry=max(heads)+4
    shape = copy(shapes[fallen%5])
    while True:
        # jet effect
        if text[step%len(text)]=='<':
            if all(x[0]=='.' for x in shape) and not cross(grid, shape, curry, -1):
                # shift left
                shape=[x[1:]+'.' for x in shape]
        else:
            if all(x[-1]=='.' for x in shape) and not cross(grid, shape, curry, 1):
                # shift right
                shape=['.'+x[:-1] for x in shape]
        step+=1
        step%=len(text)
        # check grid as well?
        if impact(shape, grid, curry):
            break
        curry-=1
    fallen+=1
    exp+=sum(1 for y in shape for x in y if x=='#')
    #update heads and grid
    for i, x in enumerate(shape[::-1]):
        heads=[curry+i if x[l]=='#' and curry+i>=heads[l] else heads[l] for l in range(len(heads))]
    new_grid = grid[:curry] + [''.join(['#' if (len(grid) > curry + j and
                                                grid[curry + j][i] == '#') or
                                               r[i] == '#' else '.' for i in range(7)]) for j, r in
                               enumerate(shape[::-1])]

    if len(new_grid)<len(grid):
        new_grid=new_grid+grid[len(new_grid):]
    grid=new_grid
    if fallen==2022:
        print(f'p1: {max(heads)+1}')
    if gridstate.get((step,tuple(grid[-10:]))) and no_rep:
        first,v = gridstate[(step,tuple(grid[-10:]))]
        if (1000000000000-fallen)%(fallen-first)==0:
            dest=1000000000000
            duration = fallen-first
            incr = max(heads)-v
            repeats = (dest-fallen)//duration
            h = max(heads)+1+repeats*incr
            print(f'p2: {h}')
            no_rep=False
    elif no_rep:
        gridstate[(step,tuple(grid[-10:]))]=(fallen,max(heads))

