# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo02.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
from tkinter.font import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from random import randrange
from PIL import Image, ImageFont, ImageDraw
from PIL import Image, ImageTk
from numpy import random
import os
import pandas as pd
from datetime import date
from tkinter import filedialog
from datetime import datetime


class Ui_demoApp(object):
    filess = ""
    dataList = []

    def setupUi(self, demoApp):
        demoApp.setObjectName("demoApp")
        demoApp.resize(550, 450)
        demoApp.setMinimumSize(QtCore.QSize(550, 450))
        demoApp.setMaximumSize(QtCore.QSize(550, 450))
        demoApp.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(demoApp)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 100, 551, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 1, 3, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 0, 3, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 2, 3, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 1, 2, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout.addWidget(self.checkBox_13, 2, 1, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout.addWidget(self.checkBox_14, 2, 2, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 1, 1, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout.addWidget(self.checkBox_15, 3, 1, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout.addWidget(self.checkBox_16, 3, 2, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 1, 4, 1, 1)
        self.checkBox_19 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_19.setObjectName("checkBox_19")
        self.gridLayout.addWidget(self.checkBox_19, 2, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 0, 2, 1, 1)
        self.checkBox_30 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_30.setObjectName("checkBox_30")
        self.gridLayout.addWidget(self.checkBox_30, 5, 4, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 0, 1, 1, 1)
        self.checkBox_25 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_25.setObjectName("checkBox_25")
        self.gridLayout.addWidget(self.checkBox_25, 4, 1, 1, 1)
        self.checkBox_23 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_23.setObjectName("checkBox_23")
        self.gridLayout.addWidget(self.checkBox_23, 4, 3, 1, 1)
        self.checkBox_29 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_29.setObjectName("checkBox_29")
        self.gridLayout.addWidget(self.checkBox_29, 5, 3, 1, 1)
        self.checkBox_26 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_26.setObjectName("checkBox_26")
        self.gridLayout.addWidget(self.checkBox_26, 5, 0, 1, 1)
        self.checkBox_28 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_28.setObjectName("checkBox_28")
        self.gridLayout.addWidget(self.checkBox_28, 5, 2, 1, 1)
        self.checkBox_27 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_27.setObjectName("checkBox_27")
        self.gridLayout.addWidget(self.checkBox_27, 5, 1, 1, 1)
        self.checkBox_22 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_22.setObjectName("checkBox_22")
        self.gridLayout.addWidget(self.checkBox_22, 4, 4, 1, 1)
        self.checkBox_20 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_20.setObjectName("checkBox_20")
        self.gridLayout.addWidget(self.checkBox_20, 3, 0, 1, 1)
        self.checkBox_21 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_21.setObjectName("checkBox_21")
        self.gridLayout.addWidget(self.checkBox_21, 4, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 4, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 4, 1, 1)
        self.checkBox_17 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_17.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_17.sizePolicy().hasHeightForWidth())
        self.checkBox_17.setSizePolicy(sizePolicy)
        self.checkBox_17.setTabletTracking(False)
        self.checkBox_17.setAutoFillBackground(True)
        self.checkBox_17.setObjectName("checkBox_17")
        self.gridLayout.addWidget(self.checkBox_17, 0, 0, 1, 1)
        self.checkBox_24 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_24.setObjectName("checkBox_24")
        self.gridLayout.addWidget(self.checkBox_24, 4, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 3, 4, 1, 1)
        self.checkBox_18 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_18.setObjectName("checkBox_18")
        self.gridLayout.addWidget(self.checkBox_18, 1, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 3, 3, 1, 1)
        self.checkBox_31 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_31.setGeometry(QtCore.QRect(120, 360, 81, 31))
        self.checkBox_31.setObjectName("checkBox_31")
        self.Create = QtWidgets.QPushButton(self.centralwidget)
        self.Create.setGeometry(QtCore.QRect(310, 360, 151, 41))
        self.Create.setCheckable(False)
        self.Create.setObjectName("Create")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 551, 431))
        self.textBrowser.setObjectName("textBrowser")
        # self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        # self.spinBox.setGeometry(QtCore.QRect(390, 40, 42, 22))
        # self.spinBox.setObjectName("spinBox")
        self.textBrowser.raise_()
        self.gridLayoutWidget.raise_()
        self.checkBox_31.raise_()
        self.Create.raise_()
        # self.spinBox.raise_()
        demoApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(demoApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        demoApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(demoApp)
        self.statusbar.setObjectName("statusbar")
        demoApp.setStatusBar(self.statusbar)

        self.retranslateUi(demoApp)
        self.checkBox_31.clicked.connect(self.checkBox_26.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_17.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_18.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_19.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_20.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_21.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_10.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_11.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_13.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_15.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_25.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_27.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_9.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_12.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_14.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_16.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_24.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_28.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_4.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_5.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_6.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_7.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_23.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_29.toggle)
        self.checkBox_31.clicked.connect(self.checkBox.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_8.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_3.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_2.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_22.toggle)
        self.checkBox_31.clicked.connect(self.checkBox_30.toggle)


    

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

        # def readFile():
        #     global results
        #     results ="data/databast02.csv"
        #     check_file = os.path.isfile(results)
        #     setpastFile(results)
        #     print(check_file)

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

                _, _, ws, hs = image_editable.textbbox((0, 0), nameHH[j], font=title_font4)
     
                
                image_editable.text(
                    (((Ws-ws)/2)-10, 350), nameHH[j], (255, 255, 255), font=title_font3)
                


                now = datetime.now()
                xx = now.strftime("%m-%d")
                daytimes = str(xx)
                results.save("raffle%s/img%d.jpg" % (daytimes, j))
                j = j+1
        

        def deleteImgTemp():
            try:
                global daytime
                for i in range(0, lenimg):
                    os.remove("imgTest%d.jpg" % (i))
                print("remov img %d" % (i))
                demoApp.destroy()
            except:
                demoApp.destroy()

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

        self.Create.clicked.connect(getProcess1)
        QtCore.QMetaObject.connectSlotsByName(demoApp)

    def retranslateUi(self, demoApp):
        _translate = QtCore.QCoreApplication.translate
        demoApp.setWindowTitle(_translate("demoApp", "demoM6"))
        self.checkBox_5.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_4.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_6.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_12.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_13.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_14.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_11.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_15.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_16.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_8.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_19.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_9.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_30.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_10.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_25.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_23.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_29.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_26.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_28.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_27.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_22.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_20.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_21.setText(_translate("demoApp", "CheckBox"))
        self.checkBox.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_3.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_17.setText(_translate("demoApp", "ลาว TV"))
        self.checkBox_24.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_2.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_18.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_7.setText(_translate("demoApp", "CheckBox"))
        self.checkBox_31.setText(_translate("demoApp", "All"))
        self.Create.setText(_translate("demoApp", "Create Image"))

        self.textBrowser.setHtml(_translate("demoApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">M6</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    demoApp = QtWidgets.QMainWindow()
    ui = Ui_demoApp()
    ui.setupUi(demoApp)
    demoApp.show()
    sys.exit(app.exec_())


class processN():
    print("process1")