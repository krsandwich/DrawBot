// 
// IMPORTANT: Assumes pencil is in start position
//

#include <AccelStepper.h>
#include <MultiStepper.h>

// Pins for motor 1
#define STEP_PIN_1  3
#define DIR_PIN_1   4

// Pins for motor 2
#define STEP_PIN_2  12
#define DIR_PIN_2   13

// Initialize individual steppers
AccelStepper stepper1(AccelStepper::FULL2WIRE, STEP_PIN_1, DIR_PIN_1);
AccelStepper stepper2(AccelStepper::FULL2WIRE, STEP_PIN_2, DIR_PIN_2);

MultiStepper steppers;

long positions[2];  // Array of desired stepper positions
bool draw; // Whether to draw (pencil down) or not

unsigned long commandsRun; // Number of commands successfully run

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(5);

  listenForPythonScript();

  // Configure each stepper
  // TODO: do speeds do anything?
  stepper1.setMaxSpeed(800);
  stepper2.setMaxSpeed(800);

  // Combine the steppers in a MultiStepper to drive simultaneously
  steppers.addStepper(stepper1);
  steppers.addStepper(stepper2);

  commandsRun = 0;
}

void loop() {
  draw = readCmd(positions);
  // TODO: move up or down

  // Adjust target positions to current positions
  positions[0] += stepper1.currentPosition();
  positions[1] += stepper2.currentPosition();

  // Move the motors
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position

  // Let Python client know command finished
  Serial.println(++commandsRun);
}

//
// Utility Functions
//

bool readCmd(long positions[2]) {
  while (!Serial.available());
  int draw = Serial.readStringUntil(',').toInt();
  positions[0] = Serial.readStringUntil(',').toInt();
  positions[1] = Serial.readStringUntil(',').toInt();
  return draw == 1;
}

void listenForPythonScript() {
  while (!Serial.available());
  String recv = Serial.readString();
  if (recv == "ready") {
    Serial.println("ack");
    return;
  }

  // Stall forever, connection failed
  while (true) {
    delay(60000);
  }
}

void waitForInput() {
  while (!Serial.available());
  int throwaway = Serial.read();
}
