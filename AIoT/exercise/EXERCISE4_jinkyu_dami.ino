// 전처리기 지시문: LED와 DHT센서를 제어하기 위한 핀번호 및 라이브러리를 선언
#define LAMP 17
#include <U8g2lib.h>
#include <SoftPWM.h>
#include "DHT.h"

// OLED 디스플레이와 토양습도 센서를 제어하기 위한 핀번호를 선언
U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);
#define DHTPIN A1
#define DHTTYPE DHT22
#define PUMP 16
#define SOILHUMI A6

SOFTPWM_DEFINE_CHANNEL(A3); // PWM을 위한 SoftPWM 채널을 정의

DHT dht(DHTPIN, DHTTYPE); // DHT 센서를 제어하기 위한 객체를 생성합니다.

// 데이터 캡쳐 간격, 온도, 습도, 토양습도, LED 및 팬 제어를 위한 변수를 선언합니다.
uint32_t DataCaptureDelay = 2000;
uint32_t DataCapture_ST = 0;
float Temp;
float Humi;
int Soilhumi = 0;
int Hour = 0;
int Minute = 1;
int Second = 0;
float FanPWM = 0;
uint32_t TimeCompare;
uint32_t StartTime = 0;
uint32_t TimeSum = (uint32_t) ((Hour*60+Minute)*60+Second)*1000;
// 아두이노 보드가 처음 시작될 때 수행할 작업을 설정
void setup() {
    dht.begin(); // DHT 센서를 초기화
    u8g2.begin(); // OLED 디스플레이를 초기화
    DataCapture_ST = millis(); // 데이터 캡처 시작 시간을 초기화
    pinMode(LAMP, OUTPUT); // LED와 펌프를 제어하기 위한 핀의 출력모드를 설정
    StartTime = millis();
    SoftPWM.begin(490); // SoftPWM을 초기화
}
void loop() { // 루프 안에서 반복해서 실행되는 작업을 설정
    if((millis() - DataCapture_ST) > DataCaptureDelay) {  // 지정한 시간마다 데이터 캡처
    Humi = dht.readHumidity();  // DHT 센서에서 습도 값 측정
    Temp = dht.readTemperature();  // DHT 센서에서 온도 값 측정
    if(isnan(Humi) || isnan(Temp)) {  // 만약 DHT 센서에서 읽어온 값이 NaN이라면,
    Serial.println(F("Failed to read from DHT sensor!"));  // 시리얼 모니터에 오류 메시지 출력
    return;  // 다음 루프로 진행하지 않고 바로 함수를 빠져나옴
    }
    if(Soilhumi <= 30) { // 토양습도가 30 이하인 경우 펌프를 가동합니다.
        delay(3000);
        digitalWrite(PUMP, HIGH);
    } else if(Soilhumi > 60) {
        delay(3000);
        digitalWrite(PUMP, LOW);
    }
    }
    OLEDdraw();  // OLED 디스플레이에 데이터 출력
    DataCapture_ST = millis();  // 데이터 캡처 시작 시간 재설정
    TimeCompare = (millis() - StartTime) / TimeSum;
    if (TimeCompare % 2 == 0 ) {
        delay(random(1000, 6000));
        digitalWrite(LAMP, HIGH);
    } else {
        delay(random(1000, 6000));
        digitalWrite(LAMP, LOW);
    }
    if(Temp >= 30) {
        FanPWM = 100;   // 30도 이상이면 FAN ON (PWM:100)
    } else if(Temp > 25) {
        FanPWM = 65;   // 25도 초과이면 FAN PWM 65로 ON
    } else {
        FanPWM = 0;   // 25도 이하이면 FAN OFF (PWM:0)
    }
    SoftPWM.set(FanPWM);   // PWM 값 설정
}
void OLEDdraw() {  // OLED 디스플레이에 데이터 출력하는 함수
  u8g2.clearBuffer();  // 이전에 디스플레이에 출력된 내용을 지우기
  u8g2.setFont(u8g2_font_ncenB08_te);  // 폰트 설정
  u8g2.drawStr(1, 15, " AIBD AIOT"); // "AIBD AIOT"이라는 문자열과, 온도, 습도, 토양습도를 나타내는 문자열을 디스플레이에 출력
  u8g2.drawStr(15, 30, "Temp.");
  u8g2.setCursor(85, 30); // 출력 위치를 설정
  u8g2.print(Temp); // 온도, 습도, 토양습도 값을 출력
  u8g2.drawStr(114, 30, "\xb0");
  u8g2.drawStr(119, 30, "C");
  u8g2.drawStr(15, 43, "Humidity");
  u8g2.setCursor(85, 43); u8g2.print(Humi);
  u8g2.drawStr(116, 43, "%");
  u8g2.drawStr(15, 54, "S-oil");
  u8g2.setCursor(85, 54); u8g2.print(Soilhumi);
  u8g2.drawStr(113, 54, "%");
    u8g2.drawStr(15, 63, "LED");
  u8g2.setCursor(85, 63); u8g2.print(TimeCompare);
  u8g2.drawStr(113, 63, "%");
  u8g2.sendBuffer(); // 호출하여 디스플레이에 내용을 출력
}
