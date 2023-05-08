senha_original = input('Digite a senha a ser criptografada: ')
print(senha_original)
n = len(senha_original)
lista_senha_original = list(senha_original)
lista_criptografada = []
for i in range(n):
    k = ord(lista_senha_original[i]) + 3
    if ord(lista_senha_original[i]) + 3 > 122:
        lista_criptografada.append(chr(k % 75))
    else:
        lista_criptografada.append(chr(ord(lista_senha_original[i]) + 3))
    senha_criptografada = ''.join(lista_criptografada)
print(senha_criptografada)

    
    
    
    