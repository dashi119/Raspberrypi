from gpiozero import Motor
from time import sleep

motor1 = Motor(22,23)
motor1.forward(0.50)
sleep(2)
motor1.backward(0.50)
sleep(2)
motor1.stop()
