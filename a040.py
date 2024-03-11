#12 min
#阿姆斯壯數
def detector(number):
    output=0
    for n in number:
        output+=int(n)**len(number)
    return output
while True:
    try:
        min,max=map(int,input().split())
    except:
        break
    answer=''
    for i in range(min,max+1):
        if detector(str(i))==i:
            answer+=str(i)+' '
    if answer=='':
        print('none')
    else:
        print(answer[:-1])
