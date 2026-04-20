from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(17)

def motion_detected():
    print("Motion Detected! Turning on lights...")

def motion_stopped():
    print("All clear.")

pir.when_motion = motion_detected
pir.when_no_motion = motion_stopped

pause() # Keep the script running
