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
            if isinstance(l2[i], list):
                rv = compare_list(elem, l2[i])
                if rv!=0:
                    return rv
            else:
                rv = compare_list(elem, [l2[i]])
                if rv!=0:
                    return rv
        else:
            if isinstance(l2[i], list):
                rv =  compare_list([elem], l2[i])
                if rv!=0:
                    return rv
            else:
                if elem<l2[i]:
                    return 1
                elif elem>l2[i]:
                    return -1
                else:
                    continue
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
snt = []
while len(assigned)<len(packets):
    left = set(list(range(len(packets)))).difference(assigned)
    for i in left:
        for j in left:
            if i!=j and compare_list(packets[i], packets[j])<0:
                break
        else:
            assigned.append(i)
            if i>len(packets)-2:
                snt.append(i)
print(math.prod([i + 1 for i in range(len(assigned)) if assigned[i] > len(packets) - 3]))

