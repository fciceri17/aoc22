with open('day15.txt','r') as f:
    text=f.read().splitlines()

# text='''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3'''.splitlines()

target=2000000
detects = {}
for row in text:
    source,dest = row.split(':')
    src_x = source[12:].split(',')[0]
    src_y = source[12:].split('y=')[-1]
    dest_x = dest[24:].split(',')[0]
    dest_y = dest[24:].split('y=')[-1]
    detects[(int(src_x), int(src_y))] = (int(dest_x), int(dest_y))


no_beacon = set()
for src, dest in detects.items():
    rad = abs(src[0]-dest[0]) + abs(src[1]-dest[1])
    for y in range(-rad,rad+1):
        if y+src[1] == target:
            step = abs(y+rad) if y<=0 else abs(rad-y)
            for x in range(src[0]-step, src[0]+step+1):
                no_beacon.add((x,y+src[1]))

print(sum(1 for x in no_beacon if x[-1]==target if x not in detects.values()))