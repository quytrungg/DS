// Library for LCD 
#include <LiquidCrystal.h> 

LiquidCrystal lcd_1(12, 11, 5, 4, 3, 2); // Initialize LCD ports
int port = A0;

void setup()
{
  pinMode(port, INPUT);
  lcd_1.begin(16, 2); // Set up the number of columns and rows on the LCD
  lcd_1.print("hello world!"); // LCD initial print
  Serial.begin(9600);
}

void loop()
{
  float tmp_value = analogRead(port);
  float t = ((tmp_value*5 / 1023) / 0.01) - 50; // convert analog value to temp
  lcd_1.setCursor(0, 1); // set cursor to correct position
  lcd_1.print(t);
}