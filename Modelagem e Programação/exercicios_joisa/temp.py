def CR_curso(curso, file):
    file_ent = open(file, 'r')
    for linha in file_ent:
        lista_alunos = linha.split(',')
        print(lista_alunos)
        if lista_alunos[1] == curso:
            print(lista_alunos[0],lista_alunos[2])
    file_ent.close()
    

#CR_curso('ENGENHARIA AMBIENTAL','alunosecursos.txt')
        
def CR_minimo(x, file):
    file_opn = open(file, 'r')
    file_ext = open('acimalimite.txt', 'w')
    for linha in file_opn:
        linha1 = linha.rstrip()
        lista_linha = linha1.split(',')
        if float(lista_linha[2]) > x:
            file_ext.write(linha)
    file_opn.close()
    file_ext.close()
    
#CR_minimo(5, 'alunosecursos.txt')

def QntsAlunosCurso(file):
    file_opn = open(file, 'r')
    comp = 0
    ambt = 0
    quim = 0
    prod = 0
    for line in file_opn:
        linha1 = line.rstrip()
        lista_linha = linha1.split(',')
        if  lista_linha[1] == 'ENGENHARIA COMPUTACAO':
            comp += 1
        elif  lista_linha[1] == 'ENGENHARIA AMBIENTAL':
            ambt += 1
        elif  lista_linha[1] == 'ENGENHARIA PRODUCAO':
            prod += 1
        elif  lista_linha[1] == 'ENGENHARIA QUIMICA':
            quim += 1
    lista_final = [['ENGENHARIA COMPUTACAO', comp],['ENGENHARIA AMBIENTAL', ambt], ['ENGENHARIA PRODUCAO', prod],['ENGENHARIA QUIMICA'],quim]
    file_opn.close()
    return lista_final

#print(QntsAlunosCurso('alunosecursos.txt'))


def busca_lista(l_tab, curso):
    #listinha é um item com curso, qntd de alunos do curso
    for ind, listinha in enumerate(l_tab):
        if listinha[0] == curso:
            return ind
    return None

def criaTabFreq(file):
    lTabFreq = []
    file_opn = open(file, 'r')
    for linha in file_opn:
        lAluno = linha.strip().split(',')
        posNaLTabFreq = busca_lista(lTabFreq, lAluno[1])
        if posNaLTabFreq != None:
            lTabFreq[posNaLTabFreq][1] += 1
        else:
            lTabFreq.append( [lAluno[1],1] )
    file_opn.close()
    return lTabFreq

print(criaTabFreq('alunosecursos.txt'))
            
def Alunos_Curso(file):
    file_opn = open(file, 'r')
    for linha in file_opn:
        linha1 = linha.rstrip()
        lista_linha = linha1.split(',')
        if lista_linha[1] == 'ENGENHARIA COMPUTACAO':
            lista_comp
        


    
    