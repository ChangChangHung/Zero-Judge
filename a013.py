#no message
#關鍵點: 字典、zfill、abs、判斷式
romanNumber={
'I':	1,
'V':	5,
'X':	10,
'L':	50,
'C':	100,
'D':	500,
'M':	1000
}
def decode(word):
    value=[]
    a=0
    sum=0
    for x in word:
        value.append(romanNumber[x])
    short=value[0]
    for i in value:
        if short<i:
            value[a-1]=-short
        short=i
        a+=1
    for v in value:
        sum+=v
    return sum
def encode(answer):
    answer=str(answer).zfill(4)
    output=''
    output+='M'*int(answer[0])
    if answer[1]=='9':
        output+='CM'
    elif int(answer[1])>4:
        output+=f'D{"C"*(int(answer[1])-5)}'
    elif answer[1]=='4':
        output+='CD'
    else:
        output+='C'*int(answer[1])
    if answer[2]=='9':
            output+='XC'
    elif int(answer[2])>4:
        output+=f'L{"X"*(int(answer[2])-5)}'
    elif answer[2]=='4':
        output+='XL'
    else:
        output+='X'*int(answer[2])
    if answer[3]=='9':
        output+='IX'
    elif int(answer[3])>4:
        output+=f'V{"I"*(int(answer[3])-5)}'
    elif answer[3]=='4':
        output+='IV'
    else:
        output+='I'*int(answer[3])
    return output
while True:
    try:
        n=input()
        if n=="#":
            break
        a,b=n.split()
        answer=encode(abs(decode(a)-decode(b)))
        if answer=='':
            print("ZERO")
        else:
            print(answer)
    except:
        break