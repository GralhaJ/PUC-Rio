def SomaPA(a1, r, n):
    soma = n*(2*a1 + (n-1)*r)/2
    print('A soma dos %d primeiros termos da PA é %d'%(n, soma))
    
a1 = int(input('Digite o primeiro termo da PG: '))
r = int(input('Digite a razão da PG: '))
n = int(input('Digite o número de termos da PG: '))
SomaPA(a1, r, n)