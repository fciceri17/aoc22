import math
from collections import defaultdict
from functools import cache
import re
with open('day19.txt','r') as f:
    text=f.read().splitlines()


# text='''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
# Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'''.splitlines()

get_id = {
    'ore':0,
    'clay':1,
    'obsidian':2,
    'geode': 3
}

bp = {}
for blueprint in text:
    idx, costs = blueprint.split(':')
    idx = int(idx.split()[-1])
    bp[idx]={}
    for c in costs.split('.'):
        if c:
            g = re.match(r'Each (.*) robot costs (.*)', c.strip()).groups()
            pay = {get_id[v.split()[1]]:int(v.split()[0]) for v in g[1].split(' and ')}
            pay = tuple([pay.get(i,0) for i in range(4)])

            bp[idx][get_id[g[0]]]=pay

# bp structure
# bot: {resource1: amt1, resource2: amt2}



def has_leftover(cost, resources, n=1):
    return all(resources[x]>=cost[x]*n for x in range(4))

def refine_states(states):
    states_by_base = defaultdict(set)
    for state in states:
        states_by_base[state[0]].add(state[1])
    gmax = max(x[0][-1]+x[1][-1] for x in states)
    # good_bases = [base for base in states_by_base if all(base[n+1]==0 or base[n]<base[n+1]*5 for n in range(3))]
    ret = set()
    for base, res_v in states_by_base.items():
        for res in res_v:
            if base[-1]+res[-1]>=gmax-2:
                if not any(all(i >= j for i, j in zip(s, res)) for s in res_v if s!=res):
                    ret.add((base,res))
    return ret

def get_q(costs,t=24):
    states=defaultdict(set)
    states[0]={((1,0,0,0),(0,0,0,0))}

    @cache
    def buildable(res):
        bot_pairs = set()
        explore = [((0, 0, 0, 0), res)]
        while explore:
            start = explore.pop()
            bot_pairs.add(start)
            bots, resources = start
            for bot, expense in costs.items():
                leftover = [resources[n] - expense[n] for n in range(4)]
                if all(x >= 0 for x in leftover):
                    new_bots = (tuple([x if i != bot else x + 1 for i, x in enumerate(bots)]), tuple(leftover))
                    if new_bots not in bot_pairs:
                        bot_pairs.add(new_bots)
                        # explore.append(new_bots)
        return bot_pairs

    for i in range(t-1):
        states[i]=refine_states(states[i])
        for bots, res in states[i]:
            new_bots = buildable(res)
            states[i+1].update([(tuple([bots[n] + new_bot[n] for n in range(4)]), tuple([bots[n]+leftover[n] for n in range(4)])) for new_bot, leftover in new_bots])
    result=max(x[0][-1]+x[1][-1] for x in states[t-1])
    return result

q = {blueprint: get_q(v) for blueprint,v in bp.items()}

print(sum(a*b for a,b in q.items()))

p2 = [get_q(v,32) for blueprint,v in bp.items() if blueprint<=3]
print(p2,math.prod(p2))