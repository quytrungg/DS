int trig_pin = 2, echo_pin = 3;
int led = 7;

void setup(){
  Serial.begin(9600);

  pinMode(trig_pin, INPUT);
  pinMode(echo_pin, INPUT);
  pinMode(led, OUTPUT);
}

void loop(){
  int status = digitalRead(trig_pin);
  if(status){
    digitalWrite(led, HIGH);
  }
  else{
    digitalWrite(led, LOW);
  }
}