def Pre�o(peso, x, y, z):
    
    volume = x * y * z
    fpeso = 1
    fdim = 2
    
    if volume > 125000 and (x or y or z) > 60:
        fdim = 10
    elif volume > 125000 and (x or y or z) < 60:
        fdim = 8
    elif volume > 27000:
        fdim = 5
    
    if peso > 25:
        fpeso = 5
    elif peso > 10 and peso <= 25:
        fpeso = 3
    
    valor_calculado = (fdim + fpeso)*20
    
    print('altura = %.2f'%y)
    print('largura = %.2f'%x)
    print('profundidade = %.2f'%z)
    print('peso = %.2f'%peso)
    print('volume = %.2f'%volume)
    print('valor calculado = %.2f'%valor_calculado)
    
peso = float(input('Digite o peso do pacote do transporte: '))
x = float(input('Digite a largura do pacote: '))
y = float(input('Digite a altura do pacote: '))
z = float(input('Digite a profundidade do pacote: '))
Pre�o(peso, x, y, z)