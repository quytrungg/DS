int port = 7;
int button = 12;

void setup() {
  // put your setup code here, to run once:
  pinMode(button, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int buttonState = digitalRead(button);
  
  if (buttonState == HIGH) {
    int start = millis();
    while(digitalRead(button) == HIGH){
    }
    int end = millis();
      if(end - start >= 5000){
        Serial.println("Reset");
      }
  }
}
