import webview
import os

# 대시보드가 통신을 보낼 원격 Autocar의 IP 및 포트를 지정합니다.
# 로컬에서 통합 테스트 시 기본 "http://127.0.0.1:8000" 사용 가능
AUTOCAR_SERVER_URL = "http://127.0.0.1:8000"

class ApiBridge:
    def get_server_url(self):
        return AUTOCAR_SERVER_URL

def run_dashboard():
    bridge = ApiBridge()
    
    # HTML 파일 절대경로 계산
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, 'index.html')
    
    window = webview.create_window(
        title='Autocar Smart Dashboard Control Center',
        url=html_path,
        js_api=bridge,
        width=1024,
        height=768,
        resizable=True
    )
    webview.start(debug=True)

if __name__ == '__main__':
    run_dashboard()