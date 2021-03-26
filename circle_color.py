import turtle
t=turtle.Turtle()
t.shape("turtle")

color1=input("색상 #1을 입력하시오:")
color2=input("색상 #2을 입력하시오:")
color3=input("색상 #3을 입력하시오:")

t.fillcolor(color1)
t.begin_fill()
t.circle(50)
t.end_fill()
t.fd(100)

t.fillcolor(color2)
t.begin_fill()
t.circle(50)
t.end_fill()
t.fd(100)

t.fillcolor(color3)
t.begin_fill()
t.circle(50)
t.end_fill()


