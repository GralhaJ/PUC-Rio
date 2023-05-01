def ProdutoPA(a1, r, n):
    produto = 1
    i = 1
    while i <= n:
        produto *= a1 + (i-1)*r
        i += 1
    print('O produto dos %d primeiros termos da PA é %d'%(n, produto))
a1 = int(input('Digite o primeiro termo da PG: '))
r = int(input('Digite a razão da PG: '))
n = int(input('Digite o número de termos da PG: '))
ProdutoPA(a1, r, n)
