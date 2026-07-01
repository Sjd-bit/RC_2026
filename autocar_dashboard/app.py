from flask import Flask, render_template, jsonify, request
import webview
import threading
import time

# 여기에 기존에 주피터에서 쓰던 pop 라이브러리들을 임포트합니다.
# from pop import AudioPlay, ... 

app = Flask(__name__)

# ---- [1. 웹 화면 보여주기] ----
@app.route('/')
def index():
    # 이 부분이 사용자에게 보여줄 HTML 대시보드 화면입니다.
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Autocar Dashboard</title>
        <style>
            body { font-family: Arial; text-align: center; background: #f0f0f0; }
            .btn { padding: 15px 25px; font-size: 18px; margin: 10px; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>🚗 Autocar 제어 대시보드</h1>
        <button class="btn" onclick="triggerTTS()">📢 TTS 안내방송 테스트</button>
        <div id="status">대기 중...</div>

        <script>
            // 버튼을 누르면 Flask API를 호출하는 자바스크립트 함수
            function triggerTTS() {
                document.getElementById('status').innerText = "TTS 재생 요청 중...";
                fetch('/api/tts')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('status').innerText = data.message;
                    });
            }
        </script>
    </body>
    </html>
    """

# ---- [2. API 구현하기 (기능들)] ----
@app.route('/api/tts', methods=['GET'])
def play_tts():
    print("API 요청 받음: 물체 감지 TTS 재생")
    
    # [과제 구현부] 주피터 랩에서 성공하셨던 TTS 재생 코드를 여기에 넣습니다.
    # 예: "물체가 감지되었습니다" 코드를 실행하는 부분
    
    return jsonify({"status": "success", "message": "물체가 감지되었습니다 안내 완료"})

# ---- [3. Flask와 pywebview 동시에 실행하기] ----
def run_flask():
    # pywebview와 충돌하지 않도록 포트를 5000번으로 설정해 배경에서 실행
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    # 1. Flask 서버를 백그라운드 쓰레드로 시작
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()
    
    # 2. Flask 서버가 켜질 때까지 잠시 대기
    time.sleep(1)
    
    # 3. pywebview 창을 띄워 Flask 주소(http://127.0.0.1:5000)를 로드
    webview.create_window('Autocar Controller', 'http://127.0.0.1:5000', width=800, height=600)
    webview.start()