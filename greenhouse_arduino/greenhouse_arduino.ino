#include <WiFi.h>
#include <DHT.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

#define dht_pin 13
#define water_pin 14
#define fan_pin1 12
#define fan_pin2 15

#define DHTTYPE DHT11
DHT dht(dht_pin, DHTTYPE);

#define timer_deep_sleep 30 * 1000000

const char *ssid = "******";
const char *password = "*******";

const char *servername_dht = "http://192.168.1.7:8000/dht_sensor/";
const char *servername_watering = "http://192.168.1.7:8000/watering/";
const char *servername_fan = "http://192.168.1.7:8000/fan/";

void setup()
{
   Serial.begin(115200);

   pinMode(water_pin, OUTPUT);

   pinMode(fan_pin1, OUTPUT);
   pinMode(fan_pin2, OUTPUT);

   dht.begin();

   WiFi.begin(ssid, password);

   Serial.println("________");
   Serial.print("Connecting");
   while (WiFi.status() != WL_CONNECTED)
   {
      delay(500);
      Serial.print(".");
   }

   Serial.print("Connected, IP address: ");
   Serial.println(WiFi.localIP());
   Serial.println("________");
}

void DHT_POST()
{
   HTTPClient http;
   float temperature, humidity;
   String str_temperature, str_humidity;
   StaticJsonDocument<300> doc;
   JsonObject obj1 = doc.to<JsonObject>();
   String postdht;

   temperature = dht.readTemperature();
   humidity = dht.readHumidity();

   if (!isnan(temperature) && !isnan(humidity))
   {
      str_temperature = String(temperature);
      str_humidity = String(humidity);

      if (str_temperature.length() != 0 && str_humidity.length() != 0)
      {
         obj1["temperature"] = str_temperature;
         obj1["humidity"] = str_humidity;
         serializeJson(doc, postdht);

         int httpResponseCode = http.begin(servername_dht);
         http.addHeader("Content-Type", "application/json");
         if (httpResponseCode)
         {
            Serial.print("dht_sensor: ");
            Serial.println(postdht);
            Serial.print("POST DHT: ");
            Serial.println(http.POST(postdht));
         }

         http.end();
      }
   }
}

void Watering_GET()
{
   HTTPClient http_get, http_post;
   StaticJsonDocument<300> doc1;
   StaticJsonDocument<300> doc2;
   JsonObject obj2 = doc2.to<JsonObject>();

   int httpResponseCode = http_get.begin(servername_watering);
   http_get.addHeader("Content-Type", "application/json");
   if (httpResponseCode)
   {
      Serial.print("GET Watering: ");
      Serial.println(http_get.GET());

      String water_get = http_get.getString();
      deserializeJson(doc1, water_get);
      String status = doc1["status"];

      if (status == "True")
      {
         int httpResponseCode = http_post.begin(servername_watering);
         String postwatering;
         http_post.addHeader("Content-Type", "application/json");
         if (httpResponseCode)
         {
            obj2["status"] = "False";
            serializeJson(doc2, postwatering);

            Serial.print("POST Watering: ");
            Serial.println(http_post.POST(postwatering));
         }
         http_post.end();

         // watering for 10s
         digitalWrite(water_pin, HIGH);
         delay(10000);
         digitalWrite(water_pin, LOW);
      }
      else
      {
         http_get.end();
      }
   }
}

void Fan_GET()
{
   HTTPClient http_get, http_post;
   StaticJsonDocument<300> doc3;
   StaticJsonDocument<300> doc4;
   JsonObject obj3 = doc4.to<JsonObject>();

   int httpResponseCode = http_get.begin(servername_fan);
   http_get.addHeader("Content-Type", "application/json");
   if (httpResponseCode)
   {
      Serial.print("GET Fan: ");
      Serial.println(http_get.GET());

      String fan_get = http_get.getString();
      deserializeJson(doc3, fan_get);
      String status = doc3["status"];

      if (status == "True")
      {
         int httpResponseCode = http_post.begin(servername_fan);
         String postfan;
         http_post.addHeader("Content-Type", "application/json");
         if (httpResponseCode)
         {
            obj3["status"] = "False";
            serializeJson(doc4, postfan);

            Serial.print("POST Fan: ");
            Serial.println(http_post.POST(postfan));
         }
         http_post.end();

         // fan Start 10s
         digitalWrite(fan_pin1, HIGH);
         digitalWrite(fan_pin2, LOW);
         delay(10000);
         digitalWrite(fan_pin1, LOW);
         digitalWrite(fan_pin2, LOW);
      }
      else
      {
         http_get.end();
      }
   }
}

void loop()
{
   digitalWrite(water_pin, LOW);
   digitalWrite(fan_pin1, LOW);
   digitalWrite(fan_pin2, LOW);
   if (WiFi.status() == WL_CONNECTED)
   {
      DHT_POST();
      Watering_GET();
      Fan_GET();
   }
   else
   {
      Serial.println("__[ WiFi Disconnected ]__");
   }

   // deep sleep
   // 30s rest for next checking
   esp_sleep_enable_timer_wakeup(timer_deep_sleep);
   esp_deep_sleep_start();
}
