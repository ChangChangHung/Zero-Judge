#78 min
import string
upperalphabet=string.ascii_uppercase
alphabet={
"A" : 10 , "B" : 11 , "C" : 12 , "D" : 13 , "E" : 14 , "F" : 15 ,
"G" : 16 , "H" : 17 , "I" : 34 , "J" : 18 , "K" : 19 , "L" : 20 ,
"M" : 21 , "N" : 22, "O" : 35 , "P" : 23 , "Q" : 24 , "R" : 25 ,
"S" : 26 , "T" : 27 , "U" : 28 , "V" : 29 ,"W" : 32 , "X" : 30 ,
"Y" : 31 , "Z" : 33 }
while True:
    try:
        lastninenumber=input()# 9 digits
        check=lastninenumber[8]
        answer=[]
        answerstr=''
        def find_first_letter(letterindex,lastninenumber):
            id=letterindex+lastninenumber
            time=9
            sum=int(id[0])
            for i in range(1,10):
                sum+=int(id[i])*time
                time-=1
            check=10-int(str(sum)[-1:])
            if check==10:
                check=0#檢查碼僅有一位，若其為10則為0
            if str(check)==id[10]:
                return True
        for letter in upperalphabet:
            if find_first_letter(str(alphabet[letter]),lastninenumber):
                answer.append(letter)
        for letter in answer:
            answerstr+=letter
        else:
            print(answerstr)
    except EOFError:
        break