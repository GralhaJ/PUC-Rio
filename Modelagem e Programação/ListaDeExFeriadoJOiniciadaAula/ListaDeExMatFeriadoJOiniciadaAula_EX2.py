def PG(a1, r, n):
    i = 0
    while i < n:
        print('a%d = %d'%(i + 1, a1 * r ** i))
        i += 1
    
a1 = int(input('Digite o primeiro termo da PG: '))
r = int(input('Digite a razão da PG: '))
n = int(input('Digite o número de termos da PG: '))
PG(a1, r, n)