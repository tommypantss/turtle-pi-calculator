import turtle
import random

h = turtle.Pen()
h.speed(0)

text = turtle.Pen()
text.speed(0)
text.hideturtle()
text.pu()
text.goto(150,300)

h.hideturtle()

h.pu()
h.goto(-200, -200)
h.pd()

for i in range(4):
    h.forward(400)
    h.left(90)

h.pu()
h.goto(0,-200)
h.pd()
h.circle(200)

h.circle(200)
h.pu()

n = 0

goal = 0

while True:
    n+=1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2+y**2 <= 1:
        goal += 1
        h.color("red")
    else:
        h.color("blue")

    h.goto(200*x,200*y)
    h.dot(2)
    text.clear()
    text.write("π ≈"+ str(4*(goal/n)),font=("",30,"bold"),align='center')
