import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


dac = [26, 19, 13, 6, 5, 11, 9, 10]


for pin in dac:
    GPIO.setup(pin, GPIO.OUT)

def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        v = int(input())
        if v == 'q':
            exit()

        if v < 0:
            print("otrizatelnoe")
            v = 0
        if v > 255:
            print("slishkom bolshoe")
            v = 0
        print(33*v/2560)
        for pin in range(8):
            GPIO.output(dac[pin] , d2b(v)[pin])




    
finally:
    for pin in dac:
        GPIO.output(pin , 1)
    GPIO.cleanup()



