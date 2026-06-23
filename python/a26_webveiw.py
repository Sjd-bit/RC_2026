from pathlib import Path

import webview

BASE_PATH = Path(__file__).resolve().parent
NOTE_PATH = BASE_PATH / "note.txt"

class MemoApi:
    def __init__(self):
        pass

    def save_note(self, text):
         NOTE_PATH.write_text(text, encoding="utf-8")
         return {"status": "saved", "path": str(NOTE_PATH)}
    
    def load_note(self):
         return{"text": NOTE_PATH.read_text(encoding="utf-8")}

def main():
    api = MemoApi()
    
    # 🌟 수정 포인트: HTML 파일을 UTF-8로 직접 읽어옵니다.
    html_path = BASE_PATH / "index.html"
    html_content = html_path.read_text(encoding="utf-8")

    webview.create_window(
        "Simple Text Memo",
        html=html_content, # url 대신 html 매개변수를 사용해 문자열을 직접 전달합니다.
        width=640,
        height=520,
        resizable=True,
        js_api=api
    )
    webview.start()    
        # "simple text",
        # html=html_contenturl=(BASE_PATH/"index.html").as_uri(),
        # width=640,
        # height=520,
        # resizable=True
    
    webview.start()

if __name__ == "__main__":
        main()