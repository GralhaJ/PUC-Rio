# importação de bibliotecas
from gpiozero import LED, Button
from datetime import datetime
from pymongo import MongoClient, DESCENDING
from flask import Flask

# criação do servidor
cliente = MongoClient("localhost", 27017)
banco = cliente["jam"]
colecao = banco["estados"]

# definição de funções das páginas
app = Flask(__name__)
@app.route("/")
def iniciar():
    return "inicio"

@app.route("/led/<int:i>/<string:estado>")
def atualiza_led(i, estado):
    if estado == "on":
        leds[i].on()
    elif estado == "off":
        leds[i].off()
    lista = []
    for led in leds:
        lista.append(led.is_lit)
      
    documento = {"data": datetime.now(), "estado_dos_leds": lista}
    colecao.insert(documento)
    
    return "Olha seu led"

# criação dos componentes
leds = [LED(21), LED(22), LED(23), LED(24), LED(25)]
botoes = [Button(11), Button(12), Button(13), Button(14)]

atualiza_led(4, False)



# rode o servidor
app.run(port=5000, debug=False)