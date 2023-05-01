def Soma_Sequencia(n):
    soma = 0
    i = 1
    while i <= n:
        soma += i * (2 * i + 1)
        i += 1
    print(soma)

n = int(input('Digite o número de termos da sequência: '))
Soma_Sequencia(n)