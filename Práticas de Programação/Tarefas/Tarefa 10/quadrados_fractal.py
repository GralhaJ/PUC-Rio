import turtle

t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(-100,-100)
t.down()

def square(t, x):
    for i in range(4):
        t.fd(x)
        t.lt(90)

    x  =  (x - 20)/2
    if x < 20:
        return
    else:
        for i in range(4):
            square(t, x)
            t.fd(2*x+20)
            t.lt(90)

square(t, 300)
