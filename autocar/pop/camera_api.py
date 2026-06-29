import cv2
import threading
from flask import Flask, render_template_string, Response

app = Flask(__name__)

# 전역 변수로 프레임 및 스레드 제어 변수 선언
output_frame = None
lock = threading.Lock()

def capture_frames():
    global output_frame, lock
    
    # [중요] 기존에 작동한다던 GStreamer 파이프라인 문자열을 표준 규격으로 직접 선언합니다.
    # Jetson 보드의 하드웨어 가속(nvarguscamerasrc)을 사용하는 최적의 파이프라인입니다.
    cam = (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), width=640, height=480, format=NV12, framerate=30/1 ! "
        "nvvidconv flip-method=0 ! "
        "video/x-raw, format=BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=BGR ! appsink drop=true sync=false"
    )
    
    camera = cv2.VideoCapture(cam, cv2.CAP_GSTREAMER)
    
    if not camera.isOpened():
        print("\n[경고] GStreamer 파이프라인으로 카메라를 열 수 없습니다.")
        print("[안내] 일반 USB 웹캠이나 내장 카메라(인덱스 0)로 대체 시도를 합니다...\n")
        camera = cv2.VideoCapture(0) # GStreamer가 아닐 경우를 대비한 fallback

    if not camera.isOpened():
        print("Error: 모든 카메라 연결에 실패했습니다. 장치 연결 상태를 확인하세요.")
        return

    while True:
        ret, frame = camera.read()
        if not ret:
            continue
        
        # 스레드 안전하게 전역 변수에 프레임 복사
        with lock:
            output_frame = frame.copy()

    camera.release()

def generate_frames():
    global output_frame, lock
    
    while True:
        with lock:
            if output_frame is None:
                continue
            
            # JPG 압축률 60% 설정 ([cv2.IMWRITE_JPEG_QUALITY, 60])
            ret, buffer = cv2.imencode('.jpg', output_frame, [cv2.IMWRITE_JPEG_QUALITY, 60])
            if not ret:
                continue
                
            frame_bytes = buffer.tobytes()
        
        # MJPEG 스트리밍 포맷으로 데이터 전송
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# 웹뷰 형태로 볼 수 있는 메인 페이지 (HTML)
@app.route('/')
def index():
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Jetson Camera WebView</title>
    </head>
    <body style="background-color: #222; color: white; text-align: center; font-family: sans-serif;">
        <h1>Camera Live Stream (640x480, 30fps)</h1>
        <hr>
        <div style="margin-top: 20px;">
            <img src="/video" width="640" height="480" style="border: 2px solid #555;" />
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

# /video 카메라 스트림 API
@app.route('/video')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # 백그라운드에서 카메라를 읽어올 스레드 시작
    t = threading.Thread(target=capture_frames)
    t.daemon = True
    t.start()
    
    # 5000번 포트로 Flask 서버 실행
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)