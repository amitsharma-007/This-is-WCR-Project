

/This is a subpart of a WCR for industrial 
inspection project in TLC under the guidance of Dr. S. R. Pandian and is being done by Amit Sharma, M.Des EDS 2016 batch, roll no. 
eds16m007.  /



#include<dht.h>
dht DHT;

// if you require to change the pin number, Edit the pin with your arduino pin.

#define DHT11_PIN 3

void setup() {

Serial.begin(9600);

 }

void loop() { // READ DATA

Serial.println("Humidity and Temperature of the Field Area");

Serial.println(" ");

int chk = DHT.read11(DHT11_PIN);

Serial.print(" Humidity       : " );

Serial.println(DHT.humidity, 1);

Serial.print(" Temparature    : ");

Serial.println(DHT.temperature, 1);

delay(2000);

}
