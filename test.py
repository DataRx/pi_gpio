import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

print "LED 17 on"
GPIO.output(17,GPIO.HIGH)
print "LED 27 on"
GPIO.output(27,GPIO.HIGH)

time.sleep(1)
print "LED 17 off"
GPIO.output(17,GPIO.LOW)
print "LED 27 off"
GPIO.output(27,GPIO.LOW)

time.sleep(1)

s = 0.15
ff = 1
for _ in range(500):
    if ff == 0:
        ff = 1
        print "LED 17 on"
        GPIO.output(17,GPIO.HIGH)
        print "LED 27 on"
        GPIO.output(27,GPIO.HIGH)
    else:
        ff = 0
        print "LED 17 off"
        GPIO.output(17,GPIO.LOW)
        print "LED 27 off"
        GPIO.output(27,GPIO.LOW)
    time.sleep(s)