import customtkinter 
from  tkinter import *
from tkinter import messagebox
import mysql.connector
import tkinter as tk
from PIL import Image, ImageTk,ImageFont, ImageDraw
import os
from numpy import random
from random import randrange
from datetime import datetime
connection = mysql.connector.connect(
    host='mysql-113584-0.cloudclusters.net',
    user='user_M6',
    password='qwer/.,m',
    port='16144',
    database='db_M6'

    # host='202.28.34.250',
    # user=' DB_64011212049',
    # password='Max2003_01',
    # port='4096',
    # database='DB65'
)
c = connection.cursor()
nameHH = []

app = customtkinter.CTk()
app.title("Login")
app.config(bg="#242320")
font1=('Arial',15,'bold')
font2=('Arial',20,'bold')
def close_window():
    app.destroy()

class loginForm:
   def __init__(self,master):
       w = 350
       h = 400
       self.master = master
       ws = self.master.winfo_screenwidth()
       hs = self.master.winfo_screenheight()
       x = (ws-w)/2
       y = (hs-h)/2
       self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
      
       self.frame = customtkinter.CTkFrame(self.master)

       image_path = os.path.join(os.path.dirname(
           os.path.realpath(__file__)), "test_images")
       
       self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "D:\DEMOM6_02\ProgramM6_v1\M6.png")), size=(150, 150))
       self.navigation_frame_label = customtkinter.CTkLabel(self.frame, image=self.logo_image,
                                                     compound="center")
                
       self.username_label = customtkinter.CTkLabel(
           self.frame, text="Username:", font=font1, text_color="#FFFFFF")
       
    
       self.password_lable = customtkinter.CTkLabel(
           self.frame, text="Password:", font=font1, text_color="#FFFFFF")
       
       self.username_entry = customtkinter.CTkEntry(
           self.frame, fg_color="#FFFFFF", font=font1, text_color="#000000", border_color='#FFFFFF', width=200, height=1)
       
       self.password_entry = customtkinter.CTkEntry(
         self.frame, show='*', fg_color="#FFFFFF", font=font1, text_color="#000000", border_color='#FFFFFF', width=200, height=1)
       
       self.login_button = customtkinter.CTkButton(
           self.frame, command=self.login_func, text='Login', font=font1, text_color='#FFFFFF', fg_color='#07b527', hover_color='#07b527', width=50)
       
       self.frame.pack(fill='both',side='top',expand='True')
       self.navigation_frame_label.place(x=100, y=0)
       self.nums = 30
       self.username_label.place(x=20, y=120+self.nums)
       self.password_lable.place(x=20, y=170+self.nums)
       self.username_entry.place(x=100, y=125+self.nums)
       self.password_entry.place(x=100, y=175+self.nums)
       self.login_button.place(x=150, y=250+self.nums)

   def login_func(self):
         username = self.username_entry.get()
         password = self.password_entry.get()
         select_query = 'SELECT * FROM `usercustomer` WHERE `username` = %s and password = %s'
         vals = (username, password,)
         c.execute(select_query, vals)
         
         # print(c.fetchall())
         user = c.fetchone()
         if user is not None:
               # messagebox.showinfo('Login', 'Yes')
               mainformwindow = tk.Toplevel()
               new = mainform(mainformwindow,user=username)
               app.withdraw()
               mainformwindow.protocol('WM_DELETE_WINDOW', close_window)
         else:
               messagebox.showwarning(
                  'Error', 'Enter a Valid Username & Password')
      
