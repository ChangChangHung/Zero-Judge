#151 min
#remove:[1,2,1,3,3] --->[1,2,'del',3.3] --->.remove('del')
#pop: [1,2,3,4,5].pop(0)--->[1,2,3,4]
#(5*(3+5)): first find ')', and then go backward to find ')'
#for item in list is actually index=0 then index+=1 and the item is list[index] so if we remove item in list, it, the loop will end earlier. And there will happen some errors.
operator1=['+','-']
operator2=['*','/','%']
def calculating(a,b,c):
    a=int(a)
    b=int(b)
    if c==operator2[0]:
        return (a*b)
    elif c==operator2[1]:
        return (a/b)
    elif c==operator2[2]:
        return (a%b)
    elif c==operator1[0]:
        return (a+b)
    elif c==operator1[1]:
        return (a-b)
    
def calculate(x):
    for nothing in range(x.count(operator2[0])+x.count(operator2[1])+x.count(operator2[2])):
        for i in x:
            if i in operator2:
                a=x.index(i)
                fn=x[a-1]
                bn=x[a+1]
                x[a-1]='del'
                x[a+1]='del'
                x.remove(i)
                x.remove('del')
                x.remove('del')
                x.insert(a-1,calculating(fn,bn,i))
    for no in range(x.count(operator1[0])+x.count(operator1[1])):
        for i in x:
            if i in operator1:
                a=x.index(i)
                fn=x[a-1]
                bn=x[a+1]
                x[a-1]='del'
                x[a+1]='del'
                x.remove(i)
                x.remove('del')
                x.remove('del')
                x.insert(a-1,calculating(fn,bn,i))
    return int(x[0])
if __name__=='__main__':
    while True:
        try:
            n=input().split()
        except EOFError:
            break
        for r in range(n.count('(')):
            bpar=n.index(')')
            findbpar=bpar
            while True:
                if n[findbpar]=='(':
                    fpar=findbpar
                    break
                findbpar-=1
            insertindex=fpar
            bpar=n.index(')')
            parentheses=[]
            ran=bpar-fpar-1
            for i in range(ran):
                parentheses.append(n[fpar+1])
                fpar+=1
            for i in range(ran+2):
                n.pop(insertindex)
            n.insert(insertindex,calculate(parentheses))
        print(calculate(n))