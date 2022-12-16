from common.dijkstra import dijkstra
from functools import cache
import re

with open('day16.txt', 'r') as f:
    text = f.read().splitlines()

# text = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II'''.splitlines()

flow = {}
links = {}
for line in text:
    v, rate, leads = re.match('Valve ([A-Z]+) has flow rate=([0-9]+);.*valve[s]* (.*)', line).groups()
    flow[v] = int(rate)
    links[v] = leads.split(', ')

pos = 'AA'
smax = 26
opened = set()

nodes = {k: {d: 1 for d in v} for k, v in links.items()}
flowing = {k for k in nodes if flow[k]}

all_dist = {s: {d: dijkstra(nodes, s, d) for d in nodes} for s in nodes}


def op(s):
    return ','.join(sorted(s))

@cache
def potential(pos, left, ops):
    if sum(left)<=0:
        return 0
    opened = set(ops.split(',')) if ops else set()
    local_pot = [flow[pos[x]] * (left[x] - 1) if left[x] > 1 and pos[x] not in opened else 0 for x in range(2)]
    opened.update(pos)
    cd = [set() for _ in range(2)]
    for i in range(2):
        for dest in flowing.difference(opened):
            if all_dist[pos[i]][dest]<left[i]-1:
                cd[i].add(dest)
        if not cd[i]:
            cd[i].add(pos[i])
    gs = {(d1,d2) for d1 in cd[0] for d2 in cd[1] if d1!=d2}
    if pos==('AA','AA'):
        goto=set()
        for elem in gs:
            if (elem[1],elem[0]) not in goto:
                goto.add(elem)
    else:
        goto=gs
    if goto and any(x>2 for x in left):
        if sum(local_pot) > 0:
            left=(max(left[0]-1, 0), max(left[1]-1,0))
            return sum(local_pot) + max(potential(g, (left[0] - all_dist[pos[0]][g[0]], left[1] - all_dist[pos[1]][g[1]],), op(opened)) for g in goto)
        else:
            if pos in goto:
                return 0
            return max(potential(g, (left[0] - all_dist[pos[0]][g[0]], left[1] - all_dist[pos[1]][g[1]]), op(opened)) for g in goto)
    else:
        return sum(local_pot)


print(potential((pos,pos), (smax,smax), op(opened)))
