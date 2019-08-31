# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'masaike.ui'
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
import numpy as np


file_path_masaike = file_path


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(627, 527)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lb = QtWidgets.QLabel(Form)
        self.lb.setGeometry(QtCore.QRect(3, 1, 621, 421))
        self.lb.setObjectName("lb")
        self.label = MyLabel(self.lb)
        self.label.setGeometry(QtCore.QRect(3, 1, 621, 421))
        self.label.setPixmap(QtGui.QPixmap(file_path_masaike))
        self.label.setScaledContents(True)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 430, 90, 90))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:/opencv_jk/添加.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(90, 90))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 430, 90, 90))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("E:/opencv_jk/删除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 430, 90, 90))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:/opencv_jk/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.tianjia)
        self.pushButton_3.clicked.connect(self.baocun)
        self.pushButton_2.clicked.connect(self.shanchu)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def mosaic(self, selected_image, nsize=3):
        rows = self.label.x1 - self.label.x0
        cols = self.label.y1 - self.label.y0
        dist = selected_image.copy()
        # 划分小方块，每个小方块填充随机颜色
        for y in range(0, rows, nsize):
            for x in range(0, cols, nsize):
                dist[y:(y + nsize), x:(x + nsize)] = (np.random.randint(0, 255),
                    np.random.randint(0, 255), np.random.randint(0, 255))
        return dist

    def tianjia(self):
        global file_path_masaike
        root = tk.Tk()
        root.withdraw()
        file_path_masaike = filedialog.askopenfilename()
        self.label.setPixmap(QtGui.QPixmap(file_path_masaike))

    def baocun(self):
        global file_path_masaike
        root = tk.Tk()
        root.withdraw()
        file_path_baocun = filedialog.asksaveasfilename(filetypes=[("picture", ".jpg")])
        rect = {}
        rect['x'] = self.label.x0
        rect['y'] = self.label.y0
        width = self.label.x1 - self.label.x0
        height = self.label.y1 - self.label.y0
        rect['width'] = width
        rect['height'] = height
        img = cv2.imread(file_path_masaike)
        img_cpy = img.copy()
        select_image = img_cpy[rect['y']:(rect['y'] + rect['height']), rect['x']:(rect['x'] + rect['width'])]
        result = self.mosaic(select_image)
        # 将处理完成的区域合并回原图像
        img_cpy[rect['y']:(rect['y'] + rect['height']), rect['x']:(rect['x'] + rect['width'])] = cv2.addWeighted(result, 0.65, select_image, 0.35, 0)
        cv2.imwrite(file_path_baocun + ".jpg", img_cpy)

    def shanchu(self):
        self.label.clear()