#11 min
shit=input()
def Solution(l):
    check=[]
    answer=''
    for n in range(len(l)-1):
        check.append(l[n+1]-l[n])
    if len(set(check))==1:
        l.append(l[-1]+check[0])
    else:
        l.append(l[-1]*(l[1]//l[0]))
    for i in l:
        answer+=str(i)+' '
    return answer[:-1]
while True:
    try:
        numbers=list(map(int,input().split()))
        print(Solution(numbers))
    except EOFError:
        break