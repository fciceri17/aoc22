import heapq
from collections import defaultdict
from functools import cache
with open('day24.txt','r') as f:
    text=f.read().splitlines()
    
# text='''#.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#'''.splitlines()

UP='^'
LEFT='<'
RIGHT='>'
DOWN='v'

grid=[[x for x in y] for y in text]

class Grid:

    def __init__(self, grid):
        self.grid=grid
        self.xmin=1
        self.ymin=1
        self.xmax=len(grid[0])-2
        self.ymax=len(grid)-2
        self.moving={direction:set() for direction in (UP,DOWN,LEFT,RIGHT)}
        for row, row_o in enumerate(self.grid):
            for col, v in enumerate(row_o):
                if v not in ('#','.'):
                    self.moving[v].add((row,col))

    @cache
    def get_moving(self, step):
        if step==0:
            return self.moving
        moving=self.get_moving(step - 1)
        new_moving = {d: {self.get_next(pos,d) for pos in v} for d,v in moving.items()}
        return new_moving


    def get_next(self, pos, direction):
        row,col=pos
        if direction==UP:
            if row==self.ymin:
                return self.ymax, col
            return row-1, col
        elif direction==DOWN:
            if row==self.ymax:
                return self.ymin, col
            return row+1, col
        elif direction==LEFT:
            if col==self.xmin:
                return row, self.xmax
            return row, col-1
        if col==self.xmax:
            return row, self.xmin
        return row, col+1
    
    @cache
    def get_occupied(self,step):
        storms = self.get_moving(step)
        occupied = {x for y in storms.values() for x in y}
        return occupied
    
    def get_dest(self, pos, step):
        row,col=pos
        occupied=self.get_occupied(step+1)
        
        return {((row+i, col+j),step+1):1 for i,j in [(0,0),(0,1),(1,0),(0,-1),(-1,0)] if (row+i,col+j) not in occupied and ((self.xmin<=col+j<=self.xmax and self.ymin<=row+i<=self.ymax) or (row+i,col+j)==self.dest or (row+i,col+j)==self.start)}

def dijkstra_dyn(start, end, grid_obj, start_step=0):
  # initialize distances from start node to all other nodes
  grid_obj.dest=end
  grid_obj.start=start
  distances = defaultdict(lambda: float("inf"))
  distances[(start,start_step)] = 0

  # initialize a set of visited nodes
  visited = set()

  # initialize a priority queue of distances
  # we use a priority queue so that we can always get the smallest
  # distance in O(1) time
  queue = []
  heapq.heappush(queue, [0, (start,start_step)])

  while queue:
    # get the smallest distance from the queue
    current_distance, current_node = heapq.heappop(queue)

    # if we have reached the end node, we can stop
    if current_node[0] == end:
      ret_i = current_node
      break

    # if we have already visited this node, we can skip it
    if current_node in visited:
      continue

    # mark the current node as visited
    visited.add(current_node)

    # check the distances to each neighbor
    dests=grid_obj.get_dest(*current_node).items()
    for neighbor, edge_distance in dests:
      # if the distance to the neighbor is shorter using the current node,
      # update the distance for the neighbor
      if distances[neighbor] > current_distance + edge_distance:
        distances[neighbor] = current_distance + edge_distance

        # add the neighbor to the queue with the updated distance
        heapq.heappush(queue, [distances[neighbor], neighbor])

  # return the final distances to the end node
  return ret_i

g=Grid(grid)
start=(0,1)
dest=(len(grid)-1,g.xmax)
p1=dijkstra_dyn(start,dest,g)
print(f'p1:{p1[1]}')
p15=dijkstra_dyn(dest,start,g,p1[1])
p2=dijkstra_dyn(start,dest,g,p15[1])
print(f'p2:{p2[1]}')