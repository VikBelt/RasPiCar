/* 
 *  Header file for GY521 gyroscope and accelerometer
 *  By Vikram Belthur - 7.30.2020
 *  Reference: https://electrosome.com/interfacing-mpu-6050-gy-521-arduino-uno/
*/

#ifndef _GY521_H //include guard
#define _GY521_H

#include <math.h>
#include <Wire.h>
#include <stdint.h>

#define PI 3.14159265 //define a PI value

//interface for the IMU
class GY521 {
public:
  //imu methods
  GY521();
  void readTemp();
  void readGyro();
  void readAccel();
  double tempCelsius();
  void getAngle();
  //imu fields
  const int MPU = 104; //0x68 in Hex
  int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;
  int acxCal,acyCal,aczCal,gyxCal,gyyCal,gyzCal,tempCal; //calibration variables
  double celsius,tx,pitch,roll;  
};

inline double fahrenheit(double cel ){
  return (cel * 9/5) + 32;
}

inline double deg(double rad){
  return (rad * 180)/PI;
}

#endif
