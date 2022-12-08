import math

with open('day8.txt','r') as f:
    lines = f.read().split()

grid = [[int(x) for x in y] for y in lines]
# grid = [[int(x) for x in y] for y in '''30373
# 25512
# 65332
# 33549
# 35390'''.split()]

def check_vis(x, y):
    blocked = {}
    for dir in ['u','d','l','r']:
        block = False
        if dir == 'u':
            for i in range(0, y):
                if grid[y][x]<=grid[i][x]:
                    block = True
                    break
        if dir == 'd':
            for i in range(y+1, len(grid)):
                if grid[y][x]<=grid[i][x]:
                    block = True
                    break
        if dir == 'l':
            for i in range(0, x):
                if grid[y][x]<=grid[y][i]:
                    block = True
                    break
        if dir == 'r':
            for i in range(x+1, len(grid[0])):
                if grid[y][x]<=grid[y][i]:
                    block = True
                    break
        blocked[dir]=block
    return any(not x for x in blocked.values())

def scenic(x,y):
    viz = {}
    for dir in ['u','d','l','r']:
        cnt = 0
        if dir=='u':
            for i in range(y-1, -1, -1):
                if grid[y][x] > grid[i][x]:
                    cnt+=1
                else:
                    cnt+=1
                    break
        if dir=='d':
            for i in range(y+1, len(grid)):
                if grid[y][x] > grid[i][x]:
                    cnt+=1
                else:
                    cnt+=1
                    break
        if dir=='l':
            for i in range(x-1, -1, -1):
                if grid[y][x] > grid[y][i]:
                    cnt+=1
                else:
                    cnt+=1
                    break
        if dir=='r':
            for i in range(x+1, len(grid[0])):
                if grid[y][x] > grid[y][i]:
                    cnt+=1
                else:
                    cnt+=1
                    break
        viz[dir]=cnt
    return math.prod(viz.values())

print(sum(check_vis(tree_x, tree_y) for tree_x in range(1,len(grid[0])-1) for tree_y in range(1,len(grid)-1)) + len(grid)*2 + len(grid[0])*2 -4)
print(max(scenic(tree_x, tree_y) for tree_x in range(1,len(grid[0])-1) for tree_y in range(1,len(grid)-1)))