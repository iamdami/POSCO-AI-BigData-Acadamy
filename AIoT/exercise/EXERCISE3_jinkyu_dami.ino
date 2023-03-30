#include <U8g2lib.h>
#include "DHT.h"
U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/U8X8_PIN_NONE);
#define DHTPIN A1
#define DHTTYPE DHT22
#define PUMP 16
#define SOILHUMI A6

DHT dht(DHTPIN, DHTTYPE);
uint32_t DataCaptureDelay = 3000;
uint32_t DataCapture_ST = 0;
float Temp;
float Humi;
float pump;
int Soilhumi = 0;
void setup() {
  dht.begin();
//DHT 센서 초기화
    u8g2.begin();
//OLED 디스플레이 초기화
    DataCapture_ST = millis();
//데이터 캡처 시작 시간 초기화
    pinMode(PUMP, OUTPUT);
}
void loop() {
  if ((millis() - DataCapture_ST) > DataCaptureDelay) {  // 지정한 시간마다 데이터 캡처
    Humi = dht.readHumidity();                           // DHT 센서에서 습도 값 측정
    Temp = dht.readTemperature();                        // DHT 센서에서 온도 값 측정
    Soilhumi = map(analogRead(SOILHUMI), 0, 1023, 100, 0);
    if (isnan(Humi) || isnan(Temp)) {                         // 만약 DHT 센서에서 읽어온 값이 NaN이라면,
      Serial.println(F("Failed to read from DHT sensor !"));  // 시리얼 모니터에 오류 메시지 출력
      return;                                                 // 다음 루프로 진행하지 않고 바로 함수를 빠져나옴
    }
    if (Soilhumi <= 30) {
      digitalWrite(PUMP, HIGH);
       // 30도 이하이면 PUMP 동작
    } else if (Soilhumi > 60) {
      digitalWrite(PUMP, LOW);
        // 25도 이상이면  PUMP OFF
    } 
    // SoftPWM.set(Soilhumi);
    // }
     OLEDdraw();                 // OLED 디스플레이에 데이터 출력
    DataCapture_ST = millis();  // 데이터 캡처 시작 시간 재설정
  }
   
  }
  void OLEDdraw() {                      // OLED 디스플레이에 데이터 출력하는 함수
    u8g2.clearBuffer();                  // 이전에 디스플레이에 출력된 내용을 지우기
    u8g2.setFont(u8g2_font_ncenB08_te);  // 폰트 설정
  u8g2.drawStr(1, 15, " AIBD AIOT");   // “AIBD AIOT”이라는 문자열과, 온도, 습도, 토양습도를 나타내는 문자열을 디스플레이에 출력
    u8g2.drawStr(15, 36, "Temp.");
    u8g2.setCursor(85, 36);  // 출력 위치를 설정
    u8g2.print(Temp);        // 온도, 습도, 토양습도 값을 출력
    u8g2.drawStr(114, 36, "\xb0");
    u8g2.drawStr(119, 36, "C");
    u8g2.drawStr(15, 47, "Humidity");
    u8g2.setCursor(85, 47);
    u8g2.print(Humi);
    u8g2.drawStr(116, 47, "%");
    u8g2.drawStr(15, 58, "S - oil");
    u8g2.setCursor(85, 58);
    u8g2.print(Soilhumi);
    u8g2.drawStr(113, 58, "%");
    u8g2.sendBuffer();  // 호출하여 디스플레이에 내용을 출력
  }