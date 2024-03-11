#3 min
while True:
    try:
        k=int(input())
    except EOFError:
        break
    print(( k*(k**2 + 5) ) // 6 + 1)