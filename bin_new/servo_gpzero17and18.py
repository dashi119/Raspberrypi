from gpiozero import Servo
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory()
servo17 = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo18 = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

#servo = Servo(17)
while True:
    servo17.min()
    servo18.min()    
    sleep(2)
    servo17.mid()
    servo18.mid()
    sleep(2)
    servo17.max()
    servo18.max()
    sleep(2) 
