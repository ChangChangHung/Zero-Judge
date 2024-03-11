#no message
while True:
    try:
        row,column=input().split()
    except EOFError:
        break
    data=''
    for i in range(int(row)):
        data+=input()
        data=data.replace(" ",'')
    for r in range(int(column)):
        answer=''
        i=r
        for a in range(r,int(row)+r):
            answer+=data[i]+' '
            i+=int(column)
        answer=answer[:-1]
        print(answer)