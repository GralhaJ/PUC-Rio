# importação de bibliotecas
from os import system
from pymongo import MongoClient, ASCENDING, DESCENDING
from Adafruit_CharLCD import Adafruit_CharLCD
from py_irsend.irsend import *
from lirc import init, nextcode
from time import sleep
from gpiozero import Buzzer
from gpiozero import LED
from gpiozero import DistanceSensor
from datetime import datetime
from gpiozero import Button
from subprocess import Popen
from requests import post, get


# Mata todos os aplicativos "mplayer" e "arecord"
system("killall mplayer")
system("killall arecord")


# parâmetros iniciais do Telegram
id_da_conversa = "6368071961"
chave = "6456813586:AAGF6fHercfrmYC9IguzhLfQbqc0eG0ym8s"
endereco_base = "https://api.telegram.org/bot" + chave


# definição de funções
def buz_on():
    campainha.on()
    
def buz_off():
    campainha.off()
    envia_msg()
    envia_foto()
    
def envia_msg():
    print("Vai enviar")
    mensagm = "Tem algm na porta abre ai!!!"
    endereco = endereco_base + "/sendMessage"
    dados = {"chat_id": id_da_conversa, "text": mensagm}
    resposta = post(endereco, json=dados)
    print("Enviado")

def envia_foto():
    endereco = endereco_base + "/sendPhoto"
    tira_fotos()
    dados = {"chat_id": id_da_conversa}
    arquivo = {"photo": open("foto_campainha.jpg", "rb")}
    resposta = post(endereco, data=dados, files=arquivo)

def tira_fotos():
    qntd = 1
    for i in range(qntd):
        system("fswebcam --resolution 640x480 --skip 10 foto_campainha.jpg")
        #sleep(2)
        
def acendeLED1():
    led1.on()

def apagaled1():
    led1.off()
    
def sirene():
    campainha.beep(n=5, on_time=0.09, off_time=0.04)

def ve_resp():
    endereco = endereco_base + "/getUpdates"
    dados = {"chat_id": id_da_conversa}
    resposta = post(endereco, data=dados, files=arquivo)
    resposta - get
    
# criação de componentes
botao1 = Button(11)
botao2 = Button(12)
campainha = Buzzer(16)
botao1.when_pressed = buz_on
botao1.when_released = buz_off

botao2.when_pressed = apagaled1
led1 = LED(21)
led2 = LED(22)

proximo_id_de_update = 0
# loop infinito
while True:
    endereco = endereco_base + "/getUpdates"
    dados = {"offset": proximo_id_de_update}
    resposta = get(endereco, json=dados)
    dicionario_da_resposta = resposta.json()
    for resultado in dicionario_da_resposta["result"]: 
        mensagem = resultado["message"] 
        if "text" in mensagem: 
            texto = mensagem["text"]
            if texto == "Abrir":
                acendeLED1()
            elif texto == "Soar Alarme":
                sirene()
        elif "voice" in mensagem: 
            id_do_arquivo = mensagem["voice"]["file_id"] 
            # depois baixa o arquivo e faz algo com ele...
        elif "photo" in mensagem: 
            foto_mais_resolucao = mensagem["photo"][-1] 
            id_do_arquivo = foto_mais_resolucao["file_id"] 
            # depois baixa o arquivo e faz algo com ele...
        proximo_id_de_update = resultado["update_id"] + 1
        sleep(1)
    
