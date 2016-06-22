#!/usr/bin/python
import cv2.cv as cv

import cv2

import sys

import numpy

min_size = (20, 20)

image_scale = 1

haar_scale = 1.1

min_neighbors = 1

haar_flags = 1

def detect_and_draw(img, cascade):

    # allocate temporary images
    gray = cv.CreateImage((img.width,img.height), 8, 1)

    small_img = cv.CreateImage((cv.Round(img.width / image_scale),
                   cv.Round (img.height / image_scale)), 8, 1)

    # convert color input image to grayscale
    cv.CvtColor(img, gray, cv.CV_BGR2GRAY)

    #gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # scale input image for faster processing
    cv.Resize(gray, small_img, cv.CV_INTER_LINEAR)

    #cv.EqualizeHist(small_img, small_img)

    if(cascade):
        t = cv.GetTickCount()#to get the time, create memory for calculation(createMemStorage)

        faces = cv.HaarDetectObjects(small_img, cascade, cv.CreateMemStorage(0),
                                     haar_scale, min_neighbors, haar_flags, min_size)

        t = cv.GetTickCount() - t#previous time minus current time

        #print "detection time = %gms" % (t/(cv.GetTickFrequency()*1000.))

        roi=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        ROI=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']

        i=0

        if faces:

            for ((x, y, w, h), n) in faces:
                # the input to cv.HaarDetectObjects was resized, so scale the
                # bounding box of each face and convert it to two CvPoints
                pt1 = (int(x * image_scale), int(y * image_scale))

                pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))

                
                #draw rectangle (imagename,topleft,bottomright,color,size)
                cv.Rectangle(img,pt1,pt2,(0,230,0),1)

                roi[i] = img[y: y + h, x: x + w]

                #cv.ShowImage(ROI[i],roi[i])
                cv.SaveImage("face/temp/"+ROI[i]+".png",roi[i])
                i=i+1;
    #cv.ShowImage("result", img)

if __name__ == '__main__':

    cascade = cv.Load("haarcascades/haarcascade_frontalface_alt.xml")
    #cv.NamedWindow("result", 1)

    image = cv.LoadImage("groupImg.png")

    detect_and_draw(image, cascade)

    cv.WaitKey(0)

    cv.DestroyWindow("result")
