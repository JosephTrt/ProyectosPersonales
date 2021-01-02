#include <RTClib.h>
#include <Wire.h>
#include <DHT.h>

#define dhtPin 2
#define dhtType DHT11

int tiempo;

RTC_DS1307 rtc;
DateTime Hora;

DHT dht(dhtPin, dhtType);

void setup() {
  Serial.begin(9600);
  
  rtc.begin();
  dht.begin();
 
  //setTime(11, 40, 0, 29, 12, 20);
  
  while(tiempo == 0) {
    tiempo = Mapeo(valorIngresado());
  }
}
void loop() {
  mostrarHora();
  mostrarTempYHum();
  delay(tiempo * 60000);
}
String valorIngresado() {
  while(true) {
    if(Serial.available() > 0) {
      delay(20);
      String bufferString = "";
  
      while(Serial.available() > 0) {
        bufferString += (char)Serial.read();
      }
      return bufferString;
    }
  }
}
int Mapeo(String numIngresado) {
  int numeroComvertido = numIngresado.toInt();
  return numeroComvertido;
}
void mostrarHora() {
  Hora = rtc.now();
  
  Serial.print(Hora.hour());
  Serial.print(".");
  Serial.print(Hora.minute());
}
void mostrarTempYHum() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  Serial.print(" ");
  Serial.print(h);
  Serial.print(" ");
  Serial.print(t);
  Serial.println("");
}
