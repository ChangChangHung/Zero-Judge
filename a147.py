#29 min
while True:
    n=int(input())
    if n==0:
        break
    answer=''
    for i in range(1,n):
        if i%7!=0:
            answer+=str(i)+' '
    print(answer[:-1])