import RPi.GPIO as GPIO
import time
from matplotlib import pyplot

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comp = 4

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troykaModule, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

GPIO.output(troykaModule, 0)
GPIO.output(dac, 0)
GPIO.output(leds, 0)


def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(dac, d2b(k))
        time.sleep(0.015)
        if GPIO.input(comp) == 0:
            k-=2**i
    return k

def leds_out(vol):
    mas = [0]*8
    for i in range(0, 7):
        if 256*(i+1)/8 < vol:
            mas[-i] = 1
    GPIO.output(leds, mas)
    time.sleep(0.01)



try:
    voltage = 0
    start_time = time.time()
    data = []
    
    print("зарядка")
    GPIO.output(troykaModule, 1)
    while voltage < 256 * 0.9:
        voltage = adc()
        leds_out(voltage)
        GPIO.output(21, 0)
        data.append(voltage/256*3.3)
        print(voltage/256*3.3)
        time.sleep(0.1)

    print("разрядка")
    GPIO.output(troykaModule, 0)
    while voltage > 256 * 0.12:
        voltage = adc()
        leds_out(voltage)
        GPIO.output(21, 0)
        data.append(voltage/256*3.3)
        print(voltage/256*3.3)
        time.sleep(0/1)
    
    finish_time = time.time()
    ttime = finish_time - start_time

    #---------------------------------------------------------------
    with open('data.txt', 'w') as file_data:
        for elem in data:
            file_data.write(str(elem) + '\n')

    with open('settings.txt', 'w') as file_settings:
        file_settings.write("частота дискретизации" + str(len(data) / ttime) + '\n')
        file_settings.write("шаг квантования АЦП" + str(3.3/(2**8-1)) + '\n')
    
    #---------------------------------------------------------------

    y = [elem / 256 * 3.3 for elem in data]
    x = [i*ttime/len(data) for i in range(len(data))]
    pyplot.plot(x, y)
    pyplot.xlabel('Время с начала эксперимента, с')
    pyplot.ylabel('напряжение на конденсаторе, В')
    pyplot.show()

    #---------------------------------------------------------------

    print("общая продолжительность эксперимента:", ttime)
    print("период одного измерения:", ttime/len(data))
    print("среднюю частоту дискретизации проведённых измерений:", ttime/len(data))
    print("шаг квантования АЦП", 3.3/(2**8-1))

finally:

    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()