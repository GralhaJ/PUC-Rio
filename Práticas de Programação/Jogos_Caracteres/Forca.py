def List_to_Str(lista):
    string = ' '
    return string.join(lista)
    
palavra = input('Qual a palavra secreta? ')
n = len(palavra)
lista_original = list(palavra)
lista_secreta = list(n*'_')
for i in range(n):
    palpite = input('Qual seu palpite? ')
    if i <= n:
        for k in range(n):
            if palpite == lista_original[k]:
                lista_secreta[k] = palpite
        print(List_to_Str(lista_secreta))
    if lista_original == lista_secreta:
        break
    print('Tentativas restantes: %d'%(n-1-i))
if '_' in lista_secreta:
    print('Você perdeu!')
else:
    print('Você ganhou!')