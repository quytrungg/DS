int trig_pin = 2, echo_pin = 3, buzzer = 5;
int led1 = 8, led2 = 7, led3 = 4;

long getDistance(){
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);

  return pulseIn(echo_pin, HIGH) * 0.0343 / 2;
}

void systemStatus(int l1, int l2, int l3, int b){
  digitalWrite(led1, l1);
  digitalWrite(led2, l2);
  digitalWrite(led3, l3);
  analogWrite(buzzer, b);
}

void setup(){
  Serial.begin(9600);
  pinMode(trig_pin, OUTPUT);
  pinMode(echo_pin, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop(){
  if(getDistance() >= 150){
    systemStatus(HIGH, LOW, LOW, LOW);
  }
  else if(getDistance() > 50 and getDistance() < 150){
  	systemStatus(LOW, HIGH, LOW, 10);
    delay(1000);
    digitalWrite(led2, LOW);
    digitalWrite(buzzer, LOW);
    delay(1000);
  }
  else{
  	systemStatus(HIGH, HIGH, HIGH, 10);
    delay(getDistance() * 10);
    systemStatus(LOW, LOW, LOW, LOW);
    delay(getDistance() * 10);
  }
}