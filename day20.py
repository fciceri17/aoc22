from collections import deque
with open('day20.txt','r') as f:
    text=f.read().splitlines()

# text='''1
# 2
# -3
# 3
# -2
# 0
# 4'''.splitlines()

def grove_sum(v_list, cycles=1):
    seq = deque([(i,x) for (i,x) in enumerate(v_list)])
    o = list(seq)
    for _ in range(cycles):
        for x in o:
            idx = seq.index(x)
            seq.remove(x)
            seq.rotate(-(x[1]%len(seq)))
            seq.insert(idx,x)


    o = [x[1] for x in seq].index(0)
    print(sum(seq[(i+o)%len(seq)][1] for i in (1000,2000,3000)))

v = [int(x) for x in text]
grove_sum(v)
grove_sum([x*811589153 for x in v],10)