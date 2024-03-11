#5 min
def calculate(op,a,b):
    if op==1:
        answer=a+b
    elif op==2:
        answer=a-b
    elif op==3:
        answer=a*b
    elif op==4:
        answer=a//b
    return answer
idontgiveashit=input()
while True:
    try:
        a,b,c=map(int,input().split())
        print(calculate(a,b,c))
    except EOFError:
        break
