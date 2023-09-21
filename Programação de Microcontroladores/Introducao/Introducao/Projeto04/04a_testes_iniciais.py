# importação de bibliotecas
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
from os import system
from subprocess import Popen
from requests import post, get

# parâmetros iniciais do Telegram
id_da_conversa = "6368071961"
chave = "6456813586:AAGF6fHercfrmYC9IguzhLfQbqc0eG0ym8s"
endereco_base = "https://api.telegram.org/bot" + chave

# definição de funções
def escreve_lcd(mensagem):
    lcd.clear()
    lcd.message(mensagem)
    
def grava_audio():
    escreve_lcd("Gravando...")
    system("arecord --duration 5 --format cd audio1.wav")
    lcd.clear()
    
def tira_fotos():
    qntd = 5
    for i in range(qntd):
        system("fswebcam --resolution 640x480 --skip 10 foto"+str(i)+".jpg")
        led1.blink(n=1,on_time = 0.2)
        sleep(2)
    led1.off()
    
def enviar_mensagem():
    endereco = endereco_base + "/sendMessage"
    dados = {"chat_id": id_da_conversa, "text": "Olá!"}
    resposta = post(endereco, json=dados)
    print(resposta.text)
    
    
    
# criação de componentes
botao1 = Button(11)
botao2 = Button(12)
botao3 = Button(13)

lcd = Adafruit_CharLCD(2,3,4,5,6,7,16,2)

led1 = LED(21)

botao1.when_pressed = grava_audio

botao2.when_pressed = tira_fotos

botao3.when_pressed = enviar_mensagem