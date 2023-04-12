import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)



dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comp = 4

GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)



def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        for value in range(256):
            signal = d2b(value)
            GPIO.output(dac, signal)
            time.sleep(0.001)
            voltage = value / levels * maxVoltage
            cv = GPIO.input(comp)
  
            if cv == 0:
                print("{}, {}, {}".format(value, signal, voltage))
                break
    




    
finally:
    GPIO.output(22 , 0)
    GPIO.cleanup()

