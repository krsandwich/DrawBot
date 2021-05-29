/*  Drawbot testing 
 *  Checking stepper motor functioning
 *
 *  modified from Dejan Nedelkovski, www.HowToMechatronics.com
 *  by Amy Dunphy, 5/3/21
 */

// defines pins numbers
const int stepPin1 = 3; 
const int dirPin1 = 4; 
const int stepPin2 = 12; 
const int dirPin2 = 13; 
 
void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPin1,OUTPUT); 
  pinMode(dirPin1,OUTPUT);
  pinMode(stepPin2,OUTPUT); 
  pinMode(dirPin2,OUTPUT);
}

void loop() {
  digitalWrite(dirPin1,HIGH); // Enables the motor to move in a particular direction
  digitalWrite(dirPin2,HIGH); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 100; x++) {
    digitalWrite(stepPin1,HIGH); 
    digitalWrite(stepPin2,HIGH); 
    delayMicroseconds(1000); 
    digitalWrite(stepPin1,LOW); 
    digitalWrite(stepPin2,LOW); 
    delayMicroseconds(100); 
  }

  digitalWrite(dirPin1,HIGH); // Enables the motor to move in a particular direction
  digitalWrite(dirPin2,LOW); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x <100; x++) {
    digitalWrite(stepPin1,HIGH); 
    digitalWrite(stepPin2,HIGH); 
    delayMicroseconds(1000); 
    digitalWrite(stepPin1,LOW); 
    digitalWrite(stepPin2,LOW); 
    delayMicroseconds(100); 
  }

  digitalWrite(dirPin1,LOW); // Enables the motor to move in a particular direction
  digitalWrite(dirPin2,LOW); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 100; x++) {
    digitalWrite(stepPin1,HIGH); 
    digitalWrite(stepPin2,HIGH); 
    delayMicroseconds(1000); 
    digitalWrite(stepPin1,LOW); 
    digitalWrite(stepPin2,LOW); 
    delayMicroseconds(100); 
  }

  digitalWrite(dirPin1,LOW); // Enables the motor to move in a particular direction
  digitalWrite(dirPin2,HIGH); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 100; x++) {
    digitalWrite(stepPin1,HIGH); 
    digitalWrite(stepPin2,HIGH); 
    delayMicroseconds(1000); 
    digitalWrite(stepPin1,LOW); 
    digitalWrite(stepPin2,LOW); 
    delayMicroseconds(100); 
  }

  delay(1000); // One second delay
  
}
