tel_list=dict()
while True:
    name=input("(입력모드)이름을 입력하시오 : ")
    if not name:
        break;
    tel=input("전화번호를 입력하시오 : ")
    tel_list[name]=tel
while True:
    search_name=input("(검색모드)이름을 입력하시오 : ")
    if search_name in tel_list:
        print(search_name,"의 전화번호는",tel_list[search_name],"입니다.")  

