def Valida_CPF():
    CPF = input('Digite seu CPF: ')

    lista_1 = []
    digitos = '0123456789'
    soma_1 = 0
    soma_2 = 0

    for i in range(14):
        if CPF[i] in digitos:
            lista_1.append(CPF[i])
            
    for i in range(9):
        soma_1 += (10 - i) * int(lista_1[i]) 
        
    if soma_1 % 11 < 2:
        digito_1 = 0
    else:
        digito_1 = 11 - soma_1 % 11
        
    lista_2 = lista_1[0:9]
    lista_2.append(digito_1)
        
    for i in range(10):
        soma_2 += (11 - i) * int(lista_2[i])
        
    if soma_2 % 11 < 2:
        digito_2 = 0
    else:
        digito_2 = 11 - soma_2 % 11
        
    if digito_1 == int(lista_1[9]) and digito_2 == int(lista_1[10]):
        return True
    else:
        return False
    
print(Valida_CPF())
        
