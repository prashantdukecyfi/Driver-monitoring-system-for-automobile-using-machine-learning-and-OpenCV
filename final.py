import numpy as np
import cv2
import math
import random

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(-1)

t = 0

while(True) :
	ret,img = cap.read()	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		img = cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

		eye = eye_cascade.detectMultiScale(gray, 1.3, 5)
		if len(eye) != 0 :
			for (ex,ey,ew,eh) in eye :
				cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
				roi_gray = gray[ey:ey+eh, ex:ex+ew]
				roi_color = img[ey:ey+eh, ex:ex+ew]
				roi_gray2 = roi_gray.copy()
				binary=cv2.resize(roi_gray2,None,fx=2,fy=2)            
				cv2.imshow('binary',binary)
				t = 0
				print ("Eye detected")
		else :
			speed = random.randint(30,151)
			print("The speed is ",speed)
			if (t == 10 or t > 10) :
				while (True) :
					print("ALERT MODE ON")
					print("\a")
			if (speed >= 30 and speed < 60 and (t <= 10)) :
				t = t+1
			elif (speed >= 60 and speed < 80 and (t <= 10)) :
				t = t+2
			elif (speed >= 80 and speed < 100 and (t <= 10)) :
				t = t+3
			elif (speed >= 100 and (t <= 10)) :
				t = t+5
			print("T is",t)
	cv2.imshow('img',img)
	if (cv2.waitKey(100) & 0xFF == ord('q')) :
		break




cap.release()
cv2.destroyAllWindows
