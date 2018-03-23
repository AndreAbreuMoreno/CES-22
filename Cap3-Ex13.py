import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
andre = turtle.Turtle()

andre.shape("turtle")
andre.color("blue")
andre.pensize(3)
andre.stamp()
andre.penup()
size1 = 100
size2 = 10
size3 = 20
size4 = size1 + size2 + size3

for i in range(12):
    andre.forward(size1)
    andre.pendown()
    andre.forward(size2)
    andre.penup()
    andre.forward(size3)
    andre.stamp()
    andre.right(180)
    andre.forward(size4)
    andre.right(150)


wn.mainloop()



