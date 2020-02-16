import RPi.GPIO as GPIO
from time import sleep
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT,initial = GPIO.LOW)

def run(pin,duration):
    for i in range (1,10):        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin,GPIO.OUT,initial = GPIO.LOW)
        GPIO.output(pin,GPIO.HIGH)
        sleep(duration)
        GPIO.output(pin,GPIO.LOW)
        sleep(duration)
        GPIO.cleanup()
def start():
    p3 = threading.Thread(target = run(3,0.1),args=(10,))
    p7 = threading.Thread(target = run(7,0.1),args=(10,))        
    p8 = threading.Thread(target = run(8,0.1),args=(10,))
    p10 = threading.Thread(target = run(10,0.1),args=(10,))
    p3.start()
    p7.start()
    p8.start()
    p10.start()
    p3.join()
    p7.join()
    p8.join()
    p10.join()
    GPIO.cleanup()
    

try:
    while True:
        start()
except (KeyboardInterrupt,SystemExit):
    GPIO.cleanup()
finally:
    GPIO.cleanup()
    
