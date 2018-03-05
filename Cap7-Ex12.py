
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

def make_a_move(t,x,y):
    t.left(x)
    t.forward(y)

wn = make_window("lightgreen", "house")
andre = make_turtle("blue", 3)

move = [(90,100),(90,100),(90,100),(135,100*2**0.5),(90,50*2**0.5),
        (90,50*2**0.5),(90,100*2**0.5),(225,100)]

for (x,y) in move:
    print (x,y)
    make_a_move(andre,x,y)

wn.mainloop()