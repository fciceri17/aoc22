from functools import cache

with open('day7.txt','r') as f:
    lines = [x[:-1] for x in f.readlines()]


dirtree={}
loc = '/'

def writeloc(loc, tree, k, v):
    path = loc.split('/')
    dest = tree
    for elem in path:
        if elem == "":
            continue
        dest = dest[elem]
    dest[k]=v

i=1
while i<len(lines):
    line = lines[i]
    if line.startswith('$'):
        # listing, write in loc
        if line[2:].startswith('ls'):
            z=1
            while not lines[z+i].startswith('$'):
                v, k = lines[z+i].split()
                if v == 'dir':
                    v = {}
                else:
                    v = int(v)
                writeloc(loc[1:], dirtree, k, v)
                z+=1
                if z+i==len(lines):
                    break
            i+=z
        # changing dir
        elif line[2:].startswith('cd'):
            dest = line[5:]
            if dest == '..':
                loc = '/'.join(loc.split('/')[:-1])
            else:
                loc += '/' + dest
            i+=1
    else:
        pass


root = dirtree
@cache
def locsize(loc):
    path = loc.split('/')
    dest = root
    for elem in path:
        if elem == "":
            continue
        dest = dest[elem]
    if isinstance(dest, int):
        return dest
    else:
        return sum(locsize(f'{loc}/{child}') for child in dest.keys())

def enum_dir(loc):
    dirs = []
    path = loc.split('/')
    dest = root
    for elem in path:
        if elem == "":
            continue
        dest = dest[elem]
    if not isinstance(dest, int):
        dirs.append([enum_dir(f'{loc}/{child}') for child in dest] + [loc])
    return dirs

flatten=lambda l: sum(map(flatten,l),[]) if isinstance(l,list) else [l]
explore_us = flatten(enum_dir(''))

sizes = {x: locsize(x) for x in explore_us}
print(sum(v for k,v in sizes.items() if v<100000))

target = locsize('') - 70000000 + 30000000
print(min(x for x in sizes.values() if x>target))
