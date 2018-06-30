
import turtle



def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr,sz):
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

def draw_figure(t,x,y):
    t.left(x)
    t.forward(y)

wn = make_window("lightgreen", "house")
andre = make_turtle("blue", 3)

andre.left(90)
andre.penup()
andre.forward(300)
andre.right(90)
andre.pendown()

#draw the figure1

move = [(270,100),(90,100),(90,100),(45,50*2**0.5),(90,50*2**0.5),
        (135,100)]

for (x,y) in move:
    draw_figure(andre,x,y)

andre.penup()
andre.forward(200)
andre.pendown()

#draw the figure2

move = [(270,100),(270,100),(270,100),(315,50*2**0.5),(270,50*2**0.5),
        (225,100),(135,100*2**0.5)]

for (x,y) in move:
    draw_figure(andre,x,y)

andre.penup()
andre.right(90)
andre.forward(300)
andre.left(45)
andre.pendown()


#draw the figure3

move = [(225,50*2**0.5),(270,100*2**0.5),(270,100*2**0.5),(270,50*2**0.5),(315,100),
        (270,100),(270,100),(270,100)]

for (x,y) in move:
    draw_figure(andre,x,y)

andre.penup()
andre.forward(200)
andre.right(45)
andre.pendown()


#draw the figure4
andre.left(180)
move = [(90,50*2**0.5),(90,100*2**0.5),(90,50*2**0.5),(135,100),(270,100),
        (315,50*2**0.5),(270,50*2**0.5),(225,100),(135,100*2**0.5),(135,100),(135,100*2**0.5)]

for (x,y) in move:
    draw_figure(andre,x,y)

wn.mainloop()