ate9 = ['um', 'dois','tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
ate19 = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta','noventa']
centenas = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos','setecentos','oitocentos','novecentos']

def numero_extenso(k):
    
    numero_extenso = []
    
    if k == 0:
        return
    if k < 10:
        for i in range(1,10):
            if k == i:
                numero_extenso.append(ate9[i-1])
                print(ate9[i-1])
    elif k < 20:
        for i in range(11):
            if k % 10 == i:
                numero_extenso.append(ate19[i])
                print(ate19[i])
    elif k == 100:
        print('cem')
    elif k < 100:
        for i in range(11):
            if k // 10 == i + 1:
                numero_extenso.append(dezenas[i-1])
                print(dezenas[i-1])
        numero_extenso(k%10)
    elif k < 1000:
        for i in range(11):
            if k // 100 == i + 1:
                numero_extenso.append(centenas[i])
                print(centenas[i])
        numero_extenso(k%100)
        
numero_extenso(907)
print()
    
        
