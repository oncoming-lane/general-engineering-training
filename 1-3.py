import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN)
GPIO.setup(22, GPIO.OUT)

GPIO.output(22, GPIO.input(18))
