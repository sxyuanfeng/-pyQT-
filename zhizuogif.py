# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhizuogif.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from pylab import *


allfile = []


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(626, 643)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 120, 621, 421))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 550, 90, 90))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:/opencv_jk/添加.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(90, 90))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 550, 90, 90))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("E:/opencv_jk/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 550, 90, 90))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:/opencv_jk/删除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 10, 90, 91))
        self.pushButton_4.setText("")
        self.pushButton_4.setIconSize(QtCore.QSize(90, 91))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 10, 90, 91))
        self.pushButton_5.setText("")
        self.pushButton_5.setIconSize(QtCore.QSize(90, 91))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 10, 90, 91))
        self.pushButton_6.setText("")
        self.pushButton_6.setIconSize(QtCore.QSize(90, 91))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(310, 10, 90, 91))
        self.pushButton_7.setText("")
        self.pushButton_7.setIconSize(QtCore.QSize(90, 91))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(410, 10, 90, 91))
        self.pushButton_8.setText("")
        self.pushButton_8.setIconSize(QtCore.QSize(90, 91))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(520, 40, 90, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color: rgb(0, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.tianjia)
        self.pushButton_2.clicked.connect(self.baocun)
        self.pushButton_3.clicked.connect(self.shanchu)
        self.pushButton_9.clicked.connect(self.queding)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_9.setText(_translate("Form", "确  定"))

    def tianjia(self):
        global allfile
        root = tk.Tk()
        root.withdraw()
        allfile = filedialog.askopenfilenames()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(allfile[0]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(allfile[1]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(allfile[2]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(allfile[3]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(allfile[4]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon7)

    def queding(self):
        global allfile
        outfilename = "E:/opencv_huancun/mygif.gif"  # 转化的GIF图片名称
        frames = []
        for image_name in allfile:
            im = Image.open(image_name)  # 读取方式上存在略微区别，由于是直接读取数据，并不需要后续处理
            frames.append(im)
        im.save(outfilename, save_all=True, append_images=frames, loop=0, duration=1, comment=b"aaabb")
        movie = QtGui.QMovie("E:/opencv_huancun/mygif.gif")
        movie.setCacheMode(QtGui.QMovie.CacheAll)
        # 播放速度
        movie.setSpeed(100)
        # 将gif显示在label上
        self.label.setMovie(movie)
        # 开始播放，对应的是movie.start()
        movie.start()

    def baocun(self):
        root = tk.Tk()
        root.withdraw()
        file_path_baocun = filedialog.asksaveasfilename(filetypes=[("picture", ".gif")])
        shutil.copyfile("E:/opencv_huancun/mygif.gif", file_path_baocun + '.gif')

    def shanchu(self):
        self.label.clear()