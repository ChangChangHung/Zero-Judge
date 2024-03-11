#6 min 
#數字翻轉
while True:
    try:
       n=input()
    except:
        break
    i=len(n)-1
    answer=''
    for x in range(len(n)):
        answer+=n[i]
        i-=1
    print(int(answer))

    print(int(''.join(reversed(input()))))