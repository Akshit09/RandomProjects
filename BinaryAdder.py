#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import math
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4,0)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,0)
GPIO.setup(23, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, GPIO.PUD_UP)
a=[0,0]
b=[0,0]
i=5
j=5
e=0
def zero(channel): 
            GPIO.output(17,1)
            if(i<2):
                a[i]=0
                print(a[i])
            if(j<2):
                b[j]=0
                print(b[j])
            time.sleep(0.1)
            GPIO.output(17,0)
def one(channel):
            GPIO.output(4, GPIO.HIGH)
            if(i<2):
                a[i]=1
                print(a[i])
            if(j<2):
                b[j]=1
                print(b[j])
            time.sleep(0.1)
            GPIO.output(4, 0)

GPIO.add_event_detect(23, GPIO.FALLING, callback=zero, bouncetime=200)
GPIO.add_event_detect(24, GPIO.FALLING, callback=one, bouncetime=200)

try:
     for i in range(0,2):
               while True:
                   print(" First Number bit:",i)
                   pass
                   time.sleep(3.0)
                   break
     for j in range(0,2):
               while True:
                   i=4
                   print("Second Number bit:",j)
                   pass
                   time.sleep(3.0)
                   break
except KeyboardInterrupt:
    GPIO.cleanup()
c=0
d=0

len1=len(a)-1
len2=len(b)-1
for i in range(0,2):
         c=c+(a[i]*(pow(2,len1)))
         d=d+(b[i]*(pow(2,len2))) 
         len1=len1-1
         len2=len2-1
print(c)
print(d)
print(type(c),type(d))
e=bin(c+d)
print(e)
e=str(e)
print(type(e),e)
for i in range(2,5):
       if(e[i]=='1'):
               GPIO.output(4, 1)
               time.sleep(1.0)
               GPIO.output(4, 0)
               time.sleep(1.0)
       else:
               GPIO.output(17, 1)
               time.sleep(1.0)
               GPIO.output(17, 0)
               time.sleep(1.0)
GPIO.cleanup()           
print("The end")