# IoT Parking System

## Description
본 프로젝트는 초음파 센서를 활용하여 차량과의 거리를 실시간으로 측정하고, 설정된 임계값에 따라 LED 및 부저를 제어하는 IoT 기반 주차 보조 시스템입니다.

## Features
- 초음파 센서를 이용한 거리 측정
- 실시간 데이터 처리
- 임계값 기반 경고 시스템 (LED 및 부저)
- 차량 접근 시 자동 알림 기능

## System Flow
1. 초음파 센서를 통해 거리 측정
2. 측정된 데이터를 실시간으로 처리
3. 설정된 임계값과 비교
4. 위험 거리일 경우 LED 및 부저 작동

## Tech Stack
- Python
- Raspberry Pi (RPi.GPIO)
- Ultrasonic Sensor

## Key Learning
- 센서 데이터를 활용한 실시간 처리 로직 구현
- 이벤트 기반 제어 시스템 설계
- IoT 환경에서의 하드웨어-소프트웨어 연동 이해

## Note
본 프로젝트는 IoT 시스템의 기본 구조와 데이터 처리 과정을 이해하기 위해 수행되었습니다.
