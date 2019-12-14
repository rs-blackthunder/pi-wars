import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#TRIG = 17
#ECHO = 27

#GPIO.setup(TRIG,GPIO.OUT)
#GPIO.setup(ECHO,GPIO.IN)

#GPIO.output(TRIG, True)
#time.sleep(0.00001)
#GPIO.output(TRIG, False)

#while GPIO.input(ECHO) == False:
 
#while GPIO.input(ECHO) == True:
 #   end = time.time()

#sig_time = end-start

##CM:
#distance = sig_time / 0.000058

##inches:
##distance = sig_time / 0.000148

#print('Distance: {} centimeters'.format(distance))

#GPIO.cleanup()


TRIG = 17
ECHO = 27
print('Distance Measurement In Progress')

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)

print('Waiting For Sensor To Settle')

time.sleep(2)

GPIO.output(TRIG, True)

time.sleep(0.00001)

GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:

  pulse_start = time.time()

while GPIO.input(ECHO)==1:

  pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

#distance = pulse_duration * 171.50

#distance = round(distance, 3)

#print("Distance:",distance,"m")

GPIO.cleanup()
