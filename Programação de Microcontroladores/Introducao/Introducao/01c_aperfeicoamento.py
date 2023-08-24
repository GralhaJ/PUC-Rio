# COMECE COPIANDO AQUI O SEU CÓDIGO DA IMPLEMENTAÇÃO
# DEPOIS FAÇA OS NOVOS RECURSOS
# importação de bibliotecas
from os import system
from time import sleep
from mplayer import Player
from gpiozero import Button
from gpiozero import LED
from Adafruit_CharLCD import Adafruit_CharLCD

# para de tocar músicas que tenham ficado tocando da vez passada
system("killall mplayer")

# definição de funções
def toca_pausa():
    player.pause()
    if player.paused:
        led.blink(on_time = 0.5, off_time = 0.5)
    else:
        led.on()
        
def proxima():
    player.pt_step(1)
    
def anterior():
    if player.time_pos > 2:
        player.time_pos = 0
    else:
        player.pt_step(-1)
        
def aperta():
    player.speed = 2
    
def solta():
    if player.speed == 2:
        player.speed = 1
    else:
        player.pt_step(1)
        
def formatacao():
    tempo = player.time_pos
    minutos = tempo // 60
    segundos = tempo % 60
    
    
# criação de componentes
led = LED(21)
player = Player()
player.loadlist("playlist.txt")
botao1 = Button(11)
botao2 = Button(12)
botao3 = Button(13)
lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)

led.on()

botao2.when_pressed = toca_pausa

botao3.when_held = aperta
botao3.when_released = solta

botao1.when_pressed = anterior

# loop infinito
while True:
    lcd.clear()
    lcd.message(player.metadata["Title"]+"\n")
    lcd.message("%02d:%02d/%02d:%02d" %(player.time_pos//60, player.time_pos%60, player.length//60, player.length%60))

    sleep(0.2)

