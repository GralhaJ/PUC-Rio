#include<GFButton.h>
#include<ShiftDisplay.h>
#include<RotaryEncoder.h>

ShiftDisplay display(4, 7, 8, COMMON_ANODE, 4, true);

int contador = 0;
int contagem = 0;
unsigned long instanteAnterior = 0;
RotaryEncoder encoder(20, 21);
int posicaoAnterior = 0;
bool emAndamento = false;
GFButton botao1(A1);
int terra = A5;
int campainha = 5;

void tickDoEncoder() {
  encoder.tick();
}

void mudaTrue() {
  emAndamento = true;
}

void setup()
{
  Serial.begin(9600);
  int origem1 = digitalPinToInterrupt(20);
  attachInterrupt(origem1, tickDoEncoder, CHANGE);
  int origem2 = digitalPinToInterrupt(21);
  attachInterrupt(origem2, tickDoEncoder, CHANGE);
  pinMode(terra, OUTPUT);
  digitalWrite(terra, LOW);
  pinMode(campainha, OUTPUT);
  botao1.setPressHandler(mudaTrue);
}

void loop() {

  unsigned long instanteAtual = millis();
  if (emAndamento == true) {
    if (instanteAtual > instanteAnterior + 1000) {
      contador--;
      instanteAnterior = instanteAtual;
    }
  }
  int posicao = encoder.getPosition();
  if (posicao > posicaoAnterior) {
    contador = contador + 15;
  }
  else if (posicao < posicaoAnterior) {
    contador = contador - 15;
    if (contador < 0) {
      contador = 0;
    }
  }
  posicaoAnterior = posicao;

  if (contador == 0 && emAndamento == true){
    emAndamento = false;
    tone(campainha, 2000, 50);
  }

  contagem = (contador/60)*100+contador%60;
  botao1.process();
  display.set(contagem,true);
  display.changeDot(1,true);
  display.update();
}
