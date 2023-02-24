
from tkinter import *
from tkinter.font import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from random import randrange
from PIL import Image, ImageFont, ImageDraw
from tkinter import *
from tkinter.font import *
from PIL import Image, ImageTk
from numpy import random
import os
import pandas as pd
from datetime import date
from tkinter import filedialog
import datetime

x = datetime.datetime.now()
print(x)

    

# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('550x500')

today = date.today()
day = today.strftime("%b-%d-%Y")

filess = ""
font = "PK Maehongson Medium.ttf"

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font='none 18')
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents
    # label_file_explorer.configure(text="File Opened: "+filename)
    check_file = os.path.isfile(filename)
    print(check_file)
    if(check_file==True):
      setpastFile(filename)
    else:
      popupmsg("File pase not Found")

def setpastFile(filepast):
    global filess, lenimg, imgCall, nameHH
    filess = filepast
    df = pd.read_csv(filess)
    nameHH = df['namelottery']
    lenimg = len(nameHH)
    print("LEN: ", lenimg)
    imgCall = []

    os.chdir(r"D:/pyM6/")
    os.mkdir("raffle"+str(day))
    background.config(text='succeed have all data %d'%(lenimg), anchor=NW)

def getString():
    print(filess)
    root.destroy()

def createImgLoop():
    global imgCall, daytime
    imgbackHead = Image.open("img/Headimg.jpg")
    for i in range(0, lenimg):
        imgbackHead.save("NewimgSystem/imgTest%d.jpg" % (i))
        print("Pass%d" % (i))

def show():
    global imgCall, daytime
    print("=============show===================")
    createImgLoop()
    j = 0
    for i in range(0, lenimg):

        results = Image.open("NewimgSystem/imgTest%d.jpg" % (i))

        title_text = "กระเต็น"
        text1 = "วิ่งรูด"
        title_font1 = ImageFont.truetype(font, 100)
        title_font2 = ImageFont.truetype(font, 50)
        title_font3 = ImageFont.truetype(font, 30)

        A1 = randrange(10)
        A2 = randrange(10)
        A11 = list(str(A1))
        A22 = list(str(A2))
        A1_1 = str(A11[0])+str(randrange(10))
        A1_2 = str(A11[0])+str(randrange(10))
        A1_3 = str(A11[0])+str(randrange(10))
        A1_4 = str(A11[0])+str(randrange(10))
        A2_1 = str(A22[0])+str(randrange(10))
        A2_2 = str(A22[0])+str(randrange(10))
        A2_3 = str(A22[0])+str(randrange(10))
        A2_4 = str(A22[0])+str(randrange(10))
        A111 = [A1_1, A1_2, A1_3, A1_4]
        A222 = [A2_1, A2_2, A2_3, A2_4]
        ABidnex3 = [A1_1, A1_2, A1_3, A1_4, A2_1, A2_2, A2_3, A2_4]

        idnex3_1 = random.choice(ABidnex3)
        idnex3_2 = random.choice(ABidnex3)
        idnex3_3 = random.choice(ABidnex3)
        if (idnex3_1 == idnex3_2):
            idnex3_2 = random.choice(ABidnex3)
            if (idnex3_2 == idnex3_1):
                idnex3_2 = random.choice(ABidnex3)
        elif (idnex3_2 == idnex3_3):
            idnex3_3 = random.choice(ABidnex3)
            if (idnex3_3 == idnex3_2):
                idnex3_2 = random.choice(ABidnex3)

        if (idnex3_1 == idnex3_3):
            idnex3_3 = random.choice(ABidnex3)
            if (idnex3_3 == idnex3_1):
                idnex3_3 = random.choice(ABidnex3)

        index333 = [idnex3_1, idnex3_2, idnex3_3]

        print('A1:%d\tA2:%d\n' % (A1, A2))
        print("A:  %s\t%s\t%s\t%s\n" % (A1_1, A1_2, A1_3, A1_4))
        print("B:  %s\t%s\t%s\t%s\n" % (A2_1, A2_2, A2_3, A2_4))
        print(A111)
        print(A222)
        print(index333)

        # ==========================================================================================
        image_editable = ImageDraw.Draw(results)
        # print('\n')
        image_editable.text((250, 60), title_text,
                            (255, 195, 0), font=title_font1)
        image_editable.text((210, 200), str(
            A1), (255, 195, 0), font=title_font2)
        image_editable.text((350, 200), str(
            text1), (255, 195, 0), font=title_font2)
        image_editable.text((550, 200), str(
            A2), (255, 195, 0), font=title_font2)

        for i in range(0, len(A111)):
            temp = i*100
            image_editable.text(
                (250+temp, 300), A111[i], (255, 195, 0), font=title_font3)

        for i in range(0, len(A222)):
            temp = i*100
            image_editable.text(
                (250+temp, 350), A222[i], (255, 195, 0), font=title_font3)

        for i in range(0, len(index333)):
            temp = i*100
            image_editable.text(
                (300+temp, 500), index333[i], (255, 195, 0), font=title_font3)

        image_editable.text(
            (340, 600), nameHH[j], (255, 195, 0), font=title_font3)

        daytimes = str(day)
        results.save("raffle%s/img%d.jpg" % (daytimes, j))

        j = j+1
        print(i)
        print('\n\n\n')
    print('Seccess full%d' % (i))
    background.config(text='Image created successfully', anchor=NW)

def result():
    try:
        global daytime
        for i in range(0, lenimg):
            os.remove("NewimgSystem/imgTest%d.jpg" % (i))
        print("remov img %d" % (i))
        root.destroy()
    except:
        root.destroy()

def Showimg(name):
    canvas.delete('all')
    if (name == 'datas'):
        background.config(text=nameHH)
    if (name == 'clear'):
        background.config(image='')
        background.config(width=72, height=25)
        return

    imgopae = Image.open('img/'+name+'.jpg')
    base_w = 550
    withbase = base_w/float(imgopae.size[0])
    heightbase = int(float(imgopae.size[1])*float(withbase))
    img = ImageTk.PhotoImage(imgopae.resize((base_w, heightbase), resample=3))
    canvas.create_image(0, 0, anchor=NW, image=img)
    canvas.image = img
    canvas.pack()
    if (name == 'datas'):
        background.config(text=nameHH, anchor=NW)

try:
   LabelTitlte = Label(text='Show Image')
   LabelTitlte.config(font='none 24', anchor=CENTER, width=30)
   btnHeadimg = Button(text='show', width=10, command=lambda: Showimg('datas'))
   btt1 = Button(text='Create', width=10, command=show)
   btt2 = Button(text='close', width=10, command=result)
   btt3 = Button(text='open file', width=10, command=browseFiles)

   lans = 95
   LabelTitlte.pack()
   background = Label(borderwidth=2, relief='groove', width=72, height=25)
   canvas = Canvas(background, width=500, height=350)
   background.place(x=20, y=100)

   btt3.place(x=10+(lans*1), y=60)
   btnHeadimg.place(x=10+(lans*2), y=60)
   btt1.place(x=10+(lans*3), y=60)
   btt2.place(x=10+(lans*4), y=60)
except:
    popupmsg("ERROR")

root.mainloop()

