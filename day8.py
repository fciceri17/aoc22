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
    h = grid[y][x]
    for g in (range(y-1, -1, -1), range(y+1, len(grid))):
        for i in g:
            if h<=grid[i][x]:
                break
        else:
            return True
    for g in (range(x - 1, -1, -1), range(x + 1, len(grid[0]))):
        for i in g:
            if h <=grid[y][i]:
                break
        else:
            return True
    return False

def scenic(x,y):
    viz = []
    for g in (range(y-1, -1, -1), range(y+1, len(grid))):
        cnt = 0
        for i in g:
            cnt+=1
            if grid[y][x] <= grid[i][x]:
                break
        viz.append(cnt)
    for g in (range(x-1, -1, -1), range(x+1, len(grid[0]))):
        cnt = 0
        for i in g:
            cnt+=1
            if grid[y][x] <= grid[y][i]:
                break
        viz.append(cnt)
    return math.prod(viz)

print(sum(check_vis(tree_x, tree_y) for tree_x in range(1,len(grid[0])-1) for tree_y in range(1,len(grid)-1)) + len(grid)*2 + len(grid[0])*2 -4)
print(max(scenic(tree_x, tree_y) for tree_x in range(1,len(grid[0])-1) for tree_y in range(1,len(grid)-1)))
