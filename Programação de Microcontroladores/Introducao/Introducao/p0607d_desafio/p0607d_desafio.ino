// 7 notas
int frequenciasDasNotas[7] = {659.26, 659.26, 659.26, 523.26, 659.26, 784.00, 392.00};
int intervalosEntreNotas[7] = {100, 200, 200, 100, 200, 400, 200};

// COMECE COPIANDO AQUI O SEU CÓDIGO DO APERFEIÇOAMENTO
// DEPOIS FAÇA OS NOVOS RECURSOS

// COMECE COPIANDO AQUI O SEU CÓDIGO DA IMPLEMENTAÇÃO
#include<GFButton.h>
#include<ShiftDisplay.h>
#include<RotaryEncoder.h>

ShiftDisplay display(4, 7, 8, COMMON_ANODE, 4, true);
int led[] = {13, 12, 11, 10};
int contador[] = {0, 0, 0, 0};
int contagem[] = {0, 0, 0, 0};
unsigned long instanteAnterior[] = {0, 0, 0, 0};
RotaryEncoder encoder(20, 21);
int posicaoAnterior = 0;
bool emAndamento[] = {false, false, false, false};
GFButton botao1(A1);
GFButton botao2(A2);
int terra = A5;
int campainha = 5;
int indiceDaContagemAtual = 0;
int indiceVisu = 0;
unsigned long instante_tick_anterior = 0;
int contaNota = 0;
unsigned long tempoMusica = 0;
int flag = 1;

void mudaCont() {
  digitalWrite(led[indiceVisu], HIGH);
  if (indiceVisu == 3)
  {
    indiceVisu = 0;
  }
  else {
    indiceVisu++;
  }
  digitalWrite(led[indiceVisu], LOW);

}
void tickDoEncoder() {
  encoder.tick();
}

void mudaTrue() {
  emAndamento[indiceVisu] = true;
}

void setup()
{
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  digitalWrite(12, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(10, HIGH);
  Serial.begin(9600);
  int origem1 = digitalPinToInterrupt(20);
  attachInterrupt(origem1, tickDoEncoder, CHANGE);
  int origem2 = digitalPinToInterrupt(21);
  attachInterrupt(origem2, tickDoEncoder, CHANGE);
  pinMode(terra, OUTPUT);
  digitalWrite(terra, LOW);
  pinMode(campainha, OUTPUT);
  botao1.setPressHandler(mudaTrue);
  botao2.setPressHandler(mudaCont);
}

void loop() {
  if (indiceDaContagemAtual == 4)
  {
    indiceDaContagemAtual = 0;
  }
  unsigned long instanteAtual = millis();

  if (emAndamento[indiceDaContagemAtual] == true) {
    if (instanteAtual > instanteAnterior[indiceDaContagemAtual] + 1000) {
      contador[indiceDaContagemAtual]--;
      instanteAnterior[indiceDaContagemAtual] = instanteAtual;
    }
  }
  int posicao = encoder.getPosition();
  unsigned long instante_tick_atual = millis();
  if (posicao > posicaoAnterior) {
    if (instante_tick_atual > instante_tick_anterior + 50) {
      contador[indiceVisu] = contador[indiceVisu] + 1;
      instante_tick_anterior = instante_tick_atual;
    }
    else {
      contador[indiceVisu] = contador[indiceVisu] + 15;
      instante_tick_anterior = instante_tick_atual;
    }
  }
  else if (posicao < posicaoAnterior) {
    if (instante_tick_atual > instante_tick_anterior + 50) {
      contador[indiceVisu] = contador[indiceVisu] - 1;
      instante_tick_anterior = instante_tick_atual;
    }
    else {
      contador[indiceVisu] = contador[indiceVisu] - 15;
      instante_tick_anterior = instante_tick_atual;
    }

    if (contador[indiceVisu] < 0) {
      contador[indiceVisu] = 0;
    }
  }
  posicaoAnterior = posicao;

  if (contador[indiceDaContagemAtual] == 0 && emAndamento[indiceDaContagemAtual] == true) {
    emAndamento[indiceDaContagemAtual] = false;
    tone(campainha, frequenciasDasNotas[contaNota], intervalosEntreNotas[contaNota]);
    flag = 0;

  }
  if (contaNota == 6)
  {
    flag = 1;
  }
  if (flag == 0) {
    if (millis() >= tempoMusica + intervalosEntreNotas[contaNota]) {
      tone(campainha, frequenciasDasNotas[contaNota + 1], intervalosEntreNotas[contaNota + 1]);
      tempoMusica = millis();
      contaNota++;
    }
  }
  contagem[indiceDaContagemAtual] = (contador[indiceDaContagemAtual] / 60) * 100 + contador[indiceDaContagemAtual] % 60;
  botao1.process();
  botao2.process();
  display.set(contagem[indiceVisu], true);
  display.changeDot(1, true);
  display.update();
  indiceDaContagemAtual++;
}
