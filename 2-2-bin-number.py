import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0] * 8

nnn = [255, 127, 64, 32, 5, 0]
n = 40
s = bin(n)[2::]

for i in range(1, len(s)+1):
    number[-i] = int(s[-i])

print(number)
print(s)

GPIO.setup(dac, GPIO.OUT)

for i in range(8):
    GPIO.output(dac[i], number[i])

time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()
