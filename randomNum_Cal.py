import random
num1=random.randint(1,100)
num2=random.randint(1,100)
ans=int(input(str(num1)+"-"+str(num2)+"="))
if(ans==num1-num2):
    print("맞았습니다.")
else:
    print("틀렸습니다.")
