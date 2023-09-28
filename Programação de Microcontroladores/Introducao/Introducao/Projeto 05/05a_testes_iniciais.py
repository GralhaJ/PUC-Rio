# importação de bibliotecas
from gpiozero import LED, MotionSensor, Button, LightSensor, DistanceSensor
from threading import Timer
from requests import post

# definição de funções
def timer_recorrente():
    print("Olá")
    global timer
    timer = Timer(2.0, timer_recorrente)
    timer.start()
    
def parar_timer():
    global timer
    if timer != None:
        timer.cancel()
        timer = None
    
def ligar_led1():
    led1.on()

def desligar_led1():
    led1.off()
    
def ligar_led2():
    led2.on()
    
def desligar_led2():
    led2.off()
    
def ligar():
    led1.on()
    global timer2
    if timer2 != None:
        timer2.cancel()
    led2.on()
        
def desligar():
    led1.off()
    global timer2
    timer2 = Timer(4.0, desligar_led2)
    timer2.start()
    
def botao_pressionado():
    url = "https://maker.ifttt.com/trigger/envia/with/key/Tf4SdM0NqRCeJHbs9ZnhSu37M5eYIfthhgMoYEZDJZ"
    valores_fornecidos = {"value1": sensor_luz.value*100, "value2": sensor_dist.distance*100}
    resultado=post(url, json=valores_fornecidos)
    print(resultado.text)
    

# criação de componentes
global timer
timer = None
timer_recorrente()
led1 = LED(21)
sensor_mov = MotionSensor(27)
sensor_mov.when_motion = ligar
sensor_mov.when_no_motion = desligar
global timer2
timer2 = None
led2 = LED(22)
#CHAVE = "Tf4SdM0NqRCeJHbs9ZnhSu37M5eYIfthhgMoYEZDJZ"
url = "https://maker.ifttt.com/trigger/envia/with/key/Tf4SdM0NqRCeJHbs9ZnhSu37M5eYIfthhgMoYEZDJZ"
botao1 = Button(11)
sensor_luz = LightSensor(8)
sensor_dist = DistanceSensor(trigger=17, echo=18)
botao1.when_pressed = botao_pressionado



# loop infinito
