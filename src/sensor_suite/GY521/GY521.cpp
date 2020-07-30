/* 
 *  Implementation file for the GY521
 *  Vikram Belthur - 7/30/2020
 *  Source: https://electrosome.com/interfacing-mpu-6050-gy-521-arduino-uno/
 *  Refer to Registers in the MPU6050 Data Sheet
*/

#include "GY521.h"

//constructor data correction
GY521::GY521(){
    //Acceleration data correction
    acxCal = -950;
    acyCal = -300;
    aczCal = 0;
    //Temperature correction
    tempCal = -1600;
    //Gyro correction
    gyxCal = 480;
    gyyCal = 170;
    gyzCal = 210;
}

//read temperatue from registers - 0x41 (TEMP_OUT_H) 0x42 (TEMP_OUT_L) 
void GY521::readTemp(){
  Tmp = (int16_t)Wire.read()<<8; //bitshift - multipy by 256
  Tmp |= Wire.read(); //bitwise OR
}

//read gyroscope data from registers 0x43 (GYRO_XOUT_H) to 0x48 (GYRO_ZOUT_L) 
void GY521::readGyro(){
  GyX = (int16_t)Wire.read()<<8;
  GyX |= Wire.read();  
  GyY = (int16_t)Wire.read()<<8;
  GyY |= Wire.read();
  GyZ= (int16_t)Wire.read()<<8;
  GyZ |= Wire.read(); 
}

//read accelration data from registers 0x3B (ACCEL_XOUT_H) to 0x40 (ACCEL_ZOUT_L)
void GY521::readAccel(){
  AcX = (int16_t)Wire.read()<<8;
  AcX |= Wire.read();  
  AcY = (int16_t)Wire.read()<<8;
  AcY |= Wire.read();
  AcZ = (int16_t)Wire.read()<<8;
  AcZ |= Wire.read(); 
}

//get temperature from sensor in celsius
double GY521::tempCelsius(){
  tx  = Tmp + tempCal;
  celsius = tx/340 + 36.50; //value aquired from datasheet
  return celsius;
}

//get values for pitch and roll from accelerometer
void GY521::getAngle(){
    pitch = atan(AcX/sqrt((AcY*AcY) + (AcZ*AcZ))); //pitch calculation
    roll = atan(AcY/sqrt((AcX*AcX) + (AcZ*AcZ))); //roll calculation
    pitch = deg(pitch); //want degree angles
    roll = deg(roll);
}
