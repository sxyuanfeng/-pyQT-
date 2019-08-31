# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xuanzhuan.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import file_path
import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image

file_path_xuanzhuan = file_path


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(631, 526)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(3, 1, 621, 421))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(file_path_xuanzhuan))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 450, 271, 51))
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setMaximum(360)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 430, 81, 81))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:/opencv_jk/添加.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(81, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 430, 81, 81))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("E:/opencv_jk/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(81, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 430, 81, 81))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:/opencv_jk/删除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(81, 81))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.tianjia)
        self.pushButton_2.clicked.connect(self.baocun)
        self.pushButton_3.clicked.connect(self.shanchu)
        self.horizontalSlider.sliderReleased.connect(self.released)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def released(self):
        global file_path_xuanzhuan
        im = Image.open(file_path_xuanzhuan)
        val = self.horizontalSlider.value()
        im_rotate = im.rotate(val)
        im_rotate.save("E:/opencv_huancun/"+ "xuanzhuan" + ".jpg")
        self.label.setPixmap(QtGui.QPixmap("E:/opencv_huancun/xuanzhuan.jpg"))

    def tianjia(self):
        global file_path_xuanzhuan
        root = tk.Tk()
        root.withdraw()
        file_path_xuanzhuan = filedialog.askopenfilename()
        self.label.setPixmap(QtGui.QPixmap(file_path_xuanzhuan))

    def baocun(self):
        root = tk.Tk()
        root.withdraw()
        file_path_baocun = filedialog.asksaveasfilename(filetypes = [("picture", ".jpg")])
        dst = cv2.imread("E:/opencv_huancun/xuanzhuan.jpg")
        cv2.imwrite(file_path_baocun + ".jpg", dst)

    def shanchu(self):
        self.label.clear()