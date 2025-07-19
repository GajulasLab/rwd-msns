#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <TinyGPSPlus.h>

// OLED setup
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

// GPS setup
HardwareSerial gpsSerial(1);
TinyGPSPlus gps;

// Destination coordinates
double dest_lat = 43.77870127701418;
double dest_lng = -79.30889250152855;
bool isNearDestination = false;

void setup() {
  Serial.begin(9600);
  gpsSerial.begin(9600, SERIAL_8N1, 16, 17); // RX=16, TX=17
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
}

void loop() {
  while (gpsSerial.available() > 0) {
    gps.encode(gpsSerial.read());
  }

  if (gps.location.isUpdated()) {
    double lat = gps.location.lat();
    double lng = gps.location.lng();
    double distance = calculateDistance(lat, lng, dest_lat, dest_lng);
    
    Serial.print("Distance to destination: ");
    Serial.println(distance);

    if (distance < 200) {
      isNearDestination = true;
    } else {
      isNearDestination = false;
    }

    display.clearDisplay();
    display.setTextSize(1);
    display.setCursor(0, 0);
    display.print("Sat: ");
    display.println(gps.satellites.value());

    if (isNearDestination) {
      display.setTextSize(3);
      display.setCursor(40, 20);
      display.print("P");
    } else {
      display.setTextSize(1);
      display.setCursor(0, 20);
      display.print("On Route");
    }
    display.display();
  }
  delay(500);
}

double calculateDistance(double lat1, double lon1, double lat2, double lon2) {
  const double R = 6371000; // Radius of Earth in meters
  double dLat = radians(lat2 - lat1);
  double dLon = radians(lon2 - lon1);
  double a = sin(dLat / 2) * sin(dLat / 2) +
             cos(radians(lat1)) * cos(radians(lat2)) *
             sin(dLon / 2) * sin(dLon / 2);
  double c = 2 * atan2(sqrt(a), sqrt(1 - a));
  return R * c;
}
