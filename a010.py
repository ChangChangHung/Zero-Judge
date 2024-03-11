#55 min
#關鍵點: 
#list.count(a)得知在list中有幾個a、二行list分別儲存數字和數量、質數另外處理、

#輸入與宣告變量
n=int(input())
factor=[]
i=2
answer=''
ans1=[]
ans2=[]
#因數分解
for a in range(2,n):
    if i>n:
        break
    if n%i==0:
        n=n//i
        factor.append(i)
    else:
        i+=1
#計算因數重複次數
for number in factor:
    if (number in ans1)!=True:
        ans1.append(number)
        ans2.append(factor.count(number))
#輸出     
for i in range(len(ans1)):
    if ans2[i]==1:
        answer+=str(ans1[i])+' * '
    else:
        answer+=str(ans1[i])+'^'+str(ans2[i])+' * '
if answer=='':#質數特別處理
    print(n)
else:
    print(answer[:-3])