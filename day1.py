with open('day1.txt','r') as f:
    text=f.read()

v=0
supplies = []
for entry in text.split('\n'):
    if len(entry)==0:
         supplies.append(v)
         v=0
    else:
        v+=int(entry)
print(max(supplies))
print(sum(sorted(supplies)[::-1][:3]))