import webbrowser
import os

# 현재 app.py 파일이 있는 폴더에서 index.html 파일의 실제 경로를 찾습니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "index.html")

if os.path.exists(html_path):
    print("🌐 index.html 파일을 찾았습니다. 브라우저에서 시계를 엽니다...")
    # 브라우저로 index.html 실행
    webbrowser.open('file://' + html_path)
else:
    print("❌ 같은 폴더 안에서 index.html 파일을 찾을 수 없습니다.")
    print("파일 이름이 정확히 'index.html' 인지, clock_app 폴더 안에 있는지 확인해 주세요!")

