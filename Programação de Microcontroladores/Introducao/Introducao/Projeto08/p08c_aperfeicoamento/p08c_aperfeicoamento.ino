// COMECE COPIANDO AQUI O SEU CÓDIGO DA IMPLEMENTAÇÃO
// DEPOIS FAÇA OS NOVOS RECURSOS
#include <meArm.h>
#include <GFButton.h>
#include <EEPROM.h>

GFButton botaoA(2);
GFButton botaoB(3);
GFButton botaoC(4);
GFButton botaoD(5);

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

int pontosSalvos[4][4];
int i = 0;
int endereco = 0;

void setup()
{
  Serial.begin(9600);
  EEPROM.get(endereco, pontosSalvos);
  braco.begin(base, ombro, cotovelo, garra);
  braco.gotoPoint(0,130,0);
  braco.closeGripper();
  botaoA.setPressHandler(botaoA_pressionado);
  botaoB.setPressHandler(botaoB_pressionado);
  botaoC.setPressHandler(botaoC_pressionado);
  botaoD.setPressHandler(botaoD_pressionado);
  pinMode(eixoX, INPUT);
  pinMode(eixoY, INPUT);
}

void loop()
{
  botaoA.process();
  botaoB.process();
  botaoC.process();
  botaoD.process();

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

    braco.goDirectlyTo(valorFinalX, valorFinalY, valorFinalZ);
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

void botaoC_pressionado(GFButton& botaoC)
{
  pontosSalvos[i][0] = braco.getX();
  pontosSalvos[i][1] = braco.getY();
  pontosSalvos[i][2] = braco.getZ();
  pontosSalvos[i][3] = garr;
  if (i<3)
  {
    i++;
  }
  EEPROM.put(endereco, pontosSalvos);
}

void botaoD_pressionado(GFButton& botaoD)
{
  for(i = 0; i <4; i++)
  {
    int x = pontosSalvos[i][0];
    int y = pontosSalvos[i][1];
    int z = pontosSalvos[i][2];
    braco.gotoPoint(x, y, z);
    if (pontosSalvos[i][3] == true)
    {
      braco.closeGripper();
    }
    else
    {
      braco.openGripper();
    }
    
    delay(500);
  }
 
}



