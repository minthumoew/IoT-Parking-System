import RPi.GPIO as GPIO
import time

# GPIO 핀 설정
TRIG_PIN = 20       # 초음파 센서 TRIG 핀 (GPIO 20, PIN 38)
ECHO_PIN = 21       # 초음파 센서 ECHO 핀 (GPIO 21, PIN 40)
BUZZER_PIN = 15     # 부저 핀 (GPIO 15, PIN 10)
LED_PIN = 14        # LED 핀 (GPIO 14, PIN 8)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO 핀 설정
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)

# LED와 부저 초기 상태 (꺼짐)
GPIO.output(BUZZER_PIN, GPIO.LOW)
GPIO.output(LED_PIN, GPIO.LOW)

# 초음파 센서를 사용하여 거리 측정 함수
def get_distance():
    """
    초음파 센서를 사용하여 거리 측정.
    :return: 측정된 거리 (cm).
    """
    # TRIG 핀에 펄스 신호 출력
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)  # 10μs 동안 HIGH 유지
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # ECHO 핀에서 펄스 신호를 수신
    pulse_start, pulse_end = time.time(), time.time()
    
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()

    # 시간 차이를 거리로 변환
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # 단위: cm
    return round(distance, 2)

# LED와 부저 상태 업데이트 함수
def update_alert(distance, threshold=50):
    """
    거리에 따라 LED와 부저를 업데이트.
    :param distance: 측정된 거리 (cm).
    :param threshold: 경고 거리 임계값 (기본값: 50cm).
    """
    if distance < threshold:
        print(f"경고! 물체가 {distance} cm 거리에 있습니다.")
        GPIO.output(LED_PIN, GPIO.HIGH)    # LED 켜짐
        GPIO.output(BUZZER_PIN, GPIO.HIGH) # 부저 켜짐
    else:
        print(f"안전 거리 유지 중: {distance} cm")
        GPIO.output(LED_PIN, GPIO.LOW)    # LED 꺼짐
        GPIO.output(BUZZER_PIN, GPIO.LOW) # 부저 꺼짐

# 메인 프로그램
try:
    while True:
        print("초음파 센서로 거리 측정 중…")
        distance = get_distance()
        print(f"측정된 거리: {distance} cm")
        
        # LED와 부저 업데이트
        update_alert(distance)

        time.sleep(2)  # 2초 대기 후 다시 측정

except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    GPIO.cleanup()  # GPIO 핀 초기화
    print("GPIO 핀 초기화 완료")