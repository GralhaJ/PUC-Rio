# COMECE COPIANDO AQUI O SEU CÓDIGO DA IMPLEMENTAÇÃO
# DEPOIS FAÇA OS NOVOS RECURSOS
# importação de bibliotecas
from extra.redefinir_banco import redefinir_banco
from pymongo import MongoClient, ASCENDING, DESCENDING
from Adafruit_CharLCD import Adafruit_CharLCD
from py_irsend.irsend import *
from lirc import init, nextcode
from time import sleep
from gpiozero import Buzzer
from gpiozero import DistanceSensor
from datetime import datetime
from gpiozero import Button

# a linha abaixo apaga todo o banco e reinsere os moradores
#redefinir_banco()

# parâmetros iniciais do banco
cliente = MongoClient("localhost", 27017)
banco = cliente["projeto03"]
colecao = banco["moradores"]
colecao2 = banco["dados"]

# definição de funções
def validar_apartamento(num_apt):
    busca = {"apartamento": num_apt}
    if colecao.find_one(busca) != None:
        return True
    else:
        return False
    
def retornar_nome_do_morador(num_apt, password):
    busca = {"apartamento":num_apt, "senha":password}
    find = colecao.find_one(busca)
    if find != None:
        return colecao.find_one(busca)["nome"]
    else:
        return None
    
def chama_coletar_digitos():
    apto = coletar_digitos("Digite o apto")
    busca = {"apartamento" : apto}
    ordenacao = [["datetime", DESCENDING]]
    busca = list(colecao2.find(busca, sort = ordenacao))
    for tentativa in busca:
        tempo = tentativa["datetime"]
        if "nome" in tentativa:    
            nome = tentativa["nome"]
            print(tempo.strftime("%d/%m (%H:%M) ")+nome)
        else:
            print(tempo.strftime("%d/%m (%H:%M) : senha incorreta"))
        
def coletar_digitos(msg):
    lcd.clear()
    lcd.message(msg+"\n") 
    texto = ""
    while True:
        lista_com_codigos = nextcode()
        if lista_com_codigos != []:
            codigo = lista_com_codigos[0]
            if codigo != "KEY_OK":
                texto += codigo[-1]
                buzzer.beep(n=1, on_time=0.3)
                lcd.message("*")
            else:
                buzzer.beep(n=1, on_time=0.3)
                return texto
def requisita():
    tentativa_apt = coletar_digitos("Digite o apto:")
    if validar_apartamento(tentativa_apt):
        tentativa_senha = coletar_digitos("Digite a senha:")
        morador = retornar_nome_do_morador(tentativa_apt, tentativa_senha)
        if morador != None:
            lcd.clear()
            lcd.message("Bem-Vindo(a)!\n%s"%morador)
            tempo = datetime.now()
            dicionario = {"nome": morador, "apartamento": tentativa_apt, "datetime":tempo}
            colecao2.insert(dicionario)
        else:
            tempo = datetime.now()
            dicionario = {"apartamento": tentativa_apt, "datetime":tempo}
            colecao2.insert(dicionario)
            lcd.clear()
            buzzer.beep(n=2, on_time=0.2, off_time=0.2)
            lcd.message("Acesso Negado")
    else:
        lcd.clear()
        buzzer.beep(n=2, on_time=0.2, off_time=0.2)
        lcd.message("Apartamento\nInválido")
    sleep(1)
    
# criação de componentes
lcd = Adafruit_CharLCD(2,3,4,5,6,7,16,2)
init("aula", blocking = False)
buzzer = Buzzer(16)
sensor = DistanceSensor(trigger=17, echo=18)
botao1 = Button(11)

sensor.threshold_distance = 0.1

sensor.when_in_range = requisita

botao1.when_pressed = chama_coletar_digitos



  
    
        
        
    
    
                           
                    
                    
                    
    






