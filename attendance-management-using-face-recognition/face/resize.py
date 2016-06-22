import cv2

import numpy

import sys

from Tkinter import *

import os,os.path

root=Tk()

root.title("CONFIRM")

def confirm():    

    for i in range(1,num+1):

        image=str(i)+".png"

        image1=cv2.imread("c:/python27/face/temp/"+image)

        breadth = 150.0 / image1.shape[1]

        dimension = (125, int(image1.shape[0] * breadth))
         
        # perform the actual resizing of the image and show it

        resized = cv2.resize(image1, dimension, interpolation = cv2.INTER_AREA)

        #save the image

        cv2.imwrite("c:/python27/face/temp/"+image,resized)

        cv2.waitKey(0)

        root.destroy

    os.system("python c:/python27/face/command.py")
    
def redo():

    for i in range(1,num+1):

        os.remove("c:/python27/face/temp/"+str(i)+".png")

    os.system("python c:/python27/capture_group_image.py")


if __name__=="__main__":
    
    var1=StringVar();

    dir1="c:/python27/face/temp/";

    num=len([name for name in os.listdir(dir1) if os.path.isfile(os.path.join(dir1,name))])

    var1.set(num);

    Label(root,text="COnfirm for next steps", font=("helvatica",30),fg="black",bg="brown").grid(rowspan=2,columnspan=2,sticky=N+E+W+S, padx=5,pady=5)

    Label(root,text="total number of faces are : ",font=(20)).grid(row=2,column=0,sticky=E)

    Label(root,textvariable=var1, font=(20)).grid(row=2,column=1,sticky=N+E+W+S)

    Button(root,text="CONFIRM", fg="green", bg="gray",command=confirm).grid(row=3,column=0,sticky=E)

    Button(root,text="redo", fg="red", bg="grey",command=redo).grid(row=3,column=1,sticky=W)

root.mainloop()
