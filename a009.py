#3.5 min
while True:
    try:
        words=input()
        answer=''
        for i in words:
            answer+=chr(ord(i)-7)
        print(answer)
    except EOFError:
            break