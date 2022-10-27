int photo = A0, led = 2;

void setup(){
  pinMode(photo, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);	
}

void loop(){
  int intensity = analogRead(photo);
  if(intensity < 500){
  	digitalWrite(led, HIGH);
  }
  else{
  	digitalWrite(led, LOW);
  }
}