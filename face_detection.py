import cv2
from gtts import gTTS
import os
from threading import Thread

j=0
mytext = 'Face detected!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("audio.mp3") 
    
def func1():
    os.system("cvlc audio.mp3")
    print ('parallel')
def func2():
    cv2.rectangle(frame, (x,y),(x+w,y+w),(255,255,255,2))
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while(True): 
    ret, frame = cap.read()
    
    faces=face_cascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5, minSize=(20,20))
    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+w),(0,0,255,2))
        print ('Face detected' + str(j))
        j+=1
        os.system("cd /home/robert/'Рабочий стол'/python")
        if j%10==0:
            Thread(target = func1).start()
            Thread(target = func2).start()
            
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Front Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()