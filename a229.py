#TLE QAQ
from time import time
def check(n,limit):
    a=n.count('1')
    b=n.count('0')
    if a<=limit and b<=limit:
        return True
    else:
        return False
def censor(x):
    sum=0
    value=True
    for i in x:
        if sum<0:
            value=False
            break
        if i == '1':
            sum+=1
        elif i == '0':
            sum-=1
    return value
while True:
    try:
        s=time()
        n=2*int(input()) # digits
        low=2**(n-1)
        high=2**n
        for i in range(low,high):
            thing=bin(i)[2:]
            if check(thing,n//2):
                if thing[-1]!=1:
                    if censor(thing):
                        thing=thing.replace('1','(')
                        thing=thing.replace('0',')')
                        # print(thing)
                        pass
        print(time()-s)
    except EOFError:
        break