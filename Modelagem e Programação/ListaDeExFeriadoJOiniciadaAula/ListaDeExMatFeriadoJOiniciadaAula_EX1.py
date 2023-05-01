def PA(a1, a2, n):
    r = a2 - a1
    i = 1
    while i <= n:
        print('a%d = %d'%(i, a1 + (i-1)*r))
        i += 1

a1 = int(input('Digite o primeiro termo da PA: '))
a2 = int(input('Digite o segundo termo da PA: '))
n = int(input('Digite o número de termos da PA: '))
PA(a1, a2, n)