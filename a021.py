#18 min
while True:
    try:
        n=input().replace(' ','')
    except:
        break
    algorithms=['+','-','*','/']
    a,b=0,0
    for i in range(4):
        if algorithms[i] in n:
            algotithm=i
            a,b=n.split(algorithms[i])
            break
    a,b=map(int,[a,b])
    if algotithm==0:
        print(a+b)
    elif algotithm==1:
        print(a-b)
    elif algotithm==2:
        print(a*b)
    elif algotithm==3:
        print(a//b)