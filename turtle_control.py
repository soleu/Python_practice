import turtle
t=turtle.Turtle()
t.width(3) #선 두께 설정
t.shape("turtle")
t.shapesize(3,3)#거북이 확대

while True:
    control=input("명령을 입력하시오 :")
    if(control=="l" or control=="L"):
        t.left(90)
        t.fd(100)
    if(control=="r" or control=="R"):
        t.right(90)
        t.fd(100)


    
