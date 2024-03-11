#16 min
while True:
    try:
        word=input()
        answer=''
        for i in range(len(word)-1):
            answer+=str(abs(ord(word[i+1])-ord(word[i])))
        print(answer)
    except EOFError:
        break