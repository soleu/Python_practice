LX=int(input("큰 원의 중심좌표 x1 : "))
LY=int(input("큰 원의 중심좌표 y1 : "))
rL=int(input("큰 원의 반지름 : "))
SX=int(input("작은 원의 중심좌표 x2 : "))
SY=int(input("작은 원의 중심좌표 y2 : "))
rS=int(input("작은 원의 반지름 : "))


#그림 그리기
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.goto(LX,LY)
t.circle(rL)
t.goto(SX,SY)
t.circle(rS)

#원 안에 들어있는지
distance=((LX-SX)**2+(LY-SY)**2)**0.5
print(distance)
if distance<=(rL-rS):
    print("두번째 원은 첫번째 원의 내부에 있습니다.")
    
else:
    
    if distance>(rL-rS) and distance<=(rL+rS):
        print("두번째 원은 첫번째 원과 접하고 있습니다.")
    
    else:
        print("두번째 원은 첫번째 원의 외부에 있습니다.")
    
