def interseção(list_1, list_2):
    contador = 0
    for el in list_1:
            if el in list_2:
                contador += 1
    return contador
        
def resultado_megasena(lista_geral, lista_resultado):
    contador = 0
    k = 0
    for lista in lista_geral:
        k += 1
        if lista == lista_resultado:
            print('Houve aposta vencedora')
        for i in range(len(lista)):
            if lista[i] in lista_resultado:
                contador += 1
                resultado = contador
        contador = 0
            
        print('A lista %d acertou %d números'%(k, resultado))
        
def verifica_megasena(lista_geral, lista_resultado):
    for el in lista_geral:
        acertos = interseção(el, lista_resultado)
        print(el, '->', acertos)
        
list_1 = [1,2,3]
list_2 = [2,3]
print(interseção(list_1, list_2))
        
lista_geral= [ [13,24,28,31,50,59],          
           [13,20,22,28,36,50,53,59],          
           [10,34,28,21,50,49]]

lista_resultado= [13,22,44,33,49,50]

resultado_megasena(lista_geral, lista_resultado)

verifica_megasena(lista_geral, lista_resultado)
    
    
    
    
    