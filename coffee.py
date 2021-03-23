americano_price=2000
cafelatte_price=3000
capucino_price=3500

americanos= int(input("아메리카노 판매 개수 : "))
cafelattes =int(input("카페라테 판매 개수 : "))
capucinos = int(input("카푸치노 판매 개수 :"))

total_price=americanos*americano_price
total_price+=cafelattes*cafelatte_price
total_price+=capucinos*capucino_price

print("총 매출은 ",total_price,"원 입니다.")
