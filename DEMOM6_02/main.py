from datetime import datetime
import pandas as pd
import os
from numpy import random
from tkinter.font import *
from tkinter import *
from random import randrange
from PIL import Image, ImageFont, ImageDraw

def setDate():
   global datess
   ischeckDate = False
   now = datetime.now()
   year = now.strftime("%Y")
   month = now.strftime("%m")
   day = now.strftime("%d")
   time = now.strftime("%H:%M:%S")
   date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
   datess = now.strftime("%m/%d")
   m = now.strftime("%M")
   oday = 26
   om = 50
   if (int(day) >= oday):
      # os.remove("img/temp.jpg")
      ischeckDate = True
      print("Lest Time")
   else:
         print("now Time1 ")

   if (int(m) >= om):
         # os.remove("img/temp.jpg")
         ischeckDate = True
         print("Lest Time")
   else:
         print("now Time2")

   return ischeckDate


def setpastFile():
   global lenimg, imgCall, nameHH, datess
   now = datetime.now()
   xx = now.strftime("%m-%d")
   df = pd.read_csv("dbTest.csv")
   # df = pd.read_csv("data/d56.csv")
   nameHH = df['namelottery']
   lenimg = len(nameHH)
   print("LEN: ", lenimg)
   imgCall = []

   os.chdir(r"D:")
   os.mkdir("raffle"+str(xx))

def createImgLoop():
   global imgCall, createImgLoop, nameHH, lenimg
   imgbackHead = Image.open("H5.jpg")
   for i in range(0, lenimg):
         imgbackHead.save("imgTest%d.jpg" % (i))
         print("Pass%d" % (i))


def show():
   global imgCall, datess, nameHH, lenimg
   print("=============show===================")
   createImgLoop()
   j = 0
   font = "K2D-Bold.ttf"
   for i in range(0, lenimg):
      results = Image.open("imgTest%d.jpg" % (i))
      # title_font1 = ImageFont.truetype(font, 500)
      title_font2 = ImageFont.truetype(font, 50)
      title_font3 = ImageFont.truetype(font, 30)
      title_font4 = ImageFont.truetype(font, 20)
      title_font5 = ImageFont.truetype(font, 10)
      


      A1 = randrange(0, 5)
      A2 = randrange(6, 9)
      listA1 = []
      listA2 = []
      listA3 = []

      nums1 = list(range(0, 10))
      random.shuffle(nums1)
      nums2 = list(range(0, 10))
      random.shuffle(nums2)
      nums3 = list(range(0, 100))
      random.shuffle(nums3)

      for i in range(0, 4):
         listA1.append(str(A1)+str(nums1[i*2]))
         listA2.append(str(A2)+str(nums2[i+2]))
         listA3.append(str(randrange(0, 9))+str(nums3[i]))
                  # print("A1:%d\tA2:%d" % (A1, A2))
                  # print("listA1: ", listA1)
                  # print("listA2: ", listA2)
                  # print("listA3: ", listA3)

         now = datetime.now()
         cllanda = now.strftime("%m/%d/%Y")
         W = 500 
         w2 = int(W/2)
         H = 500
         h2 = int(H/2)

         image_editable = ImageDraw.Draw(results)
            
         image_editable.text((400,30), str(cllanda), (255, 207, 0), font = title_font5)

         image_editable.text((((w2-100)-15), 100), str(
            A1), (255, 207,0), font=title_font2)
      
         image_editable.text((((w2+100)-15), 100), str(
            A2), (255, 207,0), font=title_font2)

      for i in range(0, len(listA1)):
         temp = i*60
         image_editable.text((150+temp,200), listA1[i], (255, 207,0), font=title_font3)

      for i in range(0, len(listA2)):
         temp = i*60
         image_editable.text(
            (150+temp, 250), listA2[i], (255, 207, 0), font=title_font3)

      for i in range(0, len(listA3)):
         temp = i*60
         image_editable.text(
            (150+temp, 300), listA3[i], (255, 207,0), font=title_font4)
            

        

   
      Ws = 500
      Hs =350

      _, _, ws, hs = image_editable.textbbox((0, 0), nameHH[j], font=title_font4)

      
      image_editable.text(
         (((Ws-ws)/2)-10, 350), nameHH[j], (255, 255, 255), font=title_font3)
      


      now = datetime.now()
      xx = now.strftime("%m-%d")
      daytimes = str(xx)
      results.save("raffle%s/img%d.jpg" % (daytimes, j))
      j = j+1

def deleteImgTemp():
   global daytime
   for i in range(0, lenimg):
      os.remove("imgTest%d.jpg" % (i))
   print("remov img %d" % (i))
   


def getProcess1():
   # try:
   #     if (setDate == True):
   #         print("EOORE TIME OUT")
   #     else:
   #         setpastFile()
   #         show()
   #     deleteImgTemp()
   # except:
   #     demoApp.destroy()

   if (setDate == True):
         print("EOORE TIME OUT")
   else:
         setpastFile()
         show()
   deleteImgTemp()


   
getProcess1()
