import random

def RPS():

    usuario = int(input('Escolha do usuário: '))

    computador = random.randint(1,3)

    if computador == 1:
        print('PEDRA!')
    if computador == 2:
        print('PAPEL!')
    if computador == 3:
        print('TESOURA!')

    if usuario == computador:
        print('EMPATE!')
        RPS()
    if usuario == 1 and computador == 2:
        print('COMPUTADOR VENCEU!')
    if usuario == 1 and computador == 3: 
        print('USUÁRIO VENCEU!')
    if usuario == 2 and computador == 1:
        print('USUÁRIO  VENCEU!')
    if usuario == 2 and computador == 3:
        print('COMPUTADOR VENCEU!')
    if usuario == 3 and computador == 1:
        print('COMPUTADOR VENCEU!')
    if usuario == 3 and computador == 2:
        print('USUÁRIO VENCEU!')

RPS()
