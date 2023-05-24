import turtle
import eixos_turtle
import random

letra = 'Este samba Vai pra Dorival Caymmi João Gilberto e Caetano Veloso Vamo lá O Rio de Janeiro continua lindo O Rio de Janeiro continua sendo O Rio de Janeiro fevereiro e março Alô alô Realengo aquele abraço Alô torcida do Flamengo aquele abraço Alô alô Realengo aquele abraço Alô torcida do Flamengo aquele abraço Chacrinha continua balançando a pança E buzinando a moça e comandando a massa E continua dando as ordens no terreiro Alô alô seu Chacrinha velho guerreiro Alô alô Terezinha Rio de Janeiro Alô alô seu Chacrinha velho palhaço Alô alô Terezinha aquele abraço Alô moça da favela aquele abraço Todo mundo da Portela aquele abraço Todo mês de fevereiro aquele passo Alô Banda de Ipanema aquele abraço Meu caminho pelo mundo eu mesmo traço A Bahia já me deu régua e compasso Quem sabe de mim sou eu Aquele abraço Pra você que me esqueceu Aquele abraço Alô Rio de Janeiro aquele abraço Todo o povo brasileiro aquele abraço O Rio de Janeiro continua lindo O Rio de Janeiro continua sendo O Rio de Janeiro fevereiro e março Alô alô Realengo Alô torcida do Flamengo aquele abraço Alô alô Realengo aquele abraço Alô torcida do Flamengo aquele abraço Chacrinha continua balançando a pança E buzinando a moça e comandando a massa E continua dando as ordens no terreiro Alô alô seu Chacrinha velho guerreiro Alô alô Terezinha Alô alô seu Chacrinha Alô alô Terezinha aquele abraço Alô moça da favela aquele abraço Todo mundo da Portela aquele abraço Todo mês de fevereiro aquele passo Alô Banda de Ipanema aquele abraço Meu caminho pelo mundo eu mesmo traço A Bahia já me deu graças a Deus régua e compasso Quem sabe de mim sou eu é claro aquele abraço Pra você que me esqueceu Aquele abraço Alô Rio de Janeiro todo mundo aquele abraço Todo o povo brasileiro aquele abraço Todo mês de fevereiro aquele abraço Alô moça da favela aquele abraço Todo mundo da Portela e do Salgueiro e todo o Rio de Janeiro aquele abraço E todo mês de fevereiro e todo povo brasileiro aquele abraço Alô minha nega samba aquele abraço E alô alô da pipoca aquele abraço E todo Rio de Janeiro aquele abraço E todo povo brasileiro todo povo brasileiro Todo povo brasileiro todo povo brasileiro Todo povo brasileiro aquele abraço Aquele abraço Aquele abraço Aquele abraço Aquele abraço'

letra = letra.upper().split()
lista = []
valores = []
lista_frequencia = []
lista_ordenada = []
lista_certa = []
cores = ['red','green','blue','yellow','magenta','cyan','pink','gray','black','brown']

#somente palavras com 4 ou mais letras
for i in range(len(letra)):
    if len(letra[i]) > 3:
        lista.append(letra[i])
        
#criando lista de valores não repetidos
for i in range(len(lista)):
    if lista[i] not in valores:
        valores.append(lista[i])
        
#criando lista com a frequência de cada valor
for palavra in valores:
    lista_frequencia.append([palavra, lista.count(palavra)])
    
#colocando a ordem de frequência 
lista_ordenada = sorted(lista_frequencia, key = lambda x: x[1], reverse=True)

#deixando a lista ordenada somente com palavras a serem usadas
for i in range(20):
    lista_certa.append(lista_ordenada[i][0])
    
#criando eixos
t=turtle.Turtle()
eixos_turtle.plotEixosCartesianos(t,25,15) 

'''#escrevendo as palavras
for i in range(20):
    t.color(cores[random.randint(0,9)])
    t.goto(-50,20)
    t.write(lista_certa[i], True, font = ('Arial',20-i,'normal'))'''
            
print(lista_certa)


