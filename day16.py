from common.dijkstra import dijkstra

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
smax = 30
opened = set()

nodes = {k: {d: 1 for d in v} for k, v in links.items()}

all_dist = {s: {d: dijkstra(nodes, s, d) for d in nodes if d != s} for s in nodes}


def op(s):
    return ','.join(sorted(s))

def potential(pos, left, ops):
    opened = set(ops.split(',')) if ops else set()
    local_pot = flow[pos] * (left - 1) if left > 1 else 0
    if left>0:
        goto = [dest for dest in nodes if dest != pos and flow[dest] and dest not in opened and all_dist[pos][dest]<left-2]
    else:
        goto=[]
    if goto and left>2:
        if local_pot > 0:
            left-=1
            return local_pot+ max(potential(g, left - all_dist[pos][g], op(opened.union([pos]))) for g in goto)
        else:
            return max(potential(g, left - all_dist[pos][g], op(opened)) for g in goto)
    else:
        return local_pot


print(potential(pos, smax, op(opened)))
