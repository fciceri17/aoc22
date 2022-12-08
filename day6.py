with open('day6.txt','r') as f:
    message = list(f.read().strip())


def findseq(target):
    stack = message[:target]

    res=0
    for i, c in enumerate(message[target:]):
        if len(stack)==len(set(stack)):
            res=i
            break
        else:
            stack.pop(0)
            stack.append(c)
    return res+target

print(findseq(4))
print(findseq(14))