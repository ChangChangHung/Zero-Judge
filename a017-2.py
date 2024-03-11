#144 min
#注意 /在題目中 是整除不是一般除法 因為測資有誤
def calculate(formula):
    answers=formula
    conditions=['*','/','%']
    conditions2=['+','-']
    while True:
        condition=5
        condition2=5
        for item in answers:
            if item in conditions:
                condition=conditions.index(item)
                break
        if condition==0:
            index0=formula.index('*')
            answer=int(formula[index0-1])*int(formula[index0+1])
        elif condition==1:
            index0=formula.index('/')
            answer=int(formula[index0-1])//int(formula[index0+1])
        elif condition==2:
            index0=formula.index('%')
            answer=int(formula[index0-1])%int(formula[index0+1])
        else:
            for item in answers:
                if item in conditions2:
                    condition2=conditions2.index(item)
                    break
            if condition2==0:
                index0=formula.index('+')
                answer=int(formula[index0-1])+int(formula[index0+1])
            elif condition2==1:
                index0=formula.index('-')
                answer=int(formula[index0-1])-int(formula[index0+1])
            else:
                break
        for i in range(3):
            answers.pop(index0-1)
        answers.insert(index0-1,answer)
    return answers
while True:
    try:
        equation=input().split()
    except:
        break

    while True:
        try:
            bpar=equation.index(')')
            x=bpar
        except:
            break
        for i in range(bpar+1):
            if equation[x]=='(':
                fpar=x
                break
            x-=1
        value=calculate(equation[fpar+1:bpar])[0]
        for i in range(bpar-fpar+1):
            equation.pop(fpar)
        equation.insert(fpar,str(value))
    print(int(calculate(equation)[0]))