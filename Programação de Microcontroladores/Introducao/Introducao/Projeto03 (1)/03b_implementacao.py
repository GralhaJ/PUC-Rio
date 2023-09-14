# importação de bibliotecas
from extra.redefinir_banco import redefinir_banco
from pymongo import MongoClient
from Adafruit_CharLCD import Adafruit_CharLCD
from py_irsend.irsend import *
from lirc import init, nextcode
from time import sleep

# a linha abaixo apaga todo o banco e reinsere os moradores
redefinir_banco()

# parâmetros iniciais do banco
cliente = MongoClient("localhost", 27017)
banco = cliente["projeto03"]
colecao = banco["moradores"]

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
                lcd.message("*")
            else:
                return texto
    
# criação de componentes
lcd = Adafruit_CharLCD(2,3,4,5,6,7,16,2)
init("aula", blocking = False)

# loop infinito
while True:
    tentativa_apt = coletar_digitos("Digite o apto:")
    if validar_apartamento(tentativa_apt):
        tentativa_senha = coletar_digitos("Digite a senha:")
        morador = retornar_nome_do_morador(tentativa_apt, tentativa_senha)
        if morador != None:
            lcd.clear()
            lcd.message("Bem-Vindo(a)!\n%s"%morador)
        else:
            lcd.clear()
            lcd.message("Acesso Negado")
    else:
        lcd.clear()
        lcd.message("Apartamento\nInválido")
    sleep(1)
        
        
    
    
                           
                    
                    
                    
    





