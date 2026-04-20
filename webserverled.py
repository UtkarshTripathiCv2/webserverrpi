 34  sudo apt update
   35  sudo apt install python3-flask python3-rpi.gpio -y
   36  mkdir led_control && cd led_control
   37  nano app.py
   38  python3 app.py
   39  sudo ufw allow 5000
   40  python3 app.py
from flask import Flask, render_template_string
import RPi.GPIO as GPIO

app = Flask(__name__)

# GPIO Setup
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# HTML Template
HTML = """
<!DOCTYPE html>
<html>
<head><title>LED Control</title></head>
<body>
    <h1>Raspberry Pi LED Control</h1>
    <p><a href="/on"><button style="height:50px;width:100px">TURN ON</button></a></p>
    <p><a href="/off"><button style="height:50px;width:100px">TURN OFF</button></a></p>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/on")
def led_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    return render_template_string(HTML)

@app.route("/off")
def led_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
