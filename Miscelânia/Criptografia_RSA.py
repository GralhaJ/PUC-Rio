def totiente():
    return (primo_um - 1) * (primo_dois-1)  

def conversor_mensagem_ascii(mensagem):
    for c in mensagem:
        mensagem_ascii.append(ord(c))

def conversor_ascii_mensagem(mensagem_ascii):
    return chr(mensagem_ascii)

def codificar_letra(m, n):
    return (m**a) % n
 
def alg_euclides_estendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        mdc, x, y = alg_euclides_estendido(b % a, a)
        return mdc, y - (b // a) * x, x

def chave_privada(a, n):
    tupla = alg_euclides_estendido(a, totiente())
    return tupla[1]
    
def descodificar_letra(letra_cifrada, chave_p, n):
    return letra_cifrada ** chave_p % n 

def co_primo():
    for i in range(2,totiente()):
        if alg_euclides_estendido(i, totiente())[0] == 1:
            lista_primos.append(i)
    return lista_primos

lista_primos = []
mensagem_ascii = [] #criando um array
mensagem_criptografada = [] #criando um array
mensagem_descriptografada = [] #criando um array
mensagem_sem_ascii = [] #criando um array
mensagem = input("Digite a sua mensagem: ")
primo_um = int(input("Digite o primeiro número primo: "))
primo_dois = int(input("Digite o segundo número primo: "))
n = primo_um * primo_dois #tamanho do conjunto
print(co_primo())
a = int(input("Digite o A escolido: "))



# ---- CRIPTOGRAFANDO ----

conversor_mensagem_ascii(mensagem) # transformando em ASCII

for c in mensagem_ascii: # criptografando 
    mensagem_criptografada.append(codificar_letra(c, n))



# ---- GERANDO CHAVE PRIVADA ----

chave_privada = chave_privada(a,n)



# ---- DESCRIPTOGRAFANDO ----

for c in mensagem_criptografada:
    mensagem_descriptografada.append(descodificar_letra(c, chave_privada, n))



# ---- CONVERTENDO DE ASCII ----

for c in mensagem_descriptografada:
    mensagem_sem_ascii.append(conversor_ascii_mensagem(c))



print(mensagem)
print(mensagem_ascii)
print(mensagem_criptografada)
print(mensagem_descriptografada)
print(mensagem_sem_ascii)
