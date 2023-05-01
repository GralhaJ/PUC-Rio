def MenorPA(a1, r, n):
    i = 1
    while i <= n:
        if a1 + (i-1)*r > 200:
            print(i)
            break
        i += 1
        
        
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = int(input('Digite o número de termos da PA: '))
MenorPA(a1, r, n)