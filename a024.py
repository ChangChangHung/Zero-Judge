#38 min 
#最大公因數(GCD)
while True:
    try:
        n=sorted(input().split())
    except:
        break
    a,b=int(n[0]),int(n[1])
    answers=[]
    sum=1
    def factor(n):
        factors=[1]
        if n==1:
            return factors
        i=2
        for a in range(n):
            if n%i==0:
                factors.append(i)
                n=n//i
            else:
                i+=1
            if i>n:
                break
        return factors
    a,b=map(factor,[a,b])
    for item in a:
        if item in b:
            answers.append(item)
            b.remove(item)
    for answer in answers:
        sum*=answer
    print(sum)