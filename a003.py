#2.5 min
fortune=['普通','吉','大吉']
while True:
    try:
        M,D=map(int,input().split())
        S=(M*2+D)%3
        print(fortune[S])
    except EOFError:
        break