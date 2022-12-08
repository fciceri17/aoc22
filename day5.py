with open('day5.txt','r') as f:
    lines = [x[:-1] for x in f.readlines()]

stacks = [list() for _ in range(9)]
instructions = []
for cc,l in enumerate(lines):
    if cc<8:
        for i, c in enumerate(l):
            if (i-1)%4==0 and c!=' ':
                stacks[(i-1)//4].append(c)
    elif len(l)>0 and cc>9:
        k=l.split()
        instructions.append((int(k[1]), int(k[3]), int(k[5])))


stacks_1 = [s[::-1] for s in stacks]
for amt, orig, dest in instructions:
    for i in range(amt):
        stacks_1[dest-1].append(stacks_1[orig-1].pop())
print(''.join(x[-1] for x in stacks_1))

stacks_2 = [s[::-1] for s in stacks]
for amt, orig, dest in instructions:
    for i in range(-amt,0):
        stacks_2[dest - 1].append(stacks_2[orig - 1].pop(i))
print(''.join(x[-1] for x in stacks_2))
