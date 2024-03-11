#19 min
while True:
    try:
        word=input().lower()
    except:
        break
    new=''.join(filter(str.isalpha,word))
    alphas=set(new)
    cunt=[]
    for alpha in alphas:
        cunt.append(new.count(alpha)%2)
    if cunt.count(1)>1:
        print('no...')
    else:
        print('yes !')