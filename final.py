import cv2
import math
import random
import time
import os
import datetime
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
now = datetime.datetime.now()
cap = cv2.VideoCapture(1)
capx = cv2.VideoCapture(0)
cap.set(3, 320);
cap.set(4, 240);
capx.set(3, 320);
capx.set(4, 240); 
t = 0
i = 0
while(True) :
	start = time.time()
	ret,img = cap.read()
	_ , imgx = capx.read()	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	grayx = cv2.cvtColor(imgx, cv2.COLOR_BGR2GRAY)
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
			if (t == 20 or t > 20) :
				while (True) :
					if (i == 0) :
						line = str(now) + '\n'
						with open('data.log','a') as f:
							f.write(line)
						i = i+1
					print("ALERT MODE ON")
					print("\a")
			if (speed >= 30 and speed < 60 and (t <= 20)) :
				t = t+1
			elif (speed >= 60 and speed < 80 and (t <= 20)) :
				t = t+2
			elif (speed >= 80 and speed < 100 and (t <= 20)) :
				t = t+3
			elif (speed >= 100 and (t <= 20)) :
				t = t+5
			print("T is",t)
	fx = face_cascade.detectMultiScale(grayx, 1.3, 5)
	for (ax,ay,aw,ah) in fx :
		imgx = cv2.rectangle(imgx, (ax,ay),(ax+aw,ay+ah),(255,0,0),2)
		roi_gray = grayx[ay:ay+ah, ax:ax+aw]
		roi_color = imgx[ay:ay+ah, ax:ax+aw]
		eyex = eye_cascade.detectMultiScale(grayx, 1.3, 5)
		if len(eyex) != 0 :
			for (bx,by,bw,bh) in eyex :
				cv2.rectangle(imgx,(bx,by),(bx+bw,by+bh),(0,255,0),2)
				roi_gray = grayx[by:by+bh, bx:bx+bw]
				roi_color = imgx[by:by+bh, bx:bx+bw]
				t = 0
		else :
			speed = random.randint(30,151)
			print("The speed is ",speed)
			if (t == 20 or t > 20) :
				while (True) :
					if (i == 0) :
						line = str(now) + '\n'
						with open('data.log','a') as f:
							f.write(line)
						i = i+1
					print("ALERT MODE ON")
					print("\a")
			if (speed >= 30 and speed < 60 and (t <= 20)) :
				t = t+1
			elif (speed >= 60 and speed < 80 and (t <= 20)) :
				t = t+2
			elif (speed >= 80 and speed < 100 and (t <= 20)) :
				t = t+3
			elif (speed >= 100 and (t <= 20)) :
				t = t+5
			print("T is",t)
	cv2.imshow('imgx',imgx)	
	end = time.time()
	avg = 1/(end-start)
	print("Average FPS ", avg)
	cv2.imshow('img',img)
	if (cv2.waitKey(100) & 0xFF == ord('q')) :
		break
cap.release()
capx.release()
cv2.destroyAllWindows
