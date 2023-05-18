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

def qntdAlg(n):
    if n < 10:
        return 1
    return 1 + qntdAlg(n//10)

def qntdAlgPares(n):
    if n < 10:
        if n % 2 == 0:
            return 1
        return 0
    if n % 2 == 0:
        return 1 + qntdAlgPares(n // 10)
    return qntdAlgPares(n // 10)
    
def exibeBomDia(n):
    if n == 0:
        return
    print('Bom dia!')
    return exibeBomDia(n-1)

def exibeMsn(msn,n):
    if n == 0:
        return
    print(msn)
    return exibeMsn(msn,n-1)




    
