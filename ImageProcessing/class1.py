import cv2
import numpy as np

#Read an image
img=cv2.imread("images/f1.jpg")
print(img)
cv2.imshow("window",img)
#to hold for an image
cv2.waitKey(0)
#changing into an grayscale image
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("window",img_gray)
cv2.waitKey(0)
#playing with an image
#I am converting blue=0
img[:,:,0]=0
cv2.imshow("window",img)
cv2.waitKey(0)
#image Stacking

blue=img[:,:,0]
green=img[:,:,1]
red=img[:,:,2]
new_img=np.hstack(blue,green,red)

#image resize
img_resize=cv2.resize(img,(256,256))
#task: image resize 30%,50%,75% etc
#flipping an image
#vertical flip
img_flip=cv2.flip(img,0)
#horizontal flip
img_flip1=cv2.flip(img,1)
#combined effect
img_flip2=cv2.flip(img,-1)
#crop an image
img_crop=img[100:300,200:500]
#images saving
cv2.imwrite('fruits_small.png',img_crop)
# Drawing images
images=np.zeros((512,512,3))
# rectangle drawing
cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=3)
#thickness =-1 then the rectangle will filled

cv2.circle(img,center=(100,400),radius=50,color=(0,0,255),thickness=2)
#line drawing
cv2.line(img,(8,8),(30,30),thickness=-1,color=(0,255,0))
#text
cv2.putText(img,org=(200,200),fontScale=4,color=(0,255,255),thickness=2,lineType=cv2.LINE_AA,text="Soumik Dey",fontFace=cv2.FONT_ITALIC)

