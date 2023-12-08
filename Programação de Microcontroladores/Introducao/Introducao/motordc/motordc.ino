#include <Stepper.h>

#define velmotor 3
#define mla 4
#define mlb 5

int vel = 0;

#define e1 8
#define e2 9
#define e3 10
#define e4 11
#define passosPorGiro 32

Stepper mp(passosPorGiro,e1,e3,e2,e4);

void setup()
{
  pinMode(velmotor,OUTPUT);
  pinMode(mla,OUTPUT);
  pinMode(mlb,OUTPUT);
  digitalWrite(mla,LOW);
  digitalWrite(mlb,LOW);
  analogWrite(velmotor,vel);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop()
{
  String texto = Serial.readString();
  texto.trim();
  if (texto != "")
  {
    if (texto == "misture")
    {
      vel=40;
      analogWrite(velmotor,vel);

      motorPasso(500,1,1,1000);

      digitalWrite(mlb,HIGH);
      digitalWrite(mla,LOW);

      delay(2000);

      vel=30;
      analogWrite(velmotor,vel);

      delay(10000);

      digitalWrite(mlb, LOW);
      digitalWrite(mla,LOW);
      
      delay(1000);

      motorPasso(500,-1,1,3000);
    }
  }
}

void motorPasso(int vel, int sentido, int voltas, int tmp)
{
  mp.setSpeed(vel);
  for (int i = 0; i<(32*voltas); i++)
  {
    mp.step(passosPorGiro*sentido);
  }
  delay(tmp);
  
}

