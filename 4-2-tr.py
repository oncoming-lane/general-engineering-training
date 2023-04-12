import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


dac = [26, 19, 13, 6, 5, 11, 9, 10]


for pin in dac:
    GPIO.setup(pin, GPIO.OUT)

def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    t = int(input())
    while True:
        for v in range(255):
            print(33*v/2560)
            time.sleep(t/510)
            for pin in range(8):
                GPIO.output(dac[pin] , d2b(v)[pin])
        for v in range(255):
            print(33*v/2560)
            time.sleep(t/510)
            for pin in range(8):
                GPIO.output(dac[pin] , d2b(255 - v)[pin])
        v = 0
    




    
finally:
    for pin in dac:
        GPIO.output(pin , 1)
    GPIO.cleanup()

