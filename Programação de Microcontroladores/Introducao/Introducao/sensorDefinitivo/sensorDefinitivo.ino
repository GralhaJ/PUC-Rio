const int pinoLed = 6; //PINO DIGITAL UTILIZADO PELO LED
const int pinoSensor = 7; //PINO DIGITAL UTILIZADO PELO SENSOR
bool estadoSensor = LOW;

void setup()
{
  pinMode(pinoSensor, INPUT); //DEFINE O PINO COMO ENTRADA
  pinMode(pinoLed, OUTPUT); //DEFINE O PINO COMO SAÍDA
  digitalWrite(pinoLed, LOW); //LED INICIA DESLIGADO
  Serial.begin(9600);
}

void loop()
{
  estadoSensor = digitalRead(pinoSensor);
  if(estadoSensor == HIGH)
  { 
    digitalWrite(pinoLed, LOW); 
    Serial.println("VAZIO");
    delay(500);
  }else
  { 
    digitalWrite(pinoLed, HIGH); //APAGA O LED
    Serial.println("COPO DETECTADO");
    delay(500);
  }
}