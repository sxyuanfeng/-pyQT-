# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tianjiawenzi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from mylabel import MyLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import file_path
import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageFont, ImageDraw
from pylab import *


file_path_tianjiawenzi = file_path


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(627, 600)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lb = QtWidgets.QLabel(Form)
        self.lb.setGeometry(QtCore.QRect(0, 70, 621, 421))
        self.lb.setObjectName("lb")
        self.label = MyLabel(self.lb)
        self.label.setGeometry(QtCore.QRect(3, 1, 621, 421))
        self.label.setPixmap(QtGui.QPixmap(file_path_tianjiawenzi))
        self.label.setScaledContents(True)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 500, 90, 90))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:/opencv_jk/添加.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(90, 90))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 500, 90, 90))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("E:/opencv_jk/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 500, 90, 90))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:/opencv_jk/删除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(0, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(340, 20, 69, 31))
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        tt = [['FZSTK'], ['simhei'], ['simsunb'], ['STCAIYUN'], ['STHUPO'], ['STLITI'], ['STXINGKA']]
        for i in tt:
            self.comboBox.addItem(i[0])
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(470, 20, 69, 31))
        self.comboBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        hh = [['10'], ['12'], ['14'], ['16'], ['18'], ['20'], ['22'], ['24'], ['26'], ['28'], ['30'], ['32'], ['34'],
              ['36'], ['38'], ['40'], ['42'], ['44'], ['46'], ['48'], ['50']]
        for i in hh:
            self.comboBox_2.addItem(i[0])
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(290, 20, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(420, 20, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.tianjia)
        self.pushButton_2.clicked.connect(self.baocun)
        self.pushButton_3.clicked.connect(self.shanchu)
        self.pushButton_4.clicked.connect(self.queding)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Adobe Arabic\'; font-size:22pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "确定"))
        self.label_2.setText(_translate("Form", "字体"))
        self.label_3.setText(_translate("Form", "大小"))

    def queding(self):
        global file_path_tianjiawenzi
        ziti = self.comboBox.currentText()
        daxiao = self.comboBox_2.currentText()
        size = int(daxiao)
        x = self.label.x0
        y = self.label.y0
        wenzi = self.textEdit.toPlainText()
        font = ImageFont.truetype('E:\opencv_jk\\' + ziti + '.ttf', size)
        # 使用自定义的字体，第二个参数表示字符大小
        im = Image.open(file_path_tianjiawenzi)
        # 生成空白图像
        draw = ImageDraw.Draw(im)
        # 绘图句柄
        draw.text((x, y), wenzi, font=font)
        im.save("E:/opencv_huancun/" + "tianjiawenzi" + ".jpg")
        self.label.setPixmap(QtGui.QPixmap("E:/opencv_huancun/tianjiawenzi.jpg"))

    def tianjia(self):
        global file_path_tianjiawenzi
        root = tk.Tk()
        root.withdraw()
        file_path_tianjiawenzi = filedialog.askopenfilename()
        self.label.setPixmap(QtGui.QPixmap(file_path_tianjiawenzi))

    def baocun(self):
        root = tk.Tk()
        root.withdraw()
        file_path_baocun = filedialog.asksaveasfilename(filetypes=[("picture", ".jpg")])
        dst = cv2.imread("E:/opencv_huancun/tianjiawenzi.jpg")
        cv2.imwrite(file_path_baocun + ".jpg", dst)

    def shanchu(self):
        self.label.clear()