from turtle import *


speed(30)
width(7)
color("purple")

forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)

#door
color("red")
left(90)

forward(120)
right(90)

forward(60)
right(90)

forward(120)

penup()
goto(200,200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#maiking the windows

penup()
goto(175,175)
pendown()
right(60)
forward(50)
left(90)
forward(45)
left(90)
forward(50)
left(90)
forward(45)

penup()
goto(15,175)
pendown()
right(90)
forward(50)
right(90)
forward(45)
right(90)
forward(50)
right(90)
forward(45)




exitonclick()