import turtle


def make_window (cor, ttle):
    w = turtle.Screen()
    w.bgcolor(cor)
    w.title(ttle)
    return w

def draw_star (t, length):
    for i in range(5):
        t.forward(length)
        t.right(144)

def make_turtle(colr, sz):
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

def draw_5star(t, lenght):
    for i in range(5):
        draw_star(t, lenght)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()

wn = make_window("lightgreen", "star")
andre = make_turtle("blue",3)
draw_5star(andre,100)

wn.mainloop()




