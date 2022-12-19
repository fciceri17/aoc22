import math

with open('day13.txt','r') as f:
    pairs=f.read().split('\n\n')

# pairs = '''[1,1,3,1,1]
# [1,1,5,1,1]
#
# [[1],[2,3,4]]
# [[1],4]
#
# [9]
# [[8,7,6]]
#
# [[4,4],4,4]
# [[4,4],4,4,4]
#
# [7,7,7,7]
# [7,7,7]
#
# []
# [3]
#
# [[[]]]
# [[]]
#
# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]'''.split('\n\n')

def compare_list(l1, l2):
    for i, elem in enumerate(l1):
        if len(l2) - 1 < i and len(l2)<len(l1):
            return -1
        if isinstance(elem, list):
            c1 = elem
            c2 = l2[i] if isinstance(l2[i], list) else [l2[i]]
        else:
            if not isinstance(l2[i], list):
                if elem == l2[i]:
                    continue
                return 1 if elem<l2[i] else -1
            else:
                c1,c2 = [elem], l2[i]
        if rv:=compare_list(c1,c2):
            return rv
    if len(l2)>len(l1):
        return 1
    return 0

idxs=[]
for i, pair in enumerate(pairs):
    a, b = eval(pair.replace('\n',','))
    if compare_list(a,b)>=0:
        idxs.append(i+1)
print(sum(idxs))

packets = [x for y in [eval(pair.replace('\n', ',')) for pair in pairs] for x in y] + [[[2]]] + [[[6]]]
assigned = []
while len(assigned)<len(packets):
    left = set(list(range(len(packets)))).difference(assigned)
    for i in left:
        for j in left:
            if i!=j and compare_list(packets[i], packets[j])<0:
                break
        else:
            assigned.append(i)
print(math.prod([i + 1 for i in range(len(assigned)) if assigned[i] > len(packets) - 3]))

