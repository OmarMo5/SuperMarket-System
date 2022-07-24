from tkinter import *
from tkinter import messagebox
import webbrowser
import os,sys,random
from PIL import ImageTk, Image
from InsideSuperMarket import ContentSuperMarket

pro = Tk()
w=800
h=450
marginLeft=(pro.winfo_screenwidth()-w)/2
marginTop=(pro.winfo_screenheight()-h)/2
pro.title("SuperMarket")
pro.geometry('%dx%d+%d+%d' %(w,h,marginLeft,marginTop))
fontForLabelAndBtn=('tajawal',12,'bold')
bgForLabelInFrame1='#0B2f3A'
bgForLabelInFrame2='#0B2f3A'
bgForButton='#DBA901'
lbl1 = Label(pro,text="SuperMarket System",fg="gold",bg="black",font=('tajawal',16,'bold')).pack(fill=X)

url1="https:\\facebook\\username"
url2="url-youtube"
url3="url-telegram"
def open1():
    webbrowser.open_new(url1)
def open2():
    webbrowser.open_new(url2)
def open3():
    webbrowser.open_new(url3)
def infoDeve():
    messagebox.showinfo("Omar Mokhtar","This Is Developer That Create This Project")
def infoProj():
    messagebox.showinfo("Supermarket","This Project Super Market To Manage All Thing You Want!...")

frameOne = Frame(pro,width=230,height=420,bg=bgForLabelInFrame1).place(x=570,y=30)
titel1 = Label(text="Super Market Project",bg=bgForLabelInFrame1,fg='white',font=fontForLabelAndBtn).place(x=590,y=35)
titel2 = Label(text="Omar Mokhtar Developer",bg=bgForLabelInFrame1,fg='white',font=fontForLabelAndBtn).place(x=590,y=65)
titel2 = Label(text="Connection With Us",bg=bgForLabelInFrame1,fg='white',font=fontForLabelAndBtn).place(x=590,y=100)

btn1 = Button(frameOne,text="Account On FaceBook",width=20,fg="black",bg=bgForButton,font=fontForLabelAndBtn,command=open1).place(x=580,y=150)
btn2 = Button(frameOne,text="Account On GitHub",width=20,fg="black",bg=bgForButton,font=fontForLabelAndBtn,command=open2).place(x=580,y=200)
btn3 = Button(frameOne,text="Account On LinkedIn",width=20,fg="black",bg=bgForButton,font=fontForLabelAndBtn,command=open3).place(x=580,y=250)
btn4 = Button(frameOne,text="Look For Project",width=20,fg="black",bg=bgForButton,font=fontForLabelAndBtn,command=infoProj).place(x=580,y=300)
btn5 = Button(frameOne,text="Look For Developer",width=20,fg="black",bg=bgForButton,font=fontForLabelAndBtn,command=infoDeve).place(x=580,y=350)
btn6 = Button(frameOne,text="Exit The Project",width=20,fg="black",bg=bgForButton,font=fontForLabelAndBtn,command=pro.destroy).place(x=580,y=400)

#Way To Create Or Put Image In Form
img = ImageTk.PhotoImage(Image.open("super3.png"))
label1 = Label(pro, image=img).place(x=120,y=30,width=308,height=300)
#Way To Put Icon
photo = ImageTk.PhotoImage(Image.open('super3.png'))
pro.wm_iconphoto(False, photo)

frameTow = Frame(pro,width=570,height=120,bg=bgForLabelInFrame2).place(x=0,y=330)
strEntry1 = StringVar(frameTow)
strEntry2 = StringVar(frameTow)

def checkLogIn():
    user = strEntry1.get()
    passw = strEntry2.get()
    if user=="Malek Eslam" and passw=="123456":
        ContentSuperMarket()
        #messagebox.showinfo("Welcome","Your Data Are Correct, More Welcome...!♥")
    else: messagebox.showerror("Error","Your Data are Wrong")

img1 = ImageTk.PhotoImage(Image.open("super1.png"))
label2 = Label(frameTow, image=img1).place(x=430,y=340,width=140,height=100)

lbl1 = Label(frameTow,text="Username",fg='gold',bg=bgForLabelInFrame2,font=fontForLabelAndBtn).place(x=120,y=350)
lbl2 = Label(frameTow,text="Password",fg='gold',bg=bgForLabelInFrame2,font=fontForLabelAndBtn).place(x=120,y=390)
entr1 = Entry(frameTow,textvariable = strEntry1,font=fontForLabelAndBtn,justify="center").place(x=210,y=350)
entr2 = Entry(frameTow,textvariable = strEntry2,font=fontForLabelAndBtn,justify="center").place(x=210,y=390)
btnReg = Button(frameTow,text="LogIn",bg=bgForButton,font=fontForLabelAndBtn,command=checkLogIn).place(x=10,y=340,width=100,height=100)

pro.mainloop()