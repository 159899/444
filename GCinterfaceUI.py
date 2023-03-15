from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()


class UI_GC(object):
    def __init__(self):
        super().__init__()
        self.btn_style = CommonHelper.readQss("ui_frame/qss/btn_mac.qss")
        self.lineEdit_style = CommonHelper.readQss(
            "ui_frame/qss/lineEdit_mac.qss")


    def setupUi_GC(self,GC):
        

        self.showarea = QtWidgets.QWidget(GC)
        self.showarea.setObjectName("photo")
        self.showarea.setGeometry(QtCore.QRect(0, 65, 850, 700))
        # self.showarea.setStyleSheet("background:#006400")


        self.label_page1 = QtWidgets.QLabel(self.showarea)
        self.label_page1.setGeometry(QtCore.QRect(30, 30, 800, 600))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.label_page1.setFont(font)
        self.label_page1.setText("Photo Here")
        self.label_page1.setObjectName("label")
        self.label_page1.setStyleSheet(
            "background:#fff ;border: 2px dashed #000;color:#000;border-radius: 15px;")
        self.label_page1.setAlignment(Qt.AlignCenter)

        self.label_file = QtWidgets.QLabel(self.showarea)
        self.label_file.setGeometry(QtCore.QRect(30, 650, 450, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_file.setFont(font)
        self.label_file.setText(" 文件目录：")
        self.label_file.setObjectName("label")
        self.label_file.setStyleSheet(
            "background:#fff ;border-radius: 15px;color:#616161")

        self.lineEdit = QtWidgets.QLineEdit(self.showarea)
        self.lineEdit.setGeometry(QtCore.QRect(120, 655, 350, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(self.lineEdit_style)
        # self.label_path.setAlignment(Qt.AlignCenter)

        self.open_pic_btn = QtWidgets.QPushButton(self.showarea)
        self.open_pic_btn.setGeometry(QtCore.QRect(600, 650, 100, 40))
        font = QtGui.QFont()
        font.setBold(True)
        # font.setUnderline(True)
        font.setWeight(75)
        self.open_pic_btn.setFont(font)
        self.open_pic_btn.setStyleSheet(self.btn_style)
        self.open_pic_btn.setObjectName("pushButton_4")
        self.pic_det_btn = QtWidgets.QPushButton(self.showarea)
        self.pic_det_btn.setGeometry(QtCore.QRect(710, 650, 100, 40))
        font = QtGui.QFont()
        font.setBold(True)
        # font.setUnderline(True)
        self.pic_det_btn.setFont(font)
        self.pic_det_btn.setStyleSheet(self.btn_style)
        self.pic_det_btn.setObjectName("pushButton_5")

        self.randomexp_btn = QtWidgets.QPushButton(self.showarea)
        self.randomexp_btn.setGeometry(QtCore.QRect(490, 650, 100, 40))
        font = QtGui.QFont()
        font.setBold(True)
        # font.setUnderline(True)
        font.setWeight(75)
        self.randomexp_btn.setFont(font)
        self.randomexp_btn.setStyleSheet(self.btn_style)
        self.randomexp_btn.setObjectName("randomexp_btn")

        


        
        #标志显示
        self.label_flag = QtWidgets.QLabel(GC)
        self.label_flag.setGeometry(QtCore.QRect(30, 20, 800, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(36)
        self.label_flag.setFont(font)
        self.label_flag.setText("垃圾分类")
        self.label_flag.setObjectName("label_flag")

        styleFile = 'ui_frame/qss/a.qss'
        qssStyle = CommonHelper.readQss(styleFile)
        self.label_flag.setStyleSheet(qssStyle)


        

        self.label_flag.setAlignment(Qt.AlignCenter)

        self.retranslateUi_page1(GC)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi_page1(self,UI_GC):
        _translate = QtCore.QCoreApplication.translate

        self.open_pic_btn.setText(_translate("GC", "打开图片"))
        self.pic_det_btn.setText(_translate("GC", "垃圾分类"))
        self.randomexp_btn.setText(_translate("GC", "随机示例"))
        # self.vid_mode.setText(_translate("GC", "视频识别"))
        # self.cam_mode.setText(_translate("GC", "实时识别"))

    
