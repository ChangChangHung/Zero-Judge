#25 min
while True:
    try:
        n=int(input())
    except:
        break
    answer=''
    numbers=list(map(int,input().split()))
    numbers.sort()

    for i in range(n):
        answer+=str(numbers[i])+' '
    print(answer[:-1])