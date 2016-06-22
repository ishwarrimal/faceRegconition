#from Tkinter import *

import os

import sys

from Tkinter import *

import Tkinter

from PIL import Image, ImageTk

root=Tk()

root.title("enter details")

root.configure(bg="#D7CCC8")

root.focus_set()

num=0;

def enter_the_value():

    uid=e1.get()

    sid=uid[7:]

    db=uid[0:6]

    print sid+" "+db

    password=e2.get()

    #to authenticate
    if password=="12345":

	#storing the output in a wamp directory(here in windows)
        fh=open("c:/wamp/www/attendance/pyoutput/OP_0.txt","w")

        fh.write(db+" "+sid)

        fh.close()

        os.system("python capture_group_image.py");#caputres the image and stores it as groupImg.png

        os.system("python facerecognition.py")

        os.system("python face/resize.py")

        root.destroy
    
#var1=StringVar();

#dir1="c:/python27/face/temp";

#num=len([name for name in os.listdir(dir1) if os.path.isfile(os.path.join(dir1,name))])

#var1.set(num);    
    #os.system("python face/command.py");

#image = Image.open("sem.jpg")

#tkpi = ImageTk.PhotoImage(image)

#label_image = Tkinter.Label(root, image=tkpi)

#label_image.place(x=0,y=0,width=600,height=50)

def run_command():

    os.system("python face/command.py");

if __name__=="__main__":

    Label(root,text="ENTER THE DETAILS", fg='white', bg='#424242' ,font=("helvetica",40),width=23).grid(rowspan=2,columnspan=3,sticky=E+W+N+S,padx=5,pady=5)

    Label(root, text="Enter ID: ",font=("helvetica ",30),fg='#212121',bg="#D7CCC8").grid(row=2,sticky=E,column=0)

    Label(root, text="Enter password: ",font=("helvetica ",30),fg='#212121',bg="#D7CCC8").grid(row=3,sticky=E,column=0)

    e1=Entry(root)

    e2=Entry(root)

    e1.grid(row=2,column=1,columnspan=2,sticky=W)

    e2.grid(row=3,column=1,columnspan=2,sticky=W)

    enter=PhotoImage(file="enter.gif")

    clear=PhotoImage(file="clear.gif")

    Button(root,text="CLEAR",font=("times new roman",30), fg="white",bg="#3E2723",command=root.quit).grid(row=4,column=0, pady=10,padx=10,sticky=E+W+N+S)

    Button(root,text="ENTER",font=("times new roman",30), fg="white",bg="#3E2723",command=enter_the_value).grid(row=4,column=1,pady=10,padx=10,sticky=E+W+N+S)

    #Label(root, text="total number of faces detected are: ",fg="#212121",bg="#607D8B",font=(10)).grid(row=5,column=0,sticky=E)
    
    #Label( root, textvariable=var1,fg="#000000",font=(10)).grid(row=5,column=1)

    #Button(root,text="NEXT",width=5,height=3,command=run_command).grid(row=6,columnspan=2)

root.mainloop()