class mainform:
    def __init__(self,master,user): 
      global lening
      w = 760
      h = 600
      self.master = master
        # ----------- CENTER FORM ------------- #
      ws = self.master.winfo_screenwidth()
      hs = self.master.winfo_screenheight()
      x = (ws-w)/2
      y = (hs-h)/2
      self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

      self.frame = customtkinter.CTkFrame(self.master)
      self.frame.pack(fill='both',side='top',expand='True')
      self.master.config(bg="#2A2C2B")
      
      # self.lbl = tk.Label(self.master, text='Main Form', font=(
      #    'verdana', 50, 'bold'), fg='#ecf0f1', bg="#2A2C2B")
      # self.lbl.place(rely=0.5, relx=0.5, anchor=CENTER)

      def getdata():
          vars = namevar.get()
          print("vasget:",vars)
          tempS = vars.split('-')
          if (tempS[0]=='1'):
              nameHH.append(tempS[1])
          elif(tempS[0]=='0'):
               nameHH.remove(tempS[1])
          else:
               print("ERROR")

          print("C1 ", nameHH)

      def createImgLoop():
          global lens
          lens =  len(nameHH)
          print("lenTest:",lens)
          if(lens>0):
            imgbackHead = Image.open("H5.jpg")
            setpastFile()
            for i in range(0, lens):
               imgbackHead.save("imgtemp%d.jpg" % (i))
               print("Pass%d" % (i))

            ms  = messagebox.askquestion("Test",'You can Create Image sush')
            if(ms=='yes'):
                show()
                messagebox.showinfo('msee','Create Image succeed ')
                deleteImgTemp()
            else:
                deleteImgTemp()


      def deleteImgTemp():
           try:
                global daytime,lens
                for i in range(0, lens):
                    os.remove("imgtemp%d.jpg" % (i))
                print("remov img %d" % (i))
                app.destroy()
           except:
                now = datetime.now()
                xx = now.strftime("%m-%d")
                os.remove("raffle"+str(xx))
                app.destroy()


      def setpastFile():
            global nameHH, lens
            print("process : setpastFile")
            now = datetime.now()
            xx = now.strftime("%m-%d")
            try:
               ispath = os.path.isfile("raffle"+str(xx))
               print("this File agnal",ispath)
               if (ispath==True):
                  print("if: setpastFile")
                  os.remove("raffle"+str(xx))
               else:  
                  print("else: setpastFile")
                  os.chdir(r"D:")
                  os.mkdir("raffle"+str(xx))
            except:  
               messagebox.showerror(
                   'Error ', f'มีโพลเดอร์ raffle{str(xx)} อยู่แล้ว กรุณาลบโพลเดอร์ดังกล่าว')
               os.remove("raffle"+str(xx))
               print("Except: setpastFile",ispath)

      def show():
         global nameHH, lens
         print("=============show===================")
         j = 0
         font = "K2D-Bold.ttf"
         for i in range(0, lens):
               results = Image.open("imgtemp%d.jpg" % (i))

               # title_font1 = ImageFont.truetype(font, 500)
               title_font2 = ImageFont.truetype(font, 50)
               title_font3 = ImageFont.truetype(font, 30)
               title_font4 = ImageFont.truetype(font, 20)
               title_font5 = ImageFont.truetype(font, 10)
               


               A1 = randrange(0, 9)
               A2 = randrange(0, 9)
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
               # ==========================================================================================
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

               _, _, ws, hs = image_editable.textbbox(
                   (0, 0), nameHH[j], font=title_font4)
   
            
               image_editable.text(
                   (((Ws-ws)/2)-10, 350), nameHH[j], (255, 255, 255), font=title_font3)
               


               now = datetime.now()
               xx = now.strftime("%m-%d")
               daytimes = str(xx)
               results.save("raffle%s/img%d.jpg" % (daytimes, j))
               # results.save("img%d.jpg" % (j))
               j = j+1



