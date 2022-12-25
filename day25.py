import math
with open('day25.txt','r') as f:
    text=f.read().splitlines()
    
# text='''1=-0-2
# 12111
# 2=0=
# 21
# 2=01
# 111
# 20012
# 112
# 1=-1=
# 1-12
# 12
# 1=
# 122'''.splitlines()

out = []

cv = {
    '2':2,
    '1':1,
    '0':0,
    '-':-1,
    '=':-2
}
vc = {v:k for k,v in cv.items()}

def num_to_base(v, base):
    s=''
    while v>0:
        s+=(f'{v%base}')
        v//=base
    return s[::-1]

def decr(c, n):
    if c=='0':
        return '-' if n==1 else '='
    if c=='1':
        return '0' if n==1 else '-'
    return '1' if n==1 else '0'

def reverse_snafu(v):
    b5 = num_to_base(v,5)
    l = len(b5)
    if b5[0] in ('3','4'):
        l+=1
    s=['0' for _ in range(l)]
    for i,c in enumerate(b5[::-1]):
        if int(c)<=2:
            if s[i]=='0':
                s[i]=c
            elif s[i]=='1':
                if c=='2':
                    s[i+1]='1'
                    s[i]='='
                if c=='1':
                    s[i]='2'
        else:
            if c=='3':
               s[i+1]='1'
               s[i]=decr(s[i], 2)
            if c=='4':
                s[i+1]='1'
                s[i] = decr(s[i], 1)
    return ''.join(s[::-1])

def convert_snafu(s):
    v=0
    for i,c in enumerate(s[::-1]):
        p = 5**i
        v+=int(cv[c])*p
    return v
vs = [convert_snafu(row) for row in text]
reverse_snafu(12345)
print(reverse_snafu(sum(vs)))