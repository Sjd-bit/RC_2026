from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from config import Config
from car_controller import CarController
from camera_controller import CameraController
from sound_controller import SoundController

app = Flask(__name__)
CORS(app)  # 대시보드(pywebview)와의 원활한 CORS 통신 허용

car = CarController()
camera = CameraController()
sound = SoundController()

@app.route('/api/status', os=['GET'])
def get_status():
    return jsonify({
        "status": "running",
        "speed": car.speed,
        "steering_angle": car.steering_angle,
        "camera_pan": camera.pan,
        "camera_tilt": camera.tilt
    })

@app.route('/api/motor', methods=['POST'])
def control_motor():
    data = request.get_json() or {}
    if 'speed' not in data:
        return jsonify({"error": "Missing 'speed' parameter"}), 400
    
    try:
        speed = int(data['speed'])
    except ValueError:
        return jsonify({"error": "Invalid type for 'speed'"}), 400

    current_speed = car.set_motor(speed)
    return jsonify({"result": "success", "speed": current_speed})

@app.route('/api/steering', methods=['POST'])
def control_steering():
    data = request.get_json() or {}
    if 'angle' not in data:
        return jsonify({"error": "Missing 'angle' parameter"}), 400
    
    try:
        angle = int(data['angle'])
    except ValueError:
        return jsonify({"error": "Invalid type for 'angle'"}), 400

    current_angle = car.set_steering(angle)
    return jsonify({"result": "success", "angle": current_angle})

@app.route('/api/drive', methods=['POST'])
def control_drive():
    data = request.get_json() or {}
    x = data.get('x')
    y = data.get('y')
    
    if x is None or y is None:
        return jsonify({"error": "Missing 'x' or 'y' for joystick"}), 400
        
    try:
        x, y = float(x), float(y)
    except ValueError:
        return jsonify({"error": "Joystick values must be float"}), 400

    # 범위 제한 규칙 검사
    if not (-1.0 <= x <= 1.0) or not (-1.0 <= y <= 1.0):
        return jsonify({"error": "Out of bound values (-1.0 ~ 1.0)"}), 400

    car.process_joystick(x, y)
    return jsonify({"result": "success", "speed": car.speed, "steering": car.steering_angle})

@app.route('/api/camera/pan_tilt', methods=['POST'])
def control_camera():
    data = request.get_json() or {}
    pan = data.get('pan', camera.pan)
    tilt = data.get('tilt', camera.tilt)
    
    try:
        pan, tilt = int(pan), int(tilt)
    except ValueError:
        return jsonify({"error": "Pan/Tilt must be integer"}), 400

    c_pan, c_tilt = camera.set_pan_tilt(pan, tilt)
    return jsonify({"result": "success", "pan": c_pan, "tilt": c_tilt})

@app.route('/api/sound/tone', methods=['POST'])
def control_tone():
    data = request.get_json() or {}
    freq = data.get('freq', 440)
    duration = data.get('duration', 0.5)
    
    sound.play_tone(int(freq), float(duration))
    return jsonify({"result": "success"})

@app.route('/api/sound/tts', methods=['POST'])
def control_tts():
    data = request.get_json() or {}
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "Text is empty"}), 400
        
    sound.speak_tts(text)
    return jsonify({"result": "success"})

@app.route('/video_feed')
def video_feed():
    return Response(camera.generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api/stop', methods=['POST'])
def control_stop():
    car.emergency_stop()
    return jsonify({"result": "stopped", "speed": car.speed, "steering": car.steering_angle})

if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT, debug=False, threaded=True)