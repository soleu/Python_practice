money=int(input("투입한 돈: "))
price=int(input("물건 가격 : "))

change=money-price
print("거스름 돈 :",change)
coin500s=change//500
change=change%500
coin100s=change//100

print("500원 동전 개수 : ",coin500s)
print("100원 동전 개수 : ",coin100s)
