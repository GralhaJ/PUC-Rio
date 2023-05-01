import random

par = 0
impar = 0

for i in range(10):
    usuario = int(input('Digite seu número: '))
    computador  = random.randint(0,10)
    soma = usuario + computador
    if soma%2 == 0:
        par = par + 1
    else:
        impar = impar + 1
            
if par == impar:
    print('EMPATE!')
elif par > impar:
    print('COMPUTADOR VENCEU!')
else:
    print('USUÁRIO VENCEU!')
    
        
