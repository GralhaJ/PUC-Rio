import random

def Advinhaçao_0():
    computador = random.randint(1,1024)
    usuario = int(input('Qual seu palpite? '))
    for i in range(1,1023):
        if usuario == computador:
            print('0')
            print('Total de tentativas: %d'%i)
            break
        elif usuario < computador:
            print('1')
        elif usuario > computador:
            print('-1')
        
        usuario = int(input('Qual seu palpite? '))
    
def Advinhaçao_1():
    usuario = int(input('Digite um número entre 1 e 1023: ')) 
    computador = 512
    print(computador)
    for i in range(10):
        retorno = int(input(''))
        if retorno == -1:
            computador =  computador - 2**(10-i-2)
            print(computador)
        elif retorno == 1:
            computador = computador + 2**(10-i-2)
            print(computador)
        else:
            print('Número de tentativas: %d'%i)
            print('ACERTOU!')
            break
        
Escolha = int(input('Modo 1 ou Modo 0: '))
if Escolha == 1:
    Advinhaçao_1()
elif Escolha == 0:
    Advinhaçao_0()
else:
    print('Inválido')
     