# ////////////////////////////////////////////////////

      namevar = StringVar()


      self.user_label = customtkinter.CTkLabel(self.frame,text=f'Welcome {user}',font=font2, text_color="#FFFFFF")

      name1 = 'ลาว TV'
      name2 = 'ลาว'
      name3 = 'ฮานอย HD'
      name4 = 'ลาวพิเศษ'
      name5 = 'ฮานอยสตาร์'

      name6 = 'ลาว HD'
      name7 = 'ฮานอย TV'
      name8 = 'ลาวสตาร์'
      name9 = 'ฮานอยกาชาด'
      name10 = 'ฮานอยสามัคคี'
      
      

      self.checkBox1 = customtkinter.CTkCheckBox(self.frame, text=name1, font=font2, text_color="#FFFFFF", checkbox_height=20,
                                                 checkbox_width=20,   variable=namevar, onvalue=f"1-{name1}", offvalue=f'0-{name1}', command=getdata)
      
      self.checkBox2 = customtkinter.CTkCheckBox(self.frame, text=name2, font=font2, text_color="#FFFFFF",
                                                 checkbox_height=20, checkbox_width=20, variable=namevar, onvalue=f"1-{name2}", offvalue=f'0-{name2}', command=getdata)
      
      self.checkBox3 = customtkinter.CTkCheckBox(self.frame, text=name3, font=font2, text_color="#FFFFFF",
                                                 checkbox_height=20, checkbox_width=20, variable=namevar, onvalue=f"1-{name3}", offvalue=f'0-{name3}', command=getdata)
      
      self.checkBox4 = customtkinter.CTkCheckBox(self.frame, text=name4, font=font2, text_color="#FFFFFF",
                                                 checkbox_height=20, checkbox_width=20, variable=namevar, onvalue=f"1-{name4}", offvalue=f'0-{name4}', command=getdata)

      self.checkBox5 = customtkinter.CTkCheckBox(self.frame, text=name5, font=font2, text_color="#FFFFFF",
                                                 checkbox_height=20, checkbox_width=20, variable=namevar, onvalue=f"1-{name5}", offvalue=f'0-{name5}', command=getdata)


      self.checkBox6 = customtkinter.CTkCheckBox(self.frame, text=name6, font=font2, text_color="#FFFFFF", checkbox_height=20,
                                                 checkbox_width=20,   variable=namevar, onvalue=f"1-{name6}", offvalue=f'0-{name6}', command=getdata)
      
      self.checkBox7 = customtkinter.CTkCheckBox(self.frame, text=name7, font=font2, text_color="#FFFFFF",
                                                 checkbox_height=20, checkbox_width=20, variable=namevar, onvalue=f"1-{name7}", offvalue=f'0-{name7}', command=getdata)
      
      self.checkBox8 = customtkinter.CTkCheckBox(self.frame, text=name8, font=font2, text_color="#FFFFFF",
                                                 checkbox_height=20, checkbox_width=20, variable=namevar, onvalue=f"1-{name8}", offvalue=f'0-{name8}', command=getdata)
      
      self.checkBox9 = customtkinter.CTkCheckBox(self.frame, text=name9, font=font2, text_color="#FFFFFF",
                                                 checkbox_height=20, checkbox_width=20, variable=namevar, onvalue=f"1-{name9}", offvalue=f'0-{name9}', command=getdata)

      self.checkBox10 = customtkinter.CTkCheckBox(self.frame, text=name10, font=font2, text_color="#FFFFFF",
                                                 checkbox_height=20, checkbox_width=20, variable=namevar, onvalue=f"1-{name10}", offvalue=f'0-{name10}', command=getdata)


      
      
      self.OKButton = customtkinter.CTkButton(
          self.frame, text='Create Temp', font=font1, text_color='#FFFFFF', fg_color='#07b527', hover_color='#07b527', width=50, command=createImgLoop)

      self.tempidstand  = 150
      self.user_label.place(x=10,y=10)

      distesnY1 = 50
      distesnY2 = 100


      self.checkBox1.place(x=20+(self.tempidstand)*0, y=distesnY1)
      self.checkBox2.place(x=20+(self.tempidstand)*1, y=distesnY1)
      self.checkBox3.place(x=20+(self.tempidstand)*2,y=distesnY1)
      self.checkBox4.place(x=20+(self.tempidstand)*3,y=distesnY1)
      self.checkBox5.place(x=20+(self.tempidstand)*4, y=distesnY1)

      self.checkBox6.place(x=20+(self.tempidstand)*0, y=distesnY2)
      self.checkBox7.place(x=20+(self.tempidstand)*1, y=distesnY2)
      self.checkBox8.place(x=20+(self.tempidstand)*2, y=distesnY2)
      self.checkBox9.place(x=20+(self.tempidstand)*3, y=distesnY2)
      self.checkBox10.place(x=20+(self.tempidstand)*4, y=distesnY2)

      self.OKButton.place(x=200,y=500)
      
      

   
   


def main():
    login_window = loginForm(app)
    app.mainloop()


if __name__ == '__main__':
    main()

# app.mainloop()