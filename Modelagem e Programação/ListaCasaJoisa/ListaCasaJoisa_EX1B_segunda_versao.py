import random

def Price():
    
    x = random.randint(10,100)
    y = random.randint(10,100)
    z = random.randint(10,100)
    peso = random.randint(5,50)
    
    volume = x * y * z
    
    if volume > 125000 and x or y or z > 60:
        fdim = 10
    elif volume > 125000 and (x or y or z) < 60:
        fdim = 8
    elif volume > 27000:
        fdim = 5
    else:
        fdim = 2
    
    if peso > 25:
        fpeso = 5
    elif peso > 10 and peso <= 25:
        fpeso = 3
    else:
        fpeso = 1
    
    valor_calculado = (fdim + fpeso)*20
    
    print('altura = %.2f'%y)
    print('largura = %.2f'%x)
    print('profundidade = %.2f'%z)
    print('peso = %.2f'%peso)
    print('volume = %.2f'%volume)
    print('valor calculado = %.2f'%valor_calculado)

n = int(input('De quantos pacotes deseja calcular o preço de transporte: '))
i = 0
while i < n:
    Price()
    i += 1

