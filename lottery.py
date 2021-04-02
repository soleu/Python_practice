import random
lottery=random.randint(0,99)
digit1=lottery//10
digit2=lottery%10
money=0

pNum=int(input("복권번호를 입력하시오(0~97) : "))
pDigit1=pNum//10
pDigit2=pNum%10

if(pDigit1==digit1 or pDigit2==digit1 ):
         money+=50
if(pDigit1==digit2 or pDigit2==digit2):
         money+=50

print("당첨번호는 "+str(lottery)+"입니다.")
print("상금은 "+str(money)+"만원입니다.")
