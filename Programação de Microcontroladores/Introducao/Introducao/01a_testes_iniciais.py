# importação de bibliotecas
from gpiozero import LED
from time import sleep
from gpiozero import Button
from Adafruit_CharLCD import Adafruit_CharLCD

# definição de funções
def acende_led():
    led2.toggle()

def pisca_led():
    lcd.clear()
    global contador
    led3.blink(n=4, on_time = 0.5, off_time = 0.5)
    lcd.message(str(contador))
    contador += 1

# criação de componentes
led1 = LED(21)
led2 = LED(22)
led3 = LED(23)
led5 = LED(25)
led1.blink(on_time=1, off_time=3)
lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)

contador = 1
botao1 = Button(11)
botao2 = Button(12)
botao3 = Button(13)

botao2.when_pressed = acende_led
botao3.when_pressed = pisca_led

# loop infinito
while True:
    if botao1.is_pressed and led1.is_lit:
        led5.on()
    else:
        led5.off()
    
    sleep(0.2)