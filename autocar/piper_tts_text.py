# wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx
# wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json
# echo "Hello, this is Piper text to speech." | \
from IPython.display import Audio

# 현재 폴더에 있는 en_tts.mp3 파일 재생 플레이어 띄우기
Audio("en_tts.mp3")