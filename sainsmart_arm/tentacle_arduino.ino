/**
 * Servo control code for our SainSmart Arm, which will be used to test things until the Tentacle is functional
 */
#include <Servo.h>

/*
 * Pin Servo
 * 3   0
 * 5   1
 * 6   2
 * 8   3
 * 9   4
 * 11  5
 */
 
const int baud = 9600;
const int servoCount = 6;
int servoPins[servoCount] = { 3, 5, 6, 8, 9, 11 };
Servo servos[servoCount];

const int minPulseWidth = 700;
const int maxPulseWidth = 1200;

void setup() {

  for (int i = 0; i < servoCount; i++) {
    servos[i].attach(servoPins[i], minPulseWidth, maxPulseWidth);
    // Debug
    Serial.print("Servo:");
    Serial.print(i);
    Serial.print(" attached to pin ");
    Serial.println(servoPins[i]);
  }

  Serial.begin(baud);  
  Serial.print("ServoControl Ready");
}

//
// Main loop
//
void loop() {
  static int v = 0; // We'll accumulate our value here
  if ( Serial.available() ) {
    char ch = Serial.read();
    switch (ch) {
      case '0'...'9':
        v = v * 10 + ch - '0';
        break;
      case 'A'...'F':
        v = abs(v) % 180; // Sanity check: Servo range is 0-180
        int servoId = ch - 'A'; // Convert A...F to 0...5
        servos[servoId].write(v);
        v = 0;

        // Debug Output
        Serial.print(servoId);
        Serial.print("=");
        Serial.println(v);        
        break;
    }
  }
}
