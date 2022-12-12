import math
from collections import defaultdict
with open('day11.txt','r') as f:
    monkeys=f.read().split('\n\n')

m = {}
mods = []
for monkey in monkeys:
    entries = [x.strip() for x in monkey.splitlines()]
    num = int(entries[0][-2])
    items = [int(x) for x in entries[1].split(':')[-1].strip().split(',')]
    op_text = entries[2].split('= old')[-1].strip()
    op = {
        "* 3": lambda x: x*3,
        "+ 8": lambda x: x+8,
        "* old": lambda x: x*x,
        "+ 2": lambda x: x+2,
        "+ 3": lambda x: x + 3,
        "+ 6": lambda x: x + 6,
        "+ 1": lambda x: x + 1,
        "* 17": lambda x: x * 17,
    }[op_text]
    vmod = int(entries[3].split('by')[-1].strip())
    mods.append(vmod)
    test = lambda x,vmod=vmod: x%vmod == 0
    t_out = int(entries[4][-1])
    t_out2 = int(entries[5][-1])
    m[num]={
        'items': items,
        'op': op,
        'test': lambda x, t_out=t_out, t_out2=t_out2, test=test: t_out if test(x) else t_out2
    }

tot_mod = math.prod(mods)
inspected = defaultdict(int)
for round in range(10000):
    for m_index in range(8):
        inspected[m_index]+=len(m[m_index]['items'])
        for _ in range(len(m[m_index]['items'])):
            item = m[m_index]['items'].pop(0)
            worry = m[m_index]['op'](item)%tot_mod
            target = m[m_index]['test'](worry)
            m[target]['items'].append(worry)
            a=1

print(math.prod(sorted(inspected.values())[-2:]))