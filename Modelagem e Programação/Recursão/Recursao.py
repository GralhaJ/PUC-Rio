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

def prntCaract(s):
    if s == '':
        return 
    print(s[0])
    return prntCaract(s[1:])

def prntCaractInv(s):
    if s == '':
        return
    print(s[-1])
    return prntCaractInv(s[0:-1])

def qntdCaracString(s):
    if s == '':
        return 0
    return 1 + qntdCaracString(s[1:])

def qntdVogaisString(s):
    if s == '':
        return 0
    vogais = 'aeiouAEIOU'
    if s[0] in vogais:
        return 1 + qntdVogaisString(s[1:])
    return qntdVogaisString(s[1:])

def qntdCaracEspString(s, c):
    if s == '':
        return 0
    if c == s[0]:
        return 1 + qntdCaracEspString(s[1:], c)
    return qntdCaracEspString(s[1:], c)

def PertenceString(s, c):
    if s == '':
        return False
    if s[0] == c:
        return True
    return PertenceString(s[1:], c)
    
def aPorArroba(s):
    if s == '':
        return s
    if 'a' == s[0]:
        return '@' + aPorArroba(s[1:])
    return s[0:1] + aPorArroba(s[1:])

def somaLista(lista):
    soma = 0
    for elemento in lista:
        if type(elemento) == list:
            if type(elemento) != str:
                soma += somaLista(elemento)
        else:
            if type(elemento) != str:
                soma += elemento
    return soma


    
