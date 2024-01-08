from gpiozero import Motor
from time import sleep

motor2 = Motor(24,25)
motor2.forward(0.50)
sleep(2)
motor2.backward(0.50)
sleep(2)
motor2.stop()
