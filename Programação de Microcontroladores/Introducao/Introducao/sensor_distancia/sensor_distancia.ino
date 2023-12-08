#include <Ultrasonic.h>

#define pino_trigger 6
#define pino_echo 7

Ultrasonic ultrasonic(pino_trigger, pino_echo);

void setup() {
  Serial.begin(9600);
  Serial.println("Lendo dados do sensor...");
}

void loop() {
  float cmMsec, inMsec;
  long microsec = ultrasonic.timing();
  cmMsec = ultrasonic.convert(microsec, Ultrasonic::CM);
  inMsec = ultrasonic.convert(microsec, Ultrasonic::IN);
  //Exibe informacoes no serial monitor
  if (cmMsec <= 15.0)
  {
    Serial.println("Copo Detectado");
    delay(1000);
  }
  else
  {
    Serial.println("Nenhum copo detectado");
    delay(1000);
  }

}
