def Menor_n_Soma(a1, a4):
    soma = 0
    r = (a4 - a1) / 3
    i = 1
    while 1 > 0:
        soma = i*(2*a1 + (i-1)*r)/2
        if soma > 1000:
            print(i)
            break
        i += 1
        
a1 = int(input('Digite o primeiro termo da PA: '))
a4 = int(input('Digite o quarto termo da PA: '))
Menor_n_Soma(a1, a4)