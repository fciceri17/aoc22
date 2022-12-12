from queue import PriorityQueue
with open('day12.txt','r') as f:
    text=f.read().splitlines()
#
# text='''Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi'''.splitlines()


def dijkstra(G, start, goal):
    """ Uniform-cost search / dijkstra """
    visited = set()
    cost = {start: 0}
    parent = {start: None}
    todo = PriorityQueue()

    todo.put((0, start))
    while todo:
        while not todo.empty():
            _, vertex = todo.get()  # finds lowest cost vertex
            # loop until we get a fresh vertex
            if vertex not in visited: break
        else:  # if todo ran out
            break  # quit main loop
        visited.add(vertex)
        if vertex == goal:
            break
        for neighbor, distance in G[vertex]:
            if neighbor in visited: continue  # skip these to save time
            old_cost = cost.get(neighbor, float('inf'))  # default to infinity
            new_cost = cost[vertex] + distance
            if new_cost < old_cost:
                todo.put((new_cost, neighbor))
                cost[neighbor] = new_cost
                parent[neighbor] = vertex

    return parent


def make_path(parent, goal):
    if goal not in parent:
        return None
    v = goal
    path = []
    while v is not None:  # root has null parent
        path.append(v)
        v = parent[v]
    return path[::-1]


nodes = {(i,j):set() for i in range(len(text[0])) for j in range(len(text))}

known={}
starts=set()
for i,r in enumerate(text):
    for j,c in enumerate(r):
        if c in ('S','E'):
            known[c]=(j,i)
        if c=='a':
            starts.add((j,i))
        for ii,jj in [(-1,0),(1,0),(0,-1),(0,1)]:
                if jj+j >=0 and j+jj<len(r) and i+ii>=0 and i+ii<len(text):
                    v = text[i+ii][j+jj]
                    if v=='E':
                        v='z'
                    dist = ord(v)-ord(c)
                    if dist<=1 or c=='S':
                        nodes[(j,i)].add(((j+jj,i+ii), 1))


path = make_path(dijkstra(nodes,known['S'],known['E']), known['E'])
print(len(path)-1)
cand = [make_path(dijkstra(nodes,x,known['E']), known['E']) for x in starts]
print(min(len(x)-1 for x in [*cand,path] if x))