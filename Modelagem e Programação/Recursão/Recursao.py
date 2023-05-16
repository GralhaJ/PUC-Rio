def potencia(x,y):
    if y == 0:
        return 1 
    return x * potencia(x,y-1)

def fatorial(x):
    if x == 0:
        return 1
    return x * fatorial(x-1)

def fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)




    