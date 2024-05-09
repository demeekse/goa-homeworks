from turtle import *
width(7)
speed(6)


color("purple")


forward(200)
right(90)

forward(300)
right(90)

forward(200)
right(90)

forward(300)
right(90)


#now time for door

penup()
goto(145, -300)
pendown()

color("green")
begin_fill()
left(90)
forward(150)

left(90)
forward(80)

left(90)
forward(150)
end_fill()

#roof
color("purple")

penup()
goto(200, 0)
pendown()
begin_fill()
left(210)
forward(180)

left(115)
forward(185)
end_fill()
#roof ended
#start windows
penup()
goto(130, -100)
pendown()
color("blue")
right(145)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)   #end of 1 window
# second window

penup()
goto(70, -100)
pendown()

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)



exitonclick()