#define velmotor 3
#define mla 4
#define mlb 5
#define tmp 3000
int vel = 0;

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



  

  
}