#23 min
while True:
    try:
        n=int(input())
    except:
        break
    fn=(n+1)*n//2
    gn=(2+n)*(1+n)*n//6
    print(fn,gn)