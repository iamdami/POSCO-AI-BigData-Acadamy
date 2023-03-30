#include <DHT.h>
#include <AsyncTimer.h>
#include <Vegemite.h>
#include <SoftPWM.h>


auto SOILMOIST_PIN = A6;
auto DHT22_PIN = A1;
auto FAN_PIN = A3;
auto PUMP_PIN = 16;
auto LAMP_PIN = 17;

SOFTPWM_DEFINE_CHANNEL(FAN_PIN);
DHT dht(DHT22_PIN, DHT22);
AsyncTimer t;
Vegemite v;

bool currentPumpWorking = false;

void setup() {

  Serial.begin(250000);
  SoftPWM.begin(490);
  dht.begin();

  pinMode(SOILMOIST_PIN, INPUT);
  pinMode(PUMP_PIN, OUTPUT);
  pinMode(LAMP_PIN, OUTPUT);

  v.requestSubscription("config-light"); //주기적으로 config-light 정보를 받아와라. 받아오는 주기는 vegemite가 알아서
  v.requestSubscription("config-fan");
  v.requestSubscription("pump-water");
  v.requestSubscription("config-auto");

//1초 간격으로 DHT센서에서 온/습도 정보를 받아오고 인터넷 홈페이지 제어상태 정보 받아옴
  t.setInterval([]() {
    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();
    int autoConf=int(v.recv("config-auto"));
    int pumpWater = int(v.recv("pump-water"));
    int lightConf = int(v.recv("config-light"));
    int fanSpeed = int(v.recv("config-fan"));

//온/습도 화면 표시
    if (!isnan(humidity) && !isnan(temperature)) {
      v.send("temperature", temperature);
      v.send("humidity", humidity);
    }
//토양 습도 화면 표시
    int soilMoist=map(analogRead(SOILMOIST_PIN), 0, 1023, 100, 0);
    v.send("soilmoist", soilMoist);

//auto mode ON
    if(autoConf==1) {

      if(temperature < 25){ // 온도 25보다 높을 때, LED 켜짐
        digitalWrite(LAMP_PIN, HIGH);
      }
      else {
        digitalWrite(LAMP_PIN, LOW); // 온도 25 이하일 때, LED 꺼짐
      }

      if (humidity > 75) { // 습도가 75보다 높을 때, DC FAN: ON
        SoftPWM.set(100);
        delay(2000);
      }
      else { // 습도가 75 이하일 때, DC FAN: OFF
        SoftPWM.set(0);
        delay(2000);
      }

      if (humidity < 60){ // 습도가 60보다 낮을 때, 펌프: ON
        digitalWrite(PUMP_PIN, HIGH);
      }
      else { //습도가 60 이상일 때, 펌프: OFF
        digitalWrite(PUMP_PIN, LOW);
      }  
  }
  
  //auto mode OFF
    else {
      
      if (pumpWater == 1 && !currentPumpWorking) { //5초 동안 펌프 ON
            currentPumpWorking = true;
            v.send("pump-water", 0);
            digitalWrite(PUMP_PIN, HIGH);
            t.setTimeout([]() {
              digitalWrite(PUMP_PIN, LOW);
              currentPumpWorking = false;
            }, 5000);
          }

      digitalWrite(LAMP_PIN, lightConf==1? HIGH : LOW); // lightConf가 1이면 LED ON
          // 0, 1, 2 3단계로 DC FAN 작동
      if (fanSpeed==0) { // 0 단계일 때, DC FAN OFF
        SoftPWM.set(0);}
      else if (fanSpeed==1) { // 1 단계일 때, DC FAN 최저 속도
        SoftPWM.set(70);}
      else {
        SoftPWM.set(100);} // 2 단계일 때, DC FAN 최고 속도
      }
      },1000);

      }


void loop() {
  v.subscribe();
  t.handle();
}