import cv2.cv as cv

import cv2

import sys

import numpy

import os

import Image

#global i

#Minimum possible object size. Objects smaller than these size are ignored.

min_size = (20, 20)

image_scale = 1

#Parameter specifying how much the image size is reduced at each image scale.

haar_scale = 1.1

#Parameter specifying how many neighbors each candidate rectangle should have to retain it.

min_neighbors = 1

#Parameter with the same meaning for an old cascade as in the function cvHaarDetectObjects.

haar_flags = 1

def detect_and_draw(img, cascade):

    # allocate temporary images

    gray = cv.CreateImage((img.width,img.height), 8, 1)

    #create a image with smaller size

    small_img = cv.CreateImage((cv.Round(img.width / image_scale),

                   cv.Round (img.height / image_scale)), 8, 1)

    # convert color input image to grayscale

    cv.CvtColor(img, gray, cv.CV_BGR2GRAY)
    
    # scale input image for faster processing

    cv.Resize(gray, small_img, cv.CV_INTER_LINEAR)

    #if algorithm is present

    if(cascade):

        #to get the current time

        t = cv.GetTickCount()

        #create memory for calculation(createMemStorage)

        faces = cv.HaarDetectObjects(small_img, cascade, cv.CreateMemStorage(0),
                                     haar_scale, min_neighbors, haar_flags, min_size)

        #previous time minus current time

        t = cv.GetTickCount() - t

        print "detection time = %gms" % (t/(cv.GetTickFrequency()*1000.))

        i=0

	#if more then one faces detected
        if faces:

		#getting all the coordinates of face
            for ((x, y, w, h), n) in faces:

                i=1;

                # the input to cv.HaarDetectObjects was resized, so scale the

                # bounding box of each face and convert it to two CvPoints

                pt1 = (int(x * image_scale), int(y * image_scale))

                pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))

                
                #draw rectangle (imagename,topleft,bottomright,color,size)

                cv.Rectangle(img,pt1,pt2,(0,230,0),1)

                #crop the image

                var1 = img[y: y + h, x: x + w]

                cv.SaveImage("face/database/image.png",var1)

                name="face/database/image.png"

                img=Image.open(name).convert('LA')

                img.save(name)

                break;

        cv.DestroyAllWindows()

        if i == 1:

            os.system("python resize.py")


        if i == 0:

            os.remove("face/database/image.png")



#main program
if __name__ == '__main__':

    #load the haarcascade face regcognition algorithm

    cascade = cv.Load("haarcascades/haarcascade_frontalface_alt.xml")
    
    #create window with name  "result"

    cv.NamedWindow("result", 1)
    
    #load the image and store it in variable 'image'

    image=cv.LoadImage("face/database/image.png")
    
    #calling detect_and_draw function

    detect_and_draw(image, cascade)

    cv.WaitKey(0)

    cv.DestroyWindow("result")
