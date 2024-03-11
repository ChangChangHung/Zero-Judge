#20 min
# an a(n-1)+a(n-1)-a(n-2)+2
# =2*a(n-1)-a(n-2)+2

# a1=2
# a2=4
# a3=2*4-2+2=8
# a4=2*8-4+2=14


# 2   4   8   14   22    get index of this list
#   2   4   6    8       generate the plus list
#     2   2   2          d=2
while True:
    try:
        n=int(input())
        pluslist=[]
        number=2
        answer=2
        for i in range(n-1):
            pluslist.append(number)
            number+=2
        for plus in pluslist:
            answer+=plus
        print(answer)
    except EOFError:
        break