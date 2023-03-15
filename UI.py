from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import tensorflow as tf
from GCinterfaceUI_Fun import GC_Fun 
from DataBaseUI_Fun import FaceDatabase_Fun
from GarbageClassify_intenface import *
from database.connectsqlite import *
import numpy as np
import random
from PIL import Image
import cv2
import os
import sys
import shutil

class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.btn_style = CommonHelper.readQss("ui_frame/qss/btn_mac.qss")
        self.lineEdit_style = CommonHelper.readQss(
            "ui_frame/qss/lineEdit_mac.qss")

        

        self.setupUi_MW(self)

        self.gc_page()

    def write_msg(self, msg):
        # signal_write_msg信号会触发这个函数
        """
        功能函数，向接收区写入数据的方法
        信号-槽触发
        tip：PyQt程序的子线程中，直接向主线程的界面传输字符是不符合安全原则的
        :return: None
        """
        self.data_log.insertPlainText(msg)
        # 滚动条移动到结尾
        self.data_log.moveCursor(QtGui.QTextCursor.End)

    def setupUi_MW(self, MW):
        MW.setObjectName("GC")
        MW.setWindowTitle("深度学习图像垃圾分类")
        # self.resize(1100, 800)
        MW.setFixedSize(1100, 800)
        #新页面布局
        self.centralwidget = QtWidgets.QWidget(MW)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(QtCore.QRect(220, 0, 800, 800))

        self.verticalLayoutWidget = QtWidgets.QWidget(MW)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 0, 850, 800))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # self.verticalLayoutWidget.setStyleSheet("background:rgb(0,255,0)")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        #新页面布局

        # ---------------------------模式切换按钮--------------------------
        self.buttonarea = QtWidgets.QWidget(MW)
        self.buttonarea.setObjectName("photo")
        self.buttonarea.setGeometry(QtCore.QRect(10, 20, 200, 750))
        # self.buttonarea.setStyleSheet("background:#ff0000")

        

        self.vid_mode = QtWidgets.QPushButton(self.buttonarea)
        self.vid_mode.setGeometry(QtCore.QRect(15, 20, 180, 50))
        font = QtGui.QFont()
        font.setBold(True)
        # font.setUnderline(True)
        font.setWeight(75)
        self.vid_mode.setFont(font)
        self.vid_mode.setStyleSheet(self.btn_style)
        self.vid_mode.setObjectName("vid_mode")

        self.cam_mode = QtWidgets.QPushButton(self.buttonarea)
        self.cam_mode.setGeometry(QtCore.QRect(15, 120, 180, 50))
        font = QtGui.QFont()
        font.setBold(True)
        # font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.cam_mode.setFont(font)
        self.cam_mode.setStyleSheet(self.btn_style)
        self.cam_mode.setObjectName("cam_mode")

        # Logo
        self.label_log = QtWidgets.QLabel(self.buttonarea)
        self.label_log.setGeometry(QtCore.QRect(15, 240, 180, 490))
        font = QtGui.QFont()
        font.setWeight(12)
        font.setBold(True)
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_log.setFont(font)
        self.label_log.setText("\n数据日志")
        self.label_log.setObjectName("label")
        self.label_log.setStyleSheet("background-color:#fff;color:rgb(37,37,38);border-radius: 15px;")
        self.label_log.setAlignment(Qt.AlignHCenter)

        self.data_log = QtWidgets.QTextEdit(self.buttonarea)
        self.data_log.setGeometry(QtCore.QRect(22, 280, 166, 430))
        self.data_log.setStyleSheet(self.lineEdit_style)

        self.vid_mode.clicked.connect(self.gc_page)
        self.cam_mode.clicked.connect(self.database_page)

        # Logo

        # self.setupUi_GC(self)
        self.retranslateUi_main()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi_main(self):
        _translate = QtCore.QCoreApplication.translate

        self.vid_mode.setText(_translate("", "垃圾分类"))
        self.cam_mode.setText(_translate("", "数据库记录"))

    #face record
    def gc_page(self):
        print("=====1111")
        for i in range(self.verticalLayout.count()):
            self.verticalLayout.itemAt(i).widget().close_all()
        self.verticalLayout.addWidget(GC_Fun(self.data_log))
    #check in record
    def database_page(self):
        print("=====2222")

        for i in range(self.verticalLayout.count()):
            self.verticalLayout.itemAt(i).widget().close_all()
        self.verticalLayout.addWidget(FaceDatabase_Fun())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())