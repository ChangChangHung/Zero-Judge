#20 min
while True:
    try:
        n=input()
    except:
        break
    yes=True
    if (len(n)%2==0):#inputted string is even
        index1=len(n)//2-1
        index2=index1+1
    else:
        index1=len(n)//2-1
        index2=index1+2
    for i in range(len(n)//2):
        if n[index1]!=n[index2]:
            print('no')
            yes=False
            break
        index1-=1
        index2+=1
    if yes==True:
        print('yes')
