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

stack = []
state = {}
for node, v in ops:
    if n := re.match('[0-9]+', v):
        state[node]=int(n[0])
    else:
        o1, op, o2 = v.split()
        stack.append((node,(o1,op,o2)))

while stack:
    node, (o1,op,o2) = stack.pop(0)
    if o1 in state and o2 in state:
        run = f"state['{o1}'] {op} state['{o2}']"
        state[node] = eval(run)
    else:
        stack.append((node, (o1,op,o2)))

print(state['root'])