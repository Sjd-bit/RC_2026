import cv2
import numpy as np
import time
from config import Config

class CameraController:
    def __init__(self):
        self.pan = 90
        self.tilt = 90
        
        # [HARDWARE] 실제 카메라 Pan/Tilt 서보모터 인덱스 정의 위치
        
        # OpenCV 카메라 초기화 시도
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("[Mock] 실제 카메라를 찾을 수 없어 더미 이미지 스트리밍 모드로 전환합니다.")
            self.cap = None

    def set_pan_tilt(self, pan, tilt):
        self.pan = max(Config.LIMIT_PAN_MIN, min(Config.LIMIT_PAN_MAX, pan))
        self.tilt = max(Config.LIMIT_TILT_MIN, min(Config.LIMIT_TILT_MAX, tilt))
        
        # [HARDWARE] 실제 서보모터 구동 제어 코드 작성 위치
        print(f"[Mock] 카메라 서보 이동 -> Pan: {self.pan}°, Tilt: {self.tilt}°")
        return self.pan, self.tilt

    def generate_frames(self):
        while True:
            if self.cap is not None:
                success, frame = self.cap.read()
                if not success:
                    frame = self._create_dummy_frame()
            else:
                frame = self._create_dummy_frame()
                time.sleep(0.06)  # 약 15 FPS 유지를 위한 대기

            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
                
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

    def _create_dummy_frame(self):
        """카메라가 없을 때 표시할 가상화면 생성"""
        img = np.zeros((480, 640, 3), dtype=np.uint8)
        # 배경에 간단한 그라데이션 패턴 주입하여 멈춰있지 않음을 표시
        pulse = int((time.time() * 50) % 100)
        cv2.putText(img, "Camera Not Available", (120, 220), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(img, f"Status: Simulated Video Feed ({pulse})", (120, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        cv2.rectangle(img, (50, 50), (590, 430), (0, 255, 0), 2)
        return img