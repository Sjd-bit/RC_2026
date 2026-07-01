import os

class Config:
    HOST = "0.0.0.0"
    PORT = 8000
    
    # 제어 제한값 설정
    LIMIT_SPEED_MIN = -100
    LIMIT_SPEED_MAX = 100
    LIMIT_STEER_MIN = -45
    LIMIT_STEER_MAX = 45
    
    LIMIT_PAN_MIN = 0
    LIMIT_PAN_MAX = 180
    LIMIT_TILT_MIN = 0
    LIMIT_TILT_MAX = 180