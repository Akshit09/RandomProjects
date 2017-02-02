#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT) #setting the pins 
GPIO.setup(20, GPIO.OUT) #make sure in order
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

a=[21,20,16,12,7]    #high of turning on row on if all b are low
b=[23,24,25,8,18]    #hgh for turning of the particular led belonging a particular row
name=raw_input("Enter any word(IN CAPS):")
n=len(name)
try:
	for k in range(0,n):
			
		#A                   #starting capital letters
		if(name[k]=='A'):
			for i in range(0,5):
				GPIO.output(a[i],0)
				GPIO.output(b[i],0)
			blinks=450
			while(blinks < 500):
				for i in range(0,5):  #turning row high
					GPIO.output(a[i],1)
					if(a[i]==21):
						GPIO.output((b[0],b[4]),1) #controlling each led by turning led high or turning that led off
						time.sleep(0.005)
					elif(a[i]==20 or a[i]==12 or a[i]==7):
						GPIO.output((b[1],b[2],b[3]),1)
						time.sleep(0.005)
					else:
						time.sleep(0.0050)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			#B
		elif(name[k]=='B'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21):
						GPIO.output((b[3],b[4]),1)
						time.sleep(0.005)
					elif(a[i]==20 or a[i]==12):
						GPIO.output((b[4],b[1],b[2]),1)
						time.sleep(0.005)
					elif(a[i]==16):
						GPIO.output((b[3],b[4]),1)
						time.sleep(0.005)
					else:
						GPIO.output((b[4]),1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#C
		elif(name[k]=='C'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21):
						GPIO.output((b[0],b[4]),1)
						time.sleep(0.005)
					elif(a[i]==20 or a[i]==16):
						GPIO.output((b[4],b[1],b[2],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==12):
						GPIO.output((b[1],b[2],b[3]),1)
						time.sleep(0.005)
					elif(a[i]== 7):
						GPIO.output((b[0],b[4]),1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#D
		elif(name[k]=='D'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21):
						GPIO.output((b[0],b[4]),1)
						time.sleep(0.005)
					elif(a[i]==20 or a[i]==16 or a[i]==12):
						GPIO.output((b[1],b[0],b[3]),1)
						time.sleep(0.005)
					elif(a[i]== 7):
						GPIO.output((b[0],b[4]),1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#E
		elif(name[k]=='E'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21):
						GPIO.output((b[4]),1)
						time.sleep(0.005)
					elif(a[i]==20 or a[i]==12):
						GPIO.output((b[4],b[1],b[2],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==16):
						GPIO.output((b[4],b[3]),1)
						time.sleep(0.005)
					elif(a[i]== 7):
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#F
		elif(name[k]=='F'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21):
						GPIO.output((b[4]),1)
						time.sleep(0.005)
					elif(a[i]==20 or a[i]==12):
						GPIO.output((b[4],b[1],b[2],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==16):
						GPIO.output((b[4],b[3]),1)
						time.sleep(0.005)
					elif(a[i]== 7):
						GPIO.output((b[1],b[2],b[3],b[4]),1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#G
		elif(name[k]=='G'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21 or a[i]==7):
						GPIO.output((b[4],b[0]),1)
						time.sleep(0.005)
					elif(a[i]==20):
						GPIO.output((b[4],b[1],b[2],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==16):
						GPIO.output((b[1]),1)
						time.sleep(0.005)
					else:
						GPIO.output((b[1],b[2],b[3]),1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			#H
		elif(name[k]=='H'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==16):
						time.sleep(0.005)
					else:
						GPIO.output((b[1],b[2],b[3]),1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			#I
		elif(name[k]=='I'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					for j in range(1,5):
						GPIO.output(b[j],1)
					time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#J
		elif(name[k]=='J'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21):
						GPIO.output((b[4],b[0]),1)
						time.sleep(0.005)
					elif(a[i]==20 or a[i]==16):
						GPIO.output((b[4],b[1],b[0],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==12):
						GPIO.output((b[4],b[3],b[1]),1)
						time.sleep(0.005)
					elif(a[i]== 7):
						GPIO.output((b[0],b[3],b[4]),1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#K
		elif(name[k]=='K'):	
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21 or a[i]==7):
						GPIO.output((b[4],b[1],b[2]),1)
						time.sleep(0.005)
					elif(a[i]==20 or a[i]==12):
						GPIO.output((b[4],b[1],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==16):
						GPIO.output((b[4],b[3],b[2]),1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			#L
		elif(name[k]=='L'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21 or a[i]==20 or a[i]==16 or a[i]==12):
						GPIO.output((b[4],b[1],b[2],b[3]),1)
						time.sleep(0.005)
					elif(a[i]== 7):
						GPIO.output((b[3],b[4]),1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#M
		elif(name[k]=='M'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21 or a[i]==7 or a[i]==12):
						GPIO.output((b[1],b[2],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==20):
						GPIO.output((b[2]),1)
						time.sleep(0.005)
					elif(a[i]==16):
						GPIO.output((b[1],b[3]),1)
						time.sleep(0.005)
			
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#N
		elif(name[k]=='N'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21 or a[i]==7 ):
						GPIO.output((b[1],b[2],b[3]),1)
						time.sleep(0.005)
					else:
						for j in range(1,4):
							if(i==j):
								continue
							else:
								GPIO.output(b[j],1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#O
		elif(name[k]=='O'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21 or a[i]==7):
						GPIO.output((b[0],b[4]),1)
						time.sleep(0.005)
					else:
						GPIO.output((b[1],b[2],b[3]),1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#P
		elif(name[k]=='P'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21 or a[i]==16):
						GPIO.output((b[3],b[4]),1)
						time.sleep(0.005)
					elif(a[i]==20):
						GPIO.output((b[1],b[2],b[4]),1)
						time.sleep(0.005)
					else:
						GPIO.output((b[2],b[3],b[4],b[1]),1)
						time.sleep(0.005)
			
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			#Q
		elif(name[k]=='Q'):                      
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21):
						GPIO.output((b[0],b[4],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==20):
						GPIO.output((b[2],b[1],b[4]),1)
						time.sleep(0.005)
					elif(a[i]==16):
						GPIO.output((b[1],b[4]),1)
						time.sleep(0.005)
					elif(a[i]==12):
						GPIO.output((b[1],b[2],b[4]),1)
						time.sleep(0.005)
					else:
						GPIO.output((b[0],b[3]),1)
						time.sleep(0.005)
			
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			#R
		elif(name[k]=='R'):                      
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21 or a[i]==16):
						GPIO.output((b[4],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==20 or a[i]==12):
						GPIO.output((b[2],b[1],b[4]),1)
						time.sleep(0.005)
					elif(a[i]==7):
						GPIO.output((b[1],b[2],b[4]),1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#S
		elif(name[k]=='S'):                      
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21):
						GPIO.output((b[0],b[4],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==20):
						GPIO.output((b[2],b[3],b[1],b[4]),1)
						time.sleep(0.005)
					elif(a[i]==16):
						GPIO.output((b[4],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==12):
						GPIO.output((b[0],b[1],b[4],b[3]),1)
						time.sleep(0.005)
					else:
						GPIO.output((b[2],b[3],b[4]),1)
						time.sleep(0.005)
			
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#T
		elif(name[k]=='T'):        
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21):
						GPIO.output((b[4],b[3]),1)
						time.sleep(0.005)
					else:
						GPIO.output((b[2],b[3],b[0],b[4]),1)
						time.sleep(0.005)
					
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
				blinks+=1
			
			#U    
		elif(name[k]=='U'):                  
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==7):
						GPIO.output((b[0],b[4],b[3]),1)
						time.sleep(0.005)
					else:
						GPIO.output((b[2],b[1],b[4]),1)
						time.sleep(0.005)
			
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			#W
		elif(name[k]=='W'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21 or a[i]==20 ):
						GPIO.output((b[3],b[1],b[2]),1)
						time.sleep(0.005)
					elif(a[i]==16):
						GPIO.output((b[1],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==12):
						GPIO.output((b[2]),1)
						time.sleep(0.005)
					else:
						GPIO.output((b[1],b[2],b[3]),1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#V
		elif(name[k]=='V'):
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21 or a[i]==20 ):
						GPIO.output((b[3],b[1],b[2]),1)
						time.sleep(0.005)
					elif(a[i]==16):
						GPIO.output((b[0],b[2],b[4]),1)
						time.sleep(0.005)
					elif(a[i]==12):
						GPIO.output((b[4],b[0],b[3],b[1]),1)
						time.sleep(0.005)
					else:
						for j in range(0,5):
							GPIO.output(b[j],1)
						time.sleep(0.005)
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			#X
		elif(name[k]=='X'):                    
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21 or a[i]==7):
						GPIO.output((b[1],b[2],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==20 or a[i]==12):
						GPIO.output((b[2],b[4],b[0]),1)
						time.sleep(0.005)
					else:
						GPIO.output((b[0],b[1],b[4],b[3]),1)
						time.sleep(0.005)
			
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			
			#Y
		elif(name[k]=='Y'):                     
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21):
						GPIO.output((b[1],b[2],b[3]),1)
						time.sleep(0.005)
					elif(a[i]==20):
						GPIO.output((b[2],b[4],b[0]),1)
						time.sleep(0.005)
					else:
						GPIO.output((b[0],b[1],b[4],b[3]),1)
						time.sleep(0.005)
			
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1
			
			#Z 
		else:                    
			blinks=450
			while(blinks < 500):
				for i in range(0,5):
					GPIO.output(a[i],1)
					if(a[i]==21 or a[i]==7):
						time.sleep(0.005)
					elif(a[i]==20):
						GPIO.output((b[1],b[2],b[0],b[4]),1)
						time.sleep(0.005)
					elif(a[i]==16):	
						GPIO.output((b[1],b[3],b[0],b[4]),1)
						time.sleep(0.005)
					else:
						GPIO.output((b[3],b[2],b[0],b[4]),1)
						time.sleep(0.005)
			
			
					for i in range(0,5):
						GPIO.output(a[i],0)
						GPIO.output(b[i],0)
			
				blinks+=1

except KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()
