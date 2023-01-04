// Library for LCD 
#include <LiquidCrystal.h> 

LiquidCrystal lcd_1(12, 11, 5, 4, 3, 2); // Initialize LCD ports
int temp = A0, button = 7, state = 0;

void setup()
{
  pinMode(temp, INPUT);
  pinMode(button, INPUT);
  lcd_1.begin(16, 2); // Set up the number of columns and rows on the LCD
  Serial.begin(9600);
}

void loop()
{
  if(digitalRead(button) && state == 0){
    lcd_1.clear();
    while(!digitalRead(button)){
      lcd_1.setCursor(5,0);
      lcd_1.print("CLASS");
      lcd_1.setCursor(4,1);
      lcd_1.print("20CLC11");
      lcd_1.display();
      if(digitalRead(button)){
        state = (state+1) % 3;
        lcd_1.noDisplay();
      }
    }
  }    
  
  if(digitalRead(button) && state == 1){
    lcd_1.clear();
   	while(!digitalRead(button)){
      lcd_1.setCursor(2,0);
      lcd_1.print("MAI QUY TRUNG");
      lcd_1.setCursor(4,1);
      lcd_1.print("20127370");
      int check = millis();
      while(millis() - check <= 500 && !digitalRead(button)){
        lcd_1.display();
      }
      check = millis();
      while(millis() - check <= 500 && !digitalRead(button)){
        lcd_1.noDisplay();
      }
   	  if(digitalRead(button)){
        state = (state+1) % 3; 
        lcd_1.noDisplay();
      }
    }
  } 
  
  if(digitalRead(button) && state == 2){
    lcd_1.clear();
    while(!digitalRead(button)){
      float value = analogRead(temp);
      lcd_1.setCursor(2, 0);
      lcd_1.print("TEMP: ");
      lcd_1.print(((value * 5 / 1023) / 0.01) - 50);
      lcd_1.display();
      if(digitalRead(button)){
        state = (state+1) % 3;
        lcd_1.noDisplay();
      }
    }
  }
}