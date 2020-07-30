/*
 * Sketch to Interface with the GY-521 - Vikram Belthur - 7/30/2020
 * Source: https://electrosome.com/interfacing-mpu-6050-gy-521-arduino-uno/
*/

#include <Wire.h> //allows I2C comms.
#include "GY521.h" 

GY521 imuSensor; //global instance of the GY521
void setup(){

  Wire.begin();
  Wire.beginTransmission(imuSensor.MPU);
  Wire.write(0x6B);  
  Wire.write(0);
  Wire.endTransmission(true);
  Serial.begin(9600); //set baud rate to 9600
}

void loop(){
  //I2C setup - begin and restart i2c comms. to the device registers
  Wire.beginTransmission(imuSensor.MPU);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(imuSensor.MPU,14,true); //request 14 registers in total  
  
  //get values
  imuSensor.readAccel(); //read acceleration
  imuSensor.readTemp(); //read temperature
  imuSensor.readGyro(); //read gyroscope
  double celsius = imuSensor.tempCelsius(); //meaningful temp values
  double fahr = fahrenheit(celsius); 
  imuSensor.getAngle(); //get pitch and roll

   //write to serial port
   Serial.print("Angle: ");
   Serial.print("Pitch = "); Serial.print(imuSensor.pitch);
   Serial.print(" Roll = "); Serial.println(imuSensor.roll);
  
   Serial.print("Accelerometer: ");
   Serial.print("X = "); Serial.print(imuSensor.AcX + imuSensor.acxCal);
   Serial.print(" Y = "); Serial.print(imuSensor.AcY + imuSensor.acyCal);
   Serial.print(" Z = "); Serial.println(imuSensor.AcZ + imuSensor.aczCal); 

   Serial.print("Temperature in celsius = "); Serial.print(celsius);  
   Serial.print(" fahrenheit = "); Serial.println(fahr);  
  
   Serial.print("Gyroscope: ");
   Serial.print("X = "); Serial.print(imuSensor.GyX + imuSensor.gyxCal);
   Serial.print(" Y = "); Serial.print(imuSensor.GyY + imuSensor.gyyCal);
   Serial.print(" Z = "); Serial.println(imuSensor.GyZ + imuSensor.gyzCal);  
   delay(1000);
}
