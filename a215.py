#11min
while True:
    try:
        a,b=map(int,input().split())
        c=a
    except:
        break
    sum=0
    while True:
        sum+=a
        a+=1
        if sum>b:
            break
    print(a-c)