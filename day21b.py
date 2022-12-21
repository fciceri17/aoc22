import re
with open('day21.txt','r') as f:
    text=f.read().splitlines()


# text='''root: pppw + sjmn
# dbpl: 5
# cczh: sllz + lgvd
# zczc: 2
# ptdq: humn - dvpt
# dvpt: 3
# lfqf: 4
# humn: 5
# ljgn: 2
# sjmn: drzm * dbpl
# sllz: 4
# pppw: cczh / lfqf
# lgvd: ljgn * ptdq
# drzm: hmdt - zczc
# hmdt: 32'''.splitlines()

ops = [x.split(': ') for x in text]

def get_res(ops, humn=None):
    stack = []
    state = {}
    missing=set()
    for node, v in ops:
        if n := re.match('[0-9]+', v):
            if node == 'humn' and humn:
                state[node]=humn
            else:
                state[node]=int(n[0])
        else:
            o1, op, o2 = v.split()
            if node=='root':
                op = '-'
            stack.append((node,(o1,op,o2)))
            missing.add(node)

    while 'root' in missing:
        node, (o1,op,o2) = stack.pop(0)
        # if node == 'root':
        #     stack.append((node, (o1,op,o2)))
        #     continue
        if o1 in state and o2 in state:
            run = f"state['{o1}'] {op} state['{o2}']"
            state[node] = eval(run)
            missing.remove(node)
        else:
            stack.append((node, (o1,op,o2)))
    return state['root']

max_shout = 20000000000000
min_shout=0
found = False
while not found:
    shout = (max_shout + min_shout) // 2
    if (rs := get_res(ops,shout))>0:
        min_shout = shout
    elif rs==0:
        found = True
    elif rs<0:
        max_shout=shout
print(shout)
