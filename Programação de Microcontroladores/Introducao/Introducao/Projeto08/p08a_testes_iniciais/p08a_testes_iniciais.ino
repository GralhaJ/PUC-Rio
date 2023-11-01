#include <GFButton.h>
#include <EEPROM.h>
#include <Servo.h>

GFButton botaoB(3);
GFButton botaoA(2);
GFButton botaoC(4);

int potenciometro = A5;

int base = 12;
int ombro = 11;
Servo servo_base;
Servo servo_ombro;
int angulo_ombro = 45;

int contador = 0;

int endereco = 0;

void setup()
{
  Serial.begin(9600);
  EEPROM.get(endereco, contador);
  botaoB.setPressHandler(botaoB_pressionado);
  pinMode(potenciometro, INPUT);
  servo_base.attach(base);
  servo_ombro.attach(ombro);
}

void loop()
{
  botaoB.process();
  botaoA.process();
  botaoC.process();
  int valorLido = analogRead(potenciometro);
  int valorFinal = map(valorLido, 0, 1023, 0, 180);
  servo_base.write(valorFinal);

  if(botaoA.isPressed() == true)
  {
    Serial.println("botao A apertado");
    if (angulo_ombro >= 46)
    {
      angulo_ombro--;;
    }
    Serial.println(angulo_ombro);
    servo_ombro.write(angulo_ombro);
    delay(100);
  }
  
  if(botaoC.isPressed() == true)
  { 
    Serial.println("botao C apertado");
    if (angulo_ombro <= 134)
    {
      angulo_ombro++;
    }
    Serial.println(angulo_ombro);
    servo_ombro.write(angulo_ombro);
    delay(100);
  }

  EEPROM.put(endereco, contador);
}
void botaoB_pressionado(GFButton& botaoB)
{
  contador++;
  Serial.println(contador);
}
