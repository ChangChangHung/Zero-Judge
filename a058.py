#19 min
n=int(input())
mot=[]
while True:
    try:
        mot.append(int(input())%3)
    except :
        break
print(mot.count(0),mot.count(1),mot.count(2))
