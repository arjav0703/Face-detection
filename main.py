import cv2 # import openCV

alg = 'model.xml'  # accessed the model file

cascade = cv2.CascadeClassifier(alg) # loading the model with cv2

cam = cv2.VideoCapture(0)

while True:
    
    _,img = cam.read() # read from the camera
    
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert to gray scale image

    face = cascade.detectMultiScale(grayImg) #coordinates of face

    for (x, y, w, h) in face: 
        
        cv2.rectangle(img, (x, y), (x + w, y + h),(0,255,200),2) # draw the retangle

    cv2.imshow("FaceDetect",img)

    key = cv2.waitKey(1)

    if key == 81 or key == 113 :
        break

cam.release()
cv2.destroyAllWindows()
        

    

 
