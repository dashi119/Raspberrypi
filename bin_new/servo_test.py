import pigpio
import time

SERVO_PIN = 18
# pigpio Initialize
pi = pigpio.pi()

# Servo motor 90 degree 
def set_angle(angle):
  assert 0 <= angle <= 180, '0-180'
  
  # degree is from 500 to 2500 pulse width mapping
  pulse_width = (angle / 180) * (2500 - 500) + 500
  
  # pulse width set and rotate servo
  pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)
  
# UseCase
while True:
  set_angle(90) # Servo 90 degree
  time.sleep(1)
  
  set_angle(0) # Servo 0 degree
  time.sleep(1)
  
  set_angle(90) # Servo 90 degree
  time.sleep(1)
  
  set_angle(180) # Servo 180 degree
  time.sleep(1)
 
