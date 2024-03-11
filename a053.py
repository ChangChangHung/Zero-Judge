#15 min
def solution(n):
    score=0
    plusindex=0
    plusmethods=[6,2,1,1]
    while n!=0 and score!=100:
        score+=plusmethods[plusindex//10]
        plusindex+=1
        n-=1
    print(score)
while True:
    try:
        solution(int(input()))
    except:
        break