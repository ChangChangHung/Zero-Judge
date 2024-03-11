#7 min
def Solution(a,b,c):
    try:
        answer1=int((-b+(b**2-4*a*c)**0.5)/(2*a))
        answer2=int((-b-(b**2-4*a*c)**0.5)/(2*a))
        if answer1==answer2:
            print(f'Two same roots x={answer1}')
        else:
            print(f'Two different roots x1={answer1} , x2={answer2}')
    except:
        print('No real root')

while True:
    try:
        a,b,c=map(int,input().split())
        Solution(a,b,c)
    except EOFError:
        break
