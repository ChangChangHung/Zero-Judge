#6 min
while True:
    try:
        numbers=list(map(int,input().split()))
        a=numbers.pop(0)
        if sum(numbers)/a>59:
            print('no')
        else:
            print('yes')
    except:
        break