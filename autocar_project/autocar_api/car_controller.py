from config import Config

class CarController:
    def __init__(self):
        self.speed = 0
        self.steering_angle = 0
        
        # [HARDWARE] 실제 모터 드라이버 및 서보모터 라이브러리 초기화 위치
        # 예: self.pwm = PCA9685()
        print("[Mock] CarController 초기화 완료 (하드웨어 시뮬레이션 모드)")

    def set_motor(self, speed):
        # 범위 검증
        speed = max(Config.LIMIT_SPEED_MIN, min(Config.LIMIT_SPEED_MAX, speed))
        self.speed = speed
        
        # [HARDWARE] 실제 하드웨어에 속도 값 적용 코드 작성 위치
        # if speed >= 0: go_forward(speed) else: go_backward(abs(speed))
        print(f"[Mock] 모터 구동 설정 -> 속도: {self.speed}")
        return self.speed

    def set_steering(self, angle):
        # 범위 검증
        angle = max(Config.LIMIT_STEER_MIN, min(Config.LIMIT_STEER_MAX, angle))
        self.steering_angle = angle
        
        # [HARDWARE] 실제 조향 서보모터 제어 코드 작성 위치
        # self.servo.set_angle(angle)
        print(f"[Mock] 조향 방향 설정 -> 각도: {self.steering_angle}°")
        return self.steering_angle

    def process_joystick(self, x, y):
        """
        x, y: -1.0 ~ 1.0 범위의 조이스틱 입력
        x는 조향(-45 ~ 45), y는 속도(-100 ~ 100)로 변환
        """
        target_speed = int(y * Config.LIMIT_SPEED_MAX)
        target_steer = int(x * Config.LIMIT_STEER_MAX)
        
        self.set_motor(target_speed)
        self.set_steering(target_steer)

    def emergency_stop(self):
        self.set_motor(0)
        self.set_steering(0)
        print("[Mock] !!! 긴급 정지 수행 완료 !!!")