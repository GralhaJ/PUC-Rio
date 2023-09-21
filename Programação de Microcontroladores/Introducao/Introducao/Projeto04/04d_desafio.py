# COMECE COPIANDO AQUI O SEU CÓDIGO DA IMPLEMENTAÇÃO
# DEPOIS FAÇA OS NOVOS RECURSOS
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
from urllib.request import urlretrieve
from mplayer import Player
import unidecode

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

global aplicativo 
aplicativo = None
def iniciar_gravacao(): 
    global aplicativo 
    comando = ["arecord", "--duration", "30", "audio.wav"]
    aplicativo = Popen(comando) # executa em plano de fundo
    
def parar_gravacao(): 
    global aplicativo 
    if aplicativo != None: 
        aplicativo.terminate()
        aplicativo = None
    enviar_gravacao()
    
def enviar_gravacao():
    endereco = endereco_base + "/sendVoice"
    dados = {"chat_id": id_da_conversa}
    system("opusenc audio.wav audio.ogg")
    arquivo = {"voice": open("audio.ogg", "rb")}
    resposta = post(endereco, data=dados, files=arquivo)

def rasp_toca():
    endereco = endereco_base + "/getFile"
    dados = {"file_id": id_do_arquivo} 
    resposta = get(endereco, json=dados) 
    dicionario = resposta.json() 
    final_do_link = dicionario["result"]["file_path"]  
    link_do_arquivo = "https://api.telegram.org/file/bot" + chave + "/" + final_do_link
    arquivo_de_destino = "meu_arquivo.ogg" 
    urlretrieve(link_do_arquivo, arquivo_de_destino)
    player.loadfile("meu_arquivo.ogg")
    
t1 = datetime.now()
def tempo1():
    print("oi")
    global t1
    t1 = datetime.now()
    
def tempo2():
    print("tchau")
    intervalo = datetime.now()-t1
    intervalo = intervalo.total_seconds()
    if intervalo >= 10:
        pessoa_saiu()
    
def pessoa_saiu():
    mensagm = "Pessoa saiu"
    endereco = endereco_base + "/sendMessage"
    dados = {"chat_id": id_da_conversa, "text": mensagm}
    resposta = post(endereco, json=dados)

def escreve_lcd(mensagem):
    lcd.clear()
    lcd.message(mensagem)
    
def extra(mensagem_recebida):
    for i in range(2):
        lcd.message("Mensagem Recebida")
        sleep(0.4)
        campainha.beep(n=1,on_time=0.2, off_time = 0.2)
        
        lcd.clear()
        sleep(0.4)
    lcd.clear()
    formata = unidecode.unidecode(mensagem_recebida)
    lcd.message(formata)
    for i in range(16-len(mensagem_recebida)):
        sleep(0.5)
        lcd.move_left()
# criação de componentes
botao1 = Button(11)
botao2 = Button(12)
botao3 = Button(13)
campainha = Buzzer(16)
botao1.when_pressed = buz_on
botao1.when_released = buz_off
botao3.when_pressed = iniciar_gravacao
botao3.when_released = parar_gravacao
player = Player()
sensor = DistanceSensor(trigger=17, echo=18)
sensor.threshold_distance = 0.5
sensor.when_in_range = tempo1
sensor.when_out_of_range = tempo2
botao2.when_pressed = apagaled1
led1 = LED(21)
led2 = LED(22)
lcd = Adafruit_CharLCD(2,3,4,5,6,7,16,2)
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
            elif texto == "Ignorar":
                print("")
            else:
                extra(texto)
        elif "voice" in mensagem: 
            id_do_arquivo = mensagem["voice"]["file_id"] 
            # depois baixa o arquivo e faz algo com ele...
            rasp_toca()
        elif "photo" in mensagem: 
            foto_mais_resolucao = mensagem["photo"][-1] 
            id_do_arquivo = foto_mais_resolucao["file_id"] 
            # depois baixa o arquivo e faz algo com ele...
        proximo_id_de_update = resultado["update_id"] + 1
        sleep(1)
    



