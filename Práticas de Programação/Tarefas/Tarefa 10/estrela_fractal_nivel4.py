import turtle

t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(-150,0)
t.down()

def star(t, x):
    if x <= 10:
        return
    else:
        for i in range(5):
            t.fd(x)
            star(t, x/2)
            t.lt(216)

star(t, 160)






