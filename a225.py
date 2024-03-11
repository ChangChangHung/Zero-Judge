#50 min

def spliter(nl):
    a=nl[0][-1]
    value=[]
    splited_numbers=[]
    for item in nl:
        if item[-1]==a:
            splited_numbers.append(int(item))
        else:
            value.append(splited_numbers)
            splited_numbers=[int(item)]
        a=item[-1]
    value.append(splited_numbers)
    return value

while True:
    try:
        n=int(input())
    except:
        break
    answer=''
    numbers=input().split()
    numbers.sort(key=lambda x : x[-1])
    for item in spliter(numbers):
        item.sort(reverse=True)
        for thing in item:
            answer+=str(thing)+' '
    print(answer[:-1])