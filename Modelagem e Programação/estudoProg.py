#EX1
def analisa(s1, s2):
    s1 = s1.upper()
    s2 = s2.upper()
    s = ''
    tam = len(s1)
    for i in range(tam):
        if s1[i] == s2[i]:
            s += s1[i]
    return s

#EX2
def diferença_listas(l1, l2):
    l = []
    if len(l1) == len(l2):
        for i in range(len(l1)):
            l.append(l1[i]-l2[i])
    if len(l1) > len(l2):
        for i in range(len(l1)-len(l2)):
            l2.append(0)
        for i in range(len(l1)):
            l.append(l1[i]-l2[i])
    if len(l2) > len(l1):
        for i in range(len(l2)-len(l1)):
            l1.append(0)
        for i in range(len(l2)):
            l.append(l1[i]-l2[i])
    return l
#EX3A
def criaListaDeContas():
    lista_contas = open('saldoinicial.txt', 'r')
    contas = []
    for linha in lista_contas:
        linha = linha.strip().split()
        linha[1] = float(linha[1])
        contas.append(linha)
    lista_contas.close()  
    return contas
#EX3B
def BuscaAgencia(lista_agencias, agencia_procurada):
    for pos, agencia in enumerate(lista_agencias):
        if agencia[0] == agencia_procurada:
            return pos
    return None
            
def exibeQtdPorAgencia(lista_contas):
    lista_agencias = []
    for conta in lista_contas:
        agencia = conta[0][:2]
        pos = BuscaAgencia(lista_agencias, agencia)
        if pos == None:
            lista_agencias.append([agencia, 1])
        else:
            lista_agencias[pos][1] += 1
    print('A lista de agências e suas frequencias:')
    for agencia in lista_agencias:
        print('Agencia %s: %d contas'%(agencia[0],agencia[1]))
#EX3C       
def BuscaContas(lista_contas, conta_procurada):
    for pos, conta enumerate(lista_contas):
        if conta[0] == conta_procurada:
            return pos
    return None
    
def calculaSaldosFinais(lista_contas):
    operacoes = open('operacoes.txt', 'r')
    for linha in operacoes:
        linha = linha.strip().split(',')
        valor = float(linha[2])
        conta = linha[0]
        pos = BuscaContas(lista_contas, conta)
        if pos != None:
            if linha[1] == 'C':
                lista_contas[pos][1] += valor
            else:
                lista_contas[pos][1] -= valor
    operacoes.close(0)
    lista_contas_atualizada = open('ListaDeContasAtualizada', 'w')
    for contain lista_contas:
        lista_contas_atualizada.write('%s %.2f\n'%(conta[0],conta[1]))
    lsita_contas_atualizada.close()
 
calculaSaldosFinais(criaListaDeContas())
    
    
    
    
    
    
    
    
        