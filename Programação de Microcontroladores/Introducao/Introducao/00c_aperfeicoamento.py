from json import load
from turtle import *

speed(0)
# Copie as funções que você fez na Implementação aqui embaixo
def desenha_retangulo(x, y, comprimento, altura, cor):
    fillcolor(cor)
    up()
    goto(x, y)
    down()
    begin_fill()
    for i in range(2):
        fd(comprimento)
        rt(90)
        fd(altura)
        rt(90)
    end_fill()
    return
    
def desenha_circulo(x, y, raio, cor):
    fillcolor(cor)
    up()
    goto(x, y-raio)
    down()
    begin_fill()
    circle(raio)
    end_fill()
    return
        
def desenha_poligono(lista_pontos, cor):
    fillcolor(cor)
    up()
    goto(lista_pontos[0]["x"], lista_pontos[0]["y"])
    down()
    begin_fill()
    for elemento in lista_pontos:
        goto(elemento["x"], elemento["y"])
    goto(lista_pontos[0]["x"], lista_pontos[0]["y"])
    end_fill()
    return


# Faça a primeira parte do Aperfeiçoamento aqui

def desenha_bandeira(dicionario_do_pais):
    for item in dicionario_do_pais["elementos"]:
        if item["tipo"] == "retângulo":
            desenha_retangulo(item["x"], item["y"], item["comprimento"], item["altura"], item["cor"])
        if item["tipo"] == "círculo":
            desenha_circulo(item["x"], item["y"], item["raio"], item["cor"])
        if item["tipo"] == "polígono":
            desenha_poligono(item["pontos"], item["cor"])
    
    return

def clica(x, y):
    pais = textinput("Aperfeiçoamento","Qual país?")
    for elemento in lista_de_paises:
        if elemento["nome"] == pais:
            desenha_bandeira(elemento)
    

lista_de_paises = load(open('paises.json', encoding="UTF-8"))
desenha_bandeira(lista_de_paises[0])

# Faça a segunda parte do Aperfeiçoamento aqui

onscreenclick(clica)

# O desafio deve ser feito diretamente no JSON, não aqui!


# Mantém a janela do Turtle aberta
mainloop()