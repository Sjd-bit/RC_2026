let SERVER_URL = "http://127.0.0.1:8000"; // 기본값 대체용

// pywebview가 주입해준 Python 함수 호출하여 원격 서버 IP 가져오기
window.addEventListener('pywebviewready', function() {
    pywebview.api.get_server_url().then(function(url) {
        SERVER_URL = url;
        document.getElementById('connection-status').innerText = `연결 대상: ${SERVER_URL}`;
        document.getElementById('camera-stream').src = `${SERVER_URL}/video_feed`;
        startTelemetryLoop();
    });
});

// 원격 API 포스트 호출 규격 공통 유틸리티
async function sendPostCommand(endpoint, payload) {
    try {
        const response = await fetch(`${SERVER_URL}${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        return await response.json();
    } catch (error) {
        console.error(`통신 오류 발생 [${endpoint}]:`, error);
        const statusBadge = document.getElementById('connection-status');
        statusBadge.innerText = "⚠️ 통신 연결 끊김";
        statusBadge.className = "status-badge disconnected";
    }
}

// 1. 모터/조향 개별 제어 및 응급 정지
function sendMotorSpeed(val) {
    sendPostCommand('/api/motor', { speed: parseInt(val) });
}

function quickMove(steer, speed) {
    sendPostCommand('/api/motor', { speed: speed });
    sendPostCommand('/api/steering', { angle: steer });
}

function triggerEmergencyStop() {
    sendPostCommand('/api/stop', {}).then(data => {
        document.getElementById('slider-speed').value = 0;
        document.getElementById('slider-pan').value = 90;
        document.getElementById('slider-tilt').value = 90;
        document.getElementById('pan-val').innerText = 90;
        document.getElementById('tilt-val').innerText = 90;
    });
}

// 2. 카메라 방향 제어
function sendPanTilt() {
    const pan = document.getElementById('slider-pan').value;
    const tilt = document.getElementById('slider-tilt').value;
    document.getElementById('pan-val').innerText = pan;
    document.getElementById('tilt-val').innerText = tilt;
    sendPostCommand('/api/camera/pan_tilt', { pan: parseInt(pan), tilt: parseInt(tilt) });
}

function changeCameraView(preset) {
    let pan = 90, tilt = 90;
    if(preset === 'ground') { pan = 90; tilt = 30; }
    else if(preset === 'sky') { pan = 90; tilt = 150; }
    
    document.getElementById('slider-pan').value = pan;
    document.getElementById('slider-tilt').value = tilt;
    document.getElementById('pan-val').innerText = pan;
    document.getElementById('tilt-val').innerText = tilt;
    sendPostCommand('/api/camera/pan_tilt', { pan: pan, tilt: tilt });
}

// 3. 사운드 및 TTS 제어부
function playMelody(freq, duration) {
    sendPostCommand('/api/sound/tone', { freq: freq, duration: duration });
}

function sendTTS() {
    const textStr = document.getElementById('tts-input').value;
    if(!textStr) return alert("말할 내용을 작성하세요");
    sendPostCommand('/api/sound/tts', { text: textStr });
}

// 4. 조이스틱 드래그 로직 구현
const zone = document.getElementById('joystick-zone');
const knob = document.getElementById('joystick-knob');
let isDragging = false;

zone.addEventListener('mousedown', startDrag);
window.addEventListener('mousemove', dragMove);
window.addEventListener('mouseup', endDrag);

zone.addEventListener('touchstart', startDrag, {passive: false});
window.addEventListener('touchmove', dragMove, {passive: false});
window.addEventListener('touchend', endDrag);

let centerX = 80, centerY = 80; // 패널 크기 절반 기준 정점

function startDrag(e) {
    isDragging = true;
    dragMove(e);
}

function dragMove(e) {
    if (!isDragging) return;
    if (e.cancelable) e.preventDefault();

    const rect = zone.getBoundingClientRect();
    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    const clientY = e.touches ? e.touches[0].clientY : e.clientY;

    let posX = clientX - rect.left - 25; // 25는 노브 반경
    let posY = clientY - rect.top - 25;

    // 경계 원 반경 계산 제한
    let dx = posX + 25 - centerX;
    let dy = posY + 25 - centerY;
    let dist = Math.sqrt(dx*dx + dy*dy);
    const maxDist = 55;

    if (dist > maxDist) {
        posX = centerX + (dx / dist) * maxDist - 25;
        posY = centerY + (dy / dist) * maxDist - 25;
    }

    knob.style.left = posX + 'px';
    knob.style.top = posY + 'px';

    // -1.0 ~ 1.0 사잇값 정규화 (y축은 전진이 양수가 되도록 반전처리)
    let joyX = ((posX + 25 - centerX) / maxDist).toFixed(2);
    let joyY = (-((posY + 25 - centerY) / maxDist)).toFixed(2);

    // 실시간 이동 명령 전송
    sendPostCommand('/api/drive', { x: parseFloat(joyX), y: parseFloat(joyY) });
}

function endDrag() {
    if (!isDragging) return;
    isDragging = false;
    // 제자리 복귀 및 정지
    knob.style.left = '55px';
    knob.style.top = '55px';
    sendPostCommand('/api/drive', { x: 0.0, y: 0.0 });
}

// 5. 텔레메트리 갱신 루프 (주기적 데이터 폴링 수행)
function startTelemetryLoop() {
    setInterval(() => {
        fetch(`${SERVER_URL}/api/status`)
            .then(res => res.json())
            .then(data => {
                const statusBadge = document.getElementById('connection-status');
                statusBadge.className = "status-badge connected";
                
                document.getElementById('tel-status').innerText = data.status.toUpperCase();
                document.getElementById('tel-speed').innerText = data.speed;
                document.getElementById('tel-steer').innerText = data.steering_angle;
            }).catch(() => {
                document.getElementById('connection-status').className = "status-badge disconnected";
            });
    }, 1000);
}