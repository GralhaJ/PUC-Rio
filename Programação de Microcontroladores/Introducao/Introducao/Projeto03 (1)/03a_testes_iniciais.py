# importação de bibliotecas
from gpiozero import Button
from gpiozero import Buzzer
from gpiozero import LED
from gpiozero import DistanceSensor
from Adafruit_CharLCD import Adafruit_CharLCD
from datetime import datetime
from pymongo import MongoClient

# definição de funções
def pisca_led1():
    led1.blink(n=2)

def beepar():
    buzzer.beep(n=1, on_time=0.5)
    
def informa_distancia():
    lcd.clear()
    lcd.message("%.1fcm"%(sensor.distance*100))
    dados = {"distancia":sensor.distance, "horario":datetime.now()}
    colecao.insert(dados)

    
    
# criação de componentes
botao1 = Button(11)
botao2 = Button(12)
buzzer = Buzzer(16)
led1 = LED(21)
lcd = Adafruit_CharLCD(2,3,4,5,6,7,16,2)
sensor = DistanceSensor(trigger = 17, echo = 18)
cliente = MongoClient("localhost",27017)
banco = cliente["gralha"]
colecao = banco["joao"]

#parte1
botao1.when_pressed = beepar

#parte2
sensor.threshold_distance = 0.1
sensor.when_in_range = pisca_led1
sensor.when_out_of_range = pisca_led1

#parte3                                                                                                  
botao2.when_pressed = informa_distancia


