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
        for i in range(n):
            if palpite == lista_original[i]:
                lista_secreta[i] = palpite
        print(List_to_Str(lista_secreta))
    if lista_original == lista_secreta:
        break
if '_' in lista_secreta:
    print('Você perdeu!')
else:
    print('Você ganhou!')