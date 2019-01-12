# import curses and GPIO
import curses
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


# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
curses.halfdelay(3)
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char ==  ord('l'):
                spL.ChangeDutyCycle(50)
                spR.ChangeDutyCycle(50)
            elif char ==  ord('m'):
                spL.ChangeDutyCycle(75)
                spR.ChangeDutyCycle(75)
            elif char ==  ord('h'):
                spL.ChangeDutyCycle(99)
                spR.ChangeDutyCycle(99)
            elif char == curses.KEY_UP:
                GPIO.output(rb,False)
                GPIO.output(rf,True)
                GPIO.output(lb,False)
                GPIO.output(lf,True)
                print "up"
            elif char == curses.KEY_DOWN:
                GPIO.output(rb,True)
                GPIO.output(rf,False)
                GPIO.output(lb,True)
                GPIO.output(lf,False)
                print "down"
            elif char == curses.KEY_RIGHT:
                GPIO.output(rb,True)
                GPIO.output(rf,False)
                GPIO.output(lb,False)
                GPIO.output(lf,True)
                print "right"
            elif char == curses.KEY_LEFT:
                GPIO.output(rb,False)
                GPIO.output(rf,True)
                GPIO.output(lb,True)
                GPIO.output(lf,False)
                print "left"
            else:
                GPIO.output(rb,False)
                GPIO.output(rf,False)
                GPIO.output(lb,False)
                GPIO.output(lf,False)
                print "stop"
            
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    

