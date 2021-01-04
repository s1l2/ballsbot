# Miniature self driving car

<img caption="robot photo" src="https://github.com/jumpercc/ballsbot/blob/master/images/car-photo.jpg?raw=true" width="400" />

**TODO!!!** link to youtube video

## Requirements

### Hardware

- Remo Hobby Smax 1:16 RH1635 (strongly recommend) / RH1631
- E9631 Brushless Motor For Remo 1/16 smax (only for RH1631. RH1635 already has one)
- SURPASS HOBBY KK 35A ESC Waterproof Electric Speed Controller for 1/16 RC Car Brushless Motor Power system [aliexpress](https://www.aliexpress.com/item/4000004474965.html?spm=a2g0s.9042311.0.0.264d4c4da73utK&_ga=2.261127435.707005012.1606162973-254637839.1604956961)
- Nvidia Jetson Nano Developer Kit [aliexpress](https://www.aliexpress.com/item/4000765500472.html?spm=a2g0s.9042311.0.0.264d4c4da73utK&_ga=2.227629467.707005012.1606162973-254637839.1604956961)
- 64 GB micro sd card
- inner (not usb!) wi-fi card like [that one](https://www.aliexpress.com/item/4000144144831.html?spm=a2g0s.9042311.0.0.264d4c4dIbFbdb&_ga=2.17781439.707005012.1606162973-254637839.1604956961) and IPEX Connector antennas for it
- Two KY-003 hall sensor module for Arduino [aliexpress](https://www.aliexpress.com/item/32907115789.html?spm=a2g0s.9042311.0.0.264d33ediabTe4&_ga=2.262754314.707005012.1606162973-254637839.1604956961)
- neodymium magnet about 20x3x2 mm size
- IMX219 Camera 8MP Infrared Night Vision 160 Degree FOV + 2 Infrared LED Lights [aliexpress](https://www.aliexpress.com/item/4000215557127.html?spm=a2g0s.9042311.0.0.264d33edRYxD3h&_ga=2.262165514.707005012.1606162973-254637839.1604956961)
- T208 or T200 18650 UPS HAT Shield for NVIDIA Jetson Nano Developer Kit [aliexpress](https://www.aliexpress.com/item/4001332826343.html?spm=a2g0o.productlist.0.0.6b951b58Dgy7Zt&algo_pvid=f4f1dcfa-3376-4cd3-b50b-8c0612ee4dc9&algo_expid=f4f1dcfa-3376-4cd3-b50b-8c0612ee4dc9-0&btsid=21135c3416062408418056167e417b&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_)
- 6 (for T208) or 4 (for T200) 18650 Lithium Rechargeable Battery [aliexpress](https://www.aliexpress.com/item/32807032859.html?spm=a2g0s.9042311.0.0.264d33edRYxD3h&_ga=2.220166815.707005012.1606162973-254637839.1604956961)
- YDLIDAR X2L or similar [aliexpress](https://www.aliexpress.com/item/4000018415971.html?spm=a2g0s.9042311.0.0.264d4c4dFaR0Zo&_ga=2.195525162.707005012.1606162973-254637839.1604956961)
- 9-DOF IMU BNO055 [aliexpress](https://www.aliexpress.com/item/32805406886.html?spm=a2g0s.9042311.0.0.264d4c4dFaR0Zo&_ga=2.27778618.707005012.1606162973-)
- PCA9685 16 Channel 12-bit PWM Servo motor Driver I2C [aliexpress](https://www.aliexpress.com/item/4000468996665.html?spm=a2g0s.9042311.0.0.264d4c4dFaR0Zo&_ga=2.165131705.707005012.1606162973-254637839.1604956961)
- 4 Channel IIC I2C Logic Level Converter Bi-Directional Module 5V to 3.3V [aliexpress](https://www.aliexpress.com/item/32771873030.html?spm=a2g0s.9042311.0.0.264d4c4dFaR0Zo&_ga=2.165131705.707005012.1606162973-254637839.1604956961)
- short USB - USB-C data cable like [this one](https://www.aliexpress.com/item/32771873030.html?spm=a2g0s.9042311.0.0.264d4c4dFaR0Zo&_ga=2.165131705.707005012.1606162973-254637839.1604956961)
- access to 3D printer
- tools

### Software

- JetPack 4.4
- code from this repo
- ROS
- **TODO!!!**
- [YDLidar-SDK](https://github.com/YDLIDAR/YDLidar-SDK) for lidar
- [JHPWMDriver](https://github.com/jetsonhacks/JHPWMDriver.git) for PCA9685
- [RTIMULib](https://github.com/jetsonhacks/RTIMULib.git) for IMU
- [mt7610u-linksys-ae6000-wifi-fixes](https://github.com/xtknight/mt7610u-linksys-ae6000-wifi-fixes.git) if your wi-fi module has not supported by jetson by default
