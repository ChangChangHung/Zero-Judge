#155 min
def Solution(a,b):
    if a**(1/2)%1==0:
        a-=1
    while True:
        if a**(1/2)%1==0:
            break
        else:
            a-=1
    while True:
        if b**(1/2)%1==0:
            break
        else:
            b-=1
    a=a**(1/2)
    b=b**(1/2)
    a=(a*(a+1)*(2*a+1))/6
    b=(b*(b+1)*(2*b+1))/6
    return int(b-a)
n=int(input())
for i in range(1,n+1):
    a=int(input())
    b=int(input())
    print(f'Case {i}: {Solution(a,b)}')