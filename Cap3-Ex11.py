import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
andre = turtle.Turtle()

andre.hideturtle()      #hide turtle

size = 200
#draw a shape
for i in range(5):
    andre.forward(size)
    andre.right(144)

wn.mainloop()

