import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
andre = turtle.Turtle()

andre.color("blue")

size = 100
#draw an equilateral triagle
for i in range(3):
   andre.forward(size)        # Move tess along
   andre.right(120)           #  ...  and turn her

andre.right(90)
andre.penup()
andre.forward(2*size)
andre.left(90)
andre.pendown()

#draw a square
for i in range(4):
   andre.forward(size)
   andre.right(90)


andre.penup()
andre.forward(2*size)
andre.pendown()

#draw a hexagon
for i in range(6):
   andre.forward(size)
   andre.right(60)

andre.left(90)
andre.penup()
andre.forward(3*size)
andre.right(90)
andre.pendown()

#dram an octagon
for i in range(8):
   andre.forward(size)
   andre.right(45)


wn.mainloop()