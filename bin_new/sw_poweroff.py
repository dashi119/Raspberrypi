from gpiozero import Button
from time import sleep
import subprocess

button = Button(27)
state = 0

while True:
  if button.is_pressed:
    if state == 2:
      state = 0
      print("Pressed") 
#    args = ['sudo', 'poweroff']
#    subprocess.Popen(args)
    else:
      state += 1
  else:
    state = 0
    print("Released")

  sleep(0.5)    

#def my_callback(channel):
#  if channel==27:
#    args = ['sudo', 'poweroff']
#    subprocess.Popen(args)

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.add_event_detect(27, GPIO.RISING, callback=my_callback, bouncetime=200)

#try:
#  while True:
#    sleep(0.01)
    
#except KeyboardInterrupt:
#  pass
  
#GPIO.cleanup()
