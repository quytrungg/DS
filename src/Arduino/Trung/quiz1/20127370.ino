// initialize port for red, yellow and green
int green = 2, yellow = 4, red = 7;

void setup()
{
  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);
}

void loop()
{
  // turn on green LED for 7s
  digitalWrite(green, HIGH);
  delay(7000); // Wait for 7000 millisecond(s)
  digitalWrite(green, LOW);
  
  // turn on yellow LED for 4s
  digitalWrite(yellow, HIGH);
  delay(4000); // Wait for 4000 millisecond(s)
  digitalWrite(yellow, LOW);
  
  // turn on red LED for 5s
  digitalWrite(red, HIGH);
  delay(5000); // Wait for 5000 millisecond(s)
  digitalWrite(red, LOW);
}