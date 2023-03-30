#include <U8g2lib.h>
#include "DHT.h"
#include <SoftPWM.h>
#include <Adafruit_Sensor.h>

U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);

#define DHTPIN A1
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);
SOFTPWM_DEFINE_CHANNEL(A3);

uint32_t DataCaptureDelay = 3000;
uint32_t DataCapture_ST = 0;

float Temp;
float Humi;
float FanPWM;

void setup() {
  dht.begin();
  u8g2.begin();
  SoftPWM.begin(490);

  DataCapture_ST = millis();
  
}

void loop() {
  if((millis() - DataCapture_ST) > DataCaptureDelay) {
    Humi = dht.readHumidity();
    Temp = dht.readTemperature();

  if(isnan(Humi) || isnan(Temp)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  if(Temp >= 30) {
      FanPWM = 100;   // 30도 이상이면 FAN ON (PWM:100)
  } else if(Temp > 25) {
      FanPWM = 65;   // 25도 초과이면 FAN PWM 65로 ON
  } else {
      FanPWM = 0;   // 25도 이하이면 FAN OFF (PWM:0)
  }
    SoftPWM.set(FanPWM);   // PWM 값 설정


  OLEDdraw();
  DataCapture_ST = millis();
  }
}

void OLEDdraw() {
  u8g2.clearBuffer();

  u8g2.setFont(u8g2_font_ncenB08_te);
  u8g2.drawStr(1, 15, " AIBD AIOT");

  u8g2.drawStr(15, 36, "Temp.");
  u8g2.setCursor(85, 36);
  u8g2.print(Temp);
  u8g2.drawStr(114, 36, "\xb0");
  u8g2.drawStr(119, 36, "C");

  u8g2.drawStr(15, 47, "Humidity");
  u8g2.setCursor(85, 47); u8g2.print(Humi);
  u8g2.drawStr(116, 47, "%");

  u8g2.drawStr(15, 58, "FanPWM");
  u8g2.setCursor(85, 58); u8g2.print(FanPWM);
  

  u8g2.sendBuffer();
}
