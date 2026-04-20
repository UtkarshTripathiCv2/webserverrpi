import RPi.GPIO as GPIO
import time

LDR_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(LDR_PIN) == GPIO.LOW:
            print("It's Bright!")
        else:
            print("It's Dark!")
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
