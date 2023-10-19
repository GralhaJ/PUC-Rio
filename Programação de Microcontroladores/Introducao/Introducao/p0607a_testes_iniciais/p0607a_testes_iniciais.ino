#include<GFButton.h>
#include<ShiftDisplay.h>
#include<RotaryEncoder.h>

RotaryEncoder encoder(20, 21);
int posicaoAnterior = 0;

ShiftDisplay display(4, 7, 8, COMMON_ANODE, 4, true);
int led1 = 13;
int led2 = 12;
int contador = 0;
GFButton botao2(A2);
GFButton botao3(A3);
unsigned long instanteAnterior = 0;
int terra = A5;
int campainha = 5;

void mudaEstado() {
  if ( digitalRead(led2) == LOW)  {
    digitalWrite(led2, HIGH);
  }
  else {
    digitalWrite(led2, LOW);
  }
}

int soma() {
  contador++;
  return contador;
}
void tickDoEncoder() {
  encoder.tick();
}

void setup() {
  // put your setup code here, to run once:
  int origem1 = digitalPinToInterrupt(20);
  attachInterrupt(origem1, tickDoEncoder, CHANGE);
  int origem2 = digitalPinToInterrupt(21);
  attachInterrupt(origem2, tickDoEncoder, CHANGE);
  pinMode(terra, OUTPUT);
  digitalWrite(terra, LOW);
  pinMode(campainha, OUTPUT);
  Serial.begin(9600);
  pinMode(led2, OUTPUT);
  pinMode(led1, OUTPUT);
  digitalWrite(led1, HIGH);
  botao2.setPressHandler(mudaEstado);
  botao3.setPressHandler(soma);
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long instanteAtual = millis();
  if (instanteAtual > instanteAnterior + 2000) {
    Serial.println(contador);
    instanteAnterior = instanteAtual;
  }
  int posicao = encoder.getPosition();
  if (posicao > posicaoAnterior) {
    tone(campainha, 440.0, 50);
  }
  else if (posicao < posicaoAnterior) {
    tone(campainha, 220.0, 50);
  }
  posicaoAnterior = posicao;
  botao2.process();
  botao3.process();
  digitalWrite(led1, LOW);
  display.set(contador);
  display.update();
}
