
int s1=2,s2=3;
    int value1,value2;
#include <Servo.h>

Servo myservo1;
Servo myservo2;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  myservo1.attach(9);
  myservo2.attach(10);
  pinMode(s1,INPUT);
  pinMode(s2,INPUT);
  // attaches the servo on pin 9 to the servo object
}
void S1()
{
  value1=digitalRead(s1);
  }
 void S2()
 {
  value2=digitalRead(s2);
 }
void loop() {
  S1();
  S2();
  if(value1==1 && value2==1)
  {
     // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo1.write(90);
    myservo2.write(90);// tell servo to go to position in variable 'pos'
  }                       // waits 15ms for the servo to reach the position
  
  else
  { // goes from 180 degrees to 0 degrees
    myservo1.write(0);
    myservo2.write(180);// tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  }
  

