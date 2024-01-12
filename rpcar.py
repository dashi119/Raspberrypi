from gpiozero import Motor
from time import sleep

def fwbw(symspd):
  motor1 = Motor(22,23)
  motor2 = Motor(24,25)
  if symspd[-1] == "h":
    spd = 0.80
  elif symspd[-1] == "m":
    spd = 0.50
  elif symspd[-1] == "l":
    spd = 0.20

  if symspd[:2] == "fw":
    motor1.forward(spd)
    motor2.forward(spd)
    sleep(2)
  elif symspd[:2] == "bw":
    motor1.backward(spd)
    motor2.backward(spd)
    sleep(2)
  elif symspd[:2] == "lt":
    motor1.forward(spd)
    motor2.backward(spd)
    sleep(2)
  elif symspd[:2] == "rt":
    motor1.backward(spd)
    motor2.forward(spd)
    sleep(2)
  motor1.stop()
  motor2.stop()
