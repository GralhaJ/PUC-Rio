#include <Stepper.h>

#define velmotor 3
#define mla 4
#define mlb 5
int vel = 0;

#define e1 8
#define e2 9
#define e3 10
#define e4 11
#define passosPorGiro 64

Stepper mp(passosPorGiro,e1,e3,e2,e4);

void setup()
{
  pinMode(velmotor,OUTPUT);
  pinMode(mla,OUTPUT);
  pinMode(mlb,OUTPUT);
  digitalWrite(mla,LOW);
  digitalWrite(mlb,LOW);
  analogWrite(velmotor,vel);
}

void loop()
{
  vel=30;
  analogWrite(velmotor,vel);

  digitalWrite(mlb,HIGH);
  digitalWrite(mla,LOW);

  motorPasso(500,1,1,0);
  delay(3000);
  motorPasso(500,-1,1,0);
  delay(3000);
  
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