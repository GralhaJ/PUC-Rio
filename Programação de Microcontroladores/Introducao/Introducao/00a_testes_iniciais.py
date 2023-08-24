from turtle import *

up()
goto(-50,250)
down()
for i in range(2):
    fd(100)
    rt(90)
    fd(50)
    rt(90)
    # Desenhe o que foi solicitado no enunciado do PDF aqui embaixo
up()
goto(150,-50)
down()
for i in range(3):
    fd(100)
    lt(120)

up()
goto(0,-200)
down()
circle(50)

up()
goto(-250,0)
down()
for i in range(50):
    fd(i*0.7)
    rt(18)

def imprime_coordenadas(x, y):
    up()
    goto(x, y)
    print("x = ",x)
    print("y = ",y)
    write("x = %.1f, y = %.1f"%(x, y))
    
onscreenclick(imprime_coordenadas)

    
    
    
    
    
    
    
    
    
    # Mantém a janela do Turtle aberta
mainloop()