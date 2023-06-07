import turtle

t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(-600,0)
t.down()
t.width(2)

def star(t, x):
    if x <= 10:
        return
    else:
        for i in range(5):
            t.fd(x)
            star(t, x/2)
            t.lt(216)
            if x <= 640:
                t.color('blue')
            elif x<=320:
                t.color('orange')
            elif x <= 160:
                t.color('red')
            elif x <= 80:
                t.color('green')
            elif x<= 40:
                t.color('pink')
            elif x <= 20:
                t.color('purple')
        
star(t, 640)






