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
    int check = millis();
    while(digitalRead(button)){ // Button is clicked and held
      	if(millis() - start > 12000)
          	modifyAllLed(led, numOfLed, turnOnAllLed);
        else{ // Duration <= 12s
      		digitalWrite(led[idx], HIGH);
          	if(millis() - check >= 1000){ // After 1s change LED
              	digitalWrite(led[idx], LOW);
              	idx = (idx + 1) % numOfLed;
          		check = millis();	
            }
      	}
    }
  }	
  modifyAllLed(led, numOfLed, turnOffAllLed);
}