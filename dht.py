import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to GPIO 4
dhtDevice = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temp = dhtDevice.temperature
        humi = dhtDevice.humidity
        print(f"Temp: {temp:.1f}*C  Humidity: {humi}%")
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    time.sleep(2.0)
