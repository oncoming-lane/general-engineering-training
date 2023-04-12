import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
weight = [128, 64, 32, 16, 8, 4, 2, 1]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comp = 4

GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)


def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        sum = 0
        for value in range(8):
            signal = d2b(sum + weight[value])
            GPIO.output(dac, signal)
            time.sleep(0.01)
            if(GPIO.input(comp) == 1):
                sum += weight[value]
        sig = d2b(sum)
        voltage = sum / levels * maxVoltage
        for value in range(8):
            if value < sum / 255 * 8:
                GPIO.output(leds[value], 1)
            else:
                GPIO.output(leds[value], 0)
        print("{}, {}, {}".format(sum, sig, voltage))


    
finally:
    GPIO.output(22 , 0)
    GPIO.cleanup()

