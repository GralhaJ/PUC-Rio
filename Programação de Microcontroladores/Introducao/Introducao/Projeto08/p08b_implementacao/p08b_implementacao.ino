#include <meArm.h>
#include <GFButton.h>

GFButton botaoA(2);
GFButton botaoB(3);

int base = 12, ombro = 11, cotovelo = 10, garra = 9;
meArm braco(
 180, 0, -pi/2, pi/2, 
 135, 45, pi/4, 3*pi/4,
 180, 90, 0, -pi/2, 
 30, 0, pi/2, 0
);

int eixoX = A0;
int eixoY = A1;
int eixoZ = A5;

bool garr = false;
bool estado = false;

void setup()
{
  Serial.begin(9600);
  braco.begin(base, ombro, cotovelo, garra);
  braco.gotoPoint(0,130,0);
  braco.closeGripper();
  botaoA.setPressHandler(botaoA_pressionado);
  botaoB.setPressHandler(botaoB_pressionado);
  pinMode(eixoX, INPUT);
  pinMode(eixoY, INPUT);
}

void loop()
{
  botaoA.process();
  botaoB.process();

  int valorLidoX = analogRead(eixoX);
  int valorLidoY = analogRead(eixoY);
  int valorLidoZ = analogRead(eixoZ);

  if (estado == true)
  {
    int valorFinalX = map(valorLidoX, 0, 1023, -150, 150);
    int valorFinalY = map(valorLidoY, 0, 1023, 100, 200);
    int valorFinalZ = map(valorLidoZ, 0, 1023, -30, 100);
    Serial.print(valorFinalX);
    Serial.print("-");
    Serial.print(valorFinalY);
    Serial.print("-");
    Serial.println(valorFinalZ);

    braco.gotoPoint(valorFinalX, valorFinalY, valorFinalZ);
  }
  else
  {
    float coordenadaAtualX = braco.getX();
    float coordenadaAtualY = braco.getY();
    float coordenadaAtualZ = braco.getZ();

    int valorFinalX = map(valorLidoX, 0, 1023, -10, 10);
    int valorFinalY = map(valorLidoY, 0, 1023, -10, 10);
    int valorFinalZ = map(valorLidoZ, 0, 1023, -30, 100);

    coordenadaAtualX = coordenadaAtualX + valorFinalX;
    coordenadaAtualY = coordenadaAtualY + valorFinalY;
    if (coordenadaAtualX > 150)
    {
      coordenadaAtualX = 150;
    }
    if(coordenadaAtualX < -150)
    {
      coordenadaAtualX = -150;
    }
    if (coordenadaAtualY > 200)
    {
      coordenadaAtualY = 200;
    }
    if(coordenadaAtualY < 100)
    {
      coordenadaAtualY = 100;
    }
    
    Serial.print(coordenadaAtualX);
    Serial.print("-");
    Serial.print(coordenadaAtualY);
    Serial.print("-");
    Serial.println(coordenadaAtualZ);

    braco.goDirectlyTo(coordenadaAtualX, coordenadaAtualY, valorFinalZ);
    delay(50);
  }
}

void botaoA_pressionado(GFButton& botaoA)
{
  if (garr == false)
  {
    garr = true;
    braco.closeGripper();
  }
  else
  {
    garr = false;
    braco.openGripper();
  }
}

void botaoB_pressionado(GFButton& botaoA)
{
  if (estado == false)
  {
    estado = true;
    Serial.println("modo absoluto");
  }
  else
  {
    estado = false;
    Serial.println("modo relativo");
  }
}
