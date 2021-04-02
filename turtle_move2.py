import turtle
t=turtle.Turtle()
t.shape("turtle")

s=turtle.textinput("","숫자를 입력하시오 :")
x=int(s)

t.penup() #선이 안생기게
t.goto(100,100)
t.write("거북이가 여기로 오면 양수입니다.")
t.goto(100,0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100,-100)
t.write("거북이가 여기로 오면 음수입니다.")
t.goto(0,0)


t.pendown()
if(x>0):
    t.goto(100,100)
if(x==0):
    t.goto(100,0)
if(x<0):
    t.goto(100,-100)
    
