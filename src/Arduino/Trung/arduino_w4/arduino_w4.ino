#include <Servo.h>
Servo myservo;

void setup(){
  myservo.attach(9);
}

void loop(){
  myservo.write(90);
  delay(100);
  myservo.write(180);
  delay(100);
  myservo.write(270);
  delay(100);
  myservo.write(0);
  delay(100);
}