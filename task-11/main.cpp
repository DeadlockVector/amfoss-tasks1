#include <Adafruit_LiquidCrystal.h>
#include <Servo.h>

Adafruit_LiquidCrystal lcd_1(0);
Servo myservo;

int ldr_pin=A1;
int servo_pin = 8;
int ldr_reading;

void setup()
{
  lcd_1.begin(16, 2);
  myservo.attach(servo_pin);
  Serial.begin(9600);
  
  myservo.write(0);
  lcd_1.print("Initialising");
  delay(500);
  lcd_1.clear();
}

void loop()
{
  ldr_reading = analogRead(ldr_pin);
  Serial.println(ldr_reading);
  
  if (ldr_reading>860)
  {
    lcd_1.clear();
  	lcd_1.print("ROOF CLOSED");
    myservo.write(0);
  }
  else
  {
    lcd_1.clear();
 	lcd_1.print("ROOF OPEN");
    myservo.write(180);
  }
}