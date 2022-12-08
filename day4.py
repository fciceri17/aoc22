with open('day4.txt','r') as f:
    pairs=[[[int(a) for a in y.split('-')] for y in x.strip().split(',')] for x in f.readlines()]

s=0
s1=0
for p0, p1 in pairs:
    if p0[0]>=p1[0] and p0[1]<=p1[1] or p1[0]>=p0[0] and p1[1]<=p0[1]:
        s+=1
    if p0[0]<=p1[1] and p0[1]>=p1[0] or p1[0]<=p0[1] and p1[0]>=p0[1]:
        s1+=1
print(s, s1)