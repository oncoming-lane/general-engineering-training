import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)






GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)

def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
            dc = int(input())
            p.start(dc)
    




    
finally:
    GPIO.output(22 , 0)
    GPIO.cleanup()

