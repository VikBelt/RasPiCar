/* YourDuino SKETCH UltraSonic Serial 2.0
 Runs HC-04 and SRF-06 and other Ultrasonic Modules
 Open Serial Monitor to see results
 Reference: http://playground.arduino.cc/Code/NewPing
 CODE REFERENCE: https://arduinoinfo.mywikis.net/wiki/UltraSonicDistance
 Questions?  terry@yourduino.com */

/*-----( Import needed libraries )-----*/
#include <NewPing.h>
/*-----( Declare Constants and Pin Numbers )-----*/
#define  TRIGGER_PIN  2
#define  ECHO_PIN     3

#define MAX_DISTANCE 400 // Maximum distance we want to ping for (in centimeters).
                         //Maximum sensor distance is rated at 400-500cm.
/*-----( Declare objects )-----*/
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.
/*-----( Declare Variables )-----*/
int DistanceIn;
int DistanceCm;

void setup()   /****** SETUP: RUNS ONCE ******/
{
  Serial.begin(9600);
  Serial.println("UltraSonic Distance Measurement");
  Serial.println("YourDuino.com  terry@yourduino.com");
}//--(end setup )---


void loop()   /****** LOOP: RUNS CONSTANTLY ******/
{
  delay(50);// Wait 100ms between pings (about 10 pings/sec). 29ms should be the shortest delay between pings.
  DistanceIn = sonar.ping_in();
  Serial.print("Ping: ");
  Serial.print(DistanceIn); // Convert ping time to distance and print result 
                            // (0 = outside set distance range, no ping echo)
  Serial.print(" in     ");

  delay(50);// Wait 100ms between pings (about 10 pings/sec). 29ms should be the shortest delay between pings.
  DistanceCm = sonar.ping_cm();
  Serial.print("Ping: ");
  Serial.print(DistanceCm);
  Serial.println(" cm");

}//--(end main loop )---

/*-----( Declare User-written Functions )-----*/

// None
//*********( THE END )***********
