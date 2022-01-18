import RPi.GPIO as gpio
import time
sidedoorStatus = False

#cardinfo = input()
# switch like statement based on card number didctating which person
#if cardinfo == '':
    # unlock the door
    #changeLockState()
print(gpio.RPI_INFO)
    
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

gpio.setup(3, gpio.OUT)
gpio.setup(5, gpio.OUT)
gpio.setup(7, gpio.OUT)
pwm = gpio.PWM(7, 100)
pwm.start(0)

print('setup')
time.sleep(2)

gpio.output(3, True)
gpio.output(5, False)
pwm.ChangeDutyCycle(25)
gpio.output(7, True)
print(gpio.input(7))
time.sleep(5)
gpio.output(7, False)
print('hello')
gpio.cleanup()
