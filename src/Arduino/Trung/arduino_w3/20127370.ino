// Initialize LEDs' ports, button port and number of LEDs
int led[6] = {2, 4, 7, 8, 12, 13};
int button = 11, numOfLed = 6;

// Setup all the LEDs and button
void setup()
{
  for(int i = 0; i < numOfLed; ++i){
  	pinMode(led[i], OUTPUT);
  }
  pinMode(button, INPUT);
  Serial.begin(9600);
}

// Function to check if LED is HIGH and button is LOW,
// the LED will turn off right away
void checkLed(){
  	for(int i = 0; i < 10; ++i){
  		if(!digitalRead(button)){
  			return;
    	}
      	delay(100);
    }
}

// Function to turn a LED on for 1s and then off
void turnOnLed(int led){
	digitalWrite(led, HIGH);
  	checkLed();
    digitalWrite(led, LOW);
}

// Function to turn on all of the LEDs
void turnOnAllLed(int* arr, int n){
	for(int i = 0; i < n; ++i){
    	digitalWrite(arr[i], HIGH);
    }
}

// Function to turn off all of the LEDs
void turnOffAllLed(int* arr, int n){
	for(int i = 0; i < n; ++i){
    	digitalWrite(arr[i], LOW);
    }
}

// Function pointer to control the LEDS to turn on/off
void modifyAllLed(int* arr, int n, void (*p) (int*, int)){
	p(arr, n);
}

// Loop function
void loop()
{
  int buttonState = digitalRead(button);
  
  if (buttonState) { // Button is clicked
    int start = millis(), idx = 0;
    while(digitalRead(button)){ // Button is clicked and held
      	if(millis() - start <= 12000){ // Duration <= 12s
      		turnOnLed(led[idx]);
          	idx = (idx + 1) % numOfLed;
      	}
      	else modifyAllLed(led, numOfLed, turnOnAllLed);
    }
  }	
  modifyAllLed(led, numOfLed, turnOffAllLed);
}