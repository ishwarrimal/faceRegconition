import cv2

import cv2.cv as cv

import os

import Image

cap=cv.CaptureFromCAM(0)

while(True):

    img=cv.QueryFrame(cap)

    cv.ShowImage("image",img)

    k=cv.WaitKey(10)

    if k==27:

        break

    elif k==ord('c'):

        cv.SaveImage("groupImg.png",img)

        img = Image.open("groupImg.png").convert('LA')
        
        img.save('groupImg.png')

        break

cv.DestroyAllWindows()



