#26 min 
#二進位制轉換
while True:
    try:
        n=int(input())
        short=n
    except:
        break
    answer=''
    times=0
    while True:
        if short<=0:
            break
        short=short//2
        times+=1
        
    for i in range(times):
        if n%2==1:
            answer='1'+answer
            n-=1
            n=n/2
        else:
            answer='0'+answer
            n=n/2
    print(answer)