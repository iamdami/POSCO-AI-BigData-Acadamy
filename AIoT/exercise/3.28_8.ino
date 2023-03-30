#include <DHT.h>
#include <AsyncTimer.h> //AsyncTimer 라이브러리 호출
#include <Vegemite.h>
DHT dht(A1, DHT22);
AsyncTimer t;
Vegemite v;
void setup() {
  Serial.begin(250000);
  dht.begin();
  t.setInterval([]() { //2초마다 온/습도 정보 측정
    float humidity=dht.readHumidity();
    float temperature=dht.readTemperature();
    if(!isnan(humidity) && !isnan(temperature)) { //온/습도 정보를 vegemite를 통해 전달
      v.send("temperature", temperature);
      v.send("humidity", humidity);
    }
  }, 1000);
}
void loop() {
  t.handle(); //시간 간격에 따라 반복
}