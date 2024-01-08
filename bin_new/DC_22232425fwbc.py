from gpiozero import Motor
from time import sleep

motor1 = Motor(22,23)
motor2 = Motor(24,25)
motor1.forward(0.20)
motor2.forward(0.20)
sleep(2)
motor1.backward(0.20)
motor2.backward(0.20)
sleep(2)
motor1.stop()
motor2.stop()
