import numpy as np

import cv2.cv as cv

import cv2

import sys

from datetime import *

import Image

import os

from Tkinter import *

root=Tk()

root.title("enter details")

root.configure(bg="#795548")


#create a window with a name

#funtion to be called when the usn is collected
def main_program(usn):
    
    #capture from inbuilt camera i.e web cam

    cap=cv.CaptureFromCAM(0)
    
    while(True):
        
        #frame for video

        img=cv.QueryFrame(cap)
        
        #display the image from frame
        
        cv.ShowImage("image",img)

        #wait for response

        k=cv.WaitKey(10)

        #if esc is pressed the break

        if k==27:

            break
	
        #if 'c' is pressed then save the image

        elif k==ord('c'):

            time=datetime.now()

            cv.SaveImage("face/database/image.png",img)

            cv.DestroyAllWindows()

            os.system("python face.py")

            path="c:/python27/face/database/image.png"
            
            if os.path.exists(path):

		#renaming the file with the usn along with the current date stmp for making it unique
                newPath="c:/python27/face/database/"+usn+str(time.month)+str(time.day)+str(time.hour)+str(time.minute)+str(time.second)+str(time.microsecond)+".png"

                #path1="c:python27/face/database/"+usn+".png"
                
                cmd=os.rename(path,newPath)

                print "image captured, resized and renamed successfully"

                #cv.ShowImage("image","face/database"+usn+exp+".png")

            else:

                print "no face detected......image deleted"


        

#function to be called once the usn is entered
def enter_the_value():

    usn=e1.get()

    main_program(usn)

#creating UI for the input
Label(root,text="Enter Student detail", font=("helvatica",40),bg="#F44336", fg="#0a0800").grid(rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Label(root, text="Enter USN: ",fg="#42A5F5",bg="#795548",font=("chiller",20)).grid(row=3,padx=5,pady=5,sticky=E)

#Label(root, text="Enter expression: ",fg="#42A5F5",font=(20)).grid(row=4,padx=5,pady=5,sticky=E)

e1=Entry(root)

e1.grid(row=3,rowspan=2,column=1)

#clear button
Button(root,text="CLEAR",bg="#00695C",font=("times new roman",25), command=root.quit).grid(row=5,columnspan=2,stick=E+W+N+S, pady=4)

#enter/submit button
Button(root,text="ENTER",bg="#00695C",font=("times new roman",25), command=enter_the_value).grid(row=6,columnspan=2,stick=W+E+N+S, pady=4)

root.mainloop()


