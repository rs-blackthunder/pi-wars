# import curses and GPIO
import RPi.GPIO as GPIO
from time import sleep

#set GPIO numbering mode and define output pins

rb = 7 #in1 - right forward
rf = 11 #in2 - right backward
lb = 13 #in3 - left forward
lf = 15 #in4 - left backward

enR = 8 #enA - right
enL = 10 #enB - left

GPIO.setmode(GPIO.BOARD)

GPIO.setup(rb,GPIO.OUT)
GPIO.setup(rf,GPIO.OUT)
GPIO.setup(lb,GPIO.OUT)
GPIO.setup(lf,GPIO.OUT)
GPIO.setup(enR,GPIO.OUT)
GPIO.setup(enL,GPIO.OUT)

GPIO.output(rf,False)
GPIO.output(rb,False)
GPIO.output(lf,False)
GPIO.output(lb,False)

spR=GPIO.PWM(enR,1000) #speed - right
spR.start(100)

spL=GPIO.PWM(enL,1000) #speed - left
spL.start(100)

# turn 90 clockwise
# turn 90 anticlockwise
# distance
# 1sec at 80 = 0.4m
try:
        while True:   
            x  =  input()
            
            if x == 'q':
                break
            else:
                spL.ChangeDutyCycle(80)
                spR.ChangeDutyCycle(80)
                GPIO.output(rb,False)
                GPIO.output(rf,True)
                GPIO.output(lb,False)
                GPIO.output(lf,True)
                sleep(1)
                GPIO.output(rf,False)
                GPIO.output(lf,False)
finally:
    GPIO.cleanup()
    


    
