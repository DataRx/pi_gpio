import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

print "LED 17 on"
GPIO.output(17,GPIO.HIGH)
print "LED 27 on"
GPIO.output(27,GPIO.HIGH)

time.sleep(1)
print "LED 17 off"
GPIO.output(17,GPIO.LOW)
print "LED 27 off"
GPIO.output(27,GPIO.LOW)