# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FaceDatabase.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FaceDatabase(object):
    def setupUi_FaceDatabase(self, FaceDatabase):
        FaceDatabase.setObjectName("FaceDatabase")
        FaceDatabase.resize(800, 600)
        FaceDatabase.setStyleSheet("background-color:#3c3c3c;")
        # self.pushButton_search = QtWidgets.QPushButton(FaceDatabase)
        # self.pushButton_search.setGeometry(QtCore.QRect(160, 40, 101, 31))
        # font = QtGui.QFont()
        # font.setFamily("等线")
        # font.setPointSize(10)
        # font.setBold(True)
        # font.setWeight(75)
        # self.pushButton_search.setFont(font)
        # self.pushButton_search.setStyleSheet("QPushButton{\n"
        #                                      "    \n"
        #                                      "    color: rgb(255, 255, 255);\n"
        #                                      "    border-width: 1px;\n"
        #                                      "    border-radius: 6px;\n"
        #                                      "    border-bottom-color: rgb(150,150,150);\n"
        #                                      "    border-right-color: rgb(165,165,165);\n"
        #                                      "    border-left-color: rgb(165,165,165);\n"
        #                                      "    border-top-color: rgb(180,180,180);\n"
        #                                      "    border-style: solid;\n"
        #                                      "    padding: 4px;\n"
        #                                      "    background-color: rgb(69, 90, 100);\n"
        #                                      "}\n"
        #                                      "QPushButton:hover{\n"
        #                                      "    color: rgb(255, 255, 255);\n"
        #                                      "    border-width: 1px;\n"
        #                                      "    border-radius:6px;\n"
        #                                      "    border-top-color: rgb(255,150,60);\n"
        #                                      "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
        #                                      "    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
        #                                      "    border-bottom-color: rgb(200,70,20);\n"
        #                                      "    border-style: solid;\n"
        #                                      "    padding: 2px;\n"
        #                                      "    background-color: rgb(69, 90, 100);\n"
        #                                      "}\n"
        #                                      "QPushButton:default{\n"
        #                                      "    color: rgb(255, 255, 255);\n"
        #                                      "    border-width: 1px;\n"
        #                                      "    border-radius:6px;\n"
        #                                      "    border-top-color: rgb(255,150,60);\n"
        #                                      "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
        #                                      "    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
        #                                      "    border-bottom-color: rgb(200,70,20);\n"
        #                                      "    border-style: solid;\n"
        #                                      "    padding: 2px;\n"
        #                                      "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
        #                                      "}\n"
        #                                      "QPushButton:pressed{\n"
        #                                      "    color: rgb(255, 255, 255);\n"
        #                                      "    border-width: 1px;\n"
        #                                      "    border-radius: 6px;\n"
        #                                      "    border-width: 1px;\n"
        #                                      "    border-top-color: rgba(255,150,60,200);\n"
        #                                      "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
        #                                      "    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
        #                                      "    border-bottom-color: rgba(200,70,20,200);\n"
        #                                      "    border-style: solid;\n"
        #                                      "    padding: 2px;\n"
        #                                      "    \n"
        #                                      "    background-color: rgb(129, 156, 169);\n"
        #                                      "    \n"
        #                                      "}")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(":/icon/pic/search.png"),
        #                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.pushButton_search.setIcon(icon)
        # self.pushButton_search.setObjectName("pushButton_search")
        # self.pushButton_modify = QtWidgets.QPushButton(FaceDatabase)
        # self.pushButton_modify.setGeometry(QtCore.QRect(290, 40, 101, 31))
        # font = QtGui.QFont()
        # font.setFamily("等线")
        # font.setPointSize(10)
        # font.setBold(True)
        # font.setWeight(75)
        # self.pushButton_modify.setFont(font)
        # self.pushButton_modify.setStyleSheet("QPushButton{\n"
        #                                      "    \n"
        #                                      "    color: rgb(255, 255, 255);\n"
        #                                      "    border-width: 1px;\n"
        #                                      "    border-radius: 6px;\n"
        #                                      "    border-bottom-color: rgb(150,150,150);\n"
        #                                      "    border-right-color: rgb(165,165,165);\n"
        #                                      "    border-left-color: rgb(165,165,165);\n"
        #                                      "    border-top-color: rgb(180,180,180);\n"
        #                                      "    border-style: solid;\n"
        #                                      "    padding: 4px;\n"
        #                                      "    background-color: rgb(69, 90, 100);\n"
        #                                      "}\n"
        #                                      "QPushButton:hover{\n"
        #                                      "    color: rgb(255, 255, 255);\n"
        #                                      "    border-width: 1px;\n"
        #                                      "    border-radius:6px;\n"
        #                                      "    border-top-color: rgb(255,150,60);\n"
        #                                      "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
        #                                      "    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
        #                                      "    border-bottom-color: rgb(200,70,20);\n"
        #                                      "    border-style: solid;\n"
        #                                      "    padding: 2px;\n"
        #                                      "    background-color: rgb(69, 90, 100);\n"
        #                                      "}\n"
        #                                      "QPushButton:default{\n"
        #                                      "    color: rgb(255, 255, 255);\n"
        #                                      "    border-width: 1px;\n"
        #                                      "    border-radius:6px;\n"
        #                                      "    border-top-color: rgb(255,150,60);\n"
        #                                      "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
        #                                      "    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
        #                                      "    border-bottom-color: rgb(200,70,20);\n"
        #                                      "    border-style: solid;\n"
        #                                      "    padding: 2px;\n"
        #                                      "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
        #                                      "}\n"
        #                                      "QPushButton:pressed{\n"
        #                                      "    color: rgb(255, 255, 255);\n"
        #                                      "    border-width: 1px;\n"
        #                                      "    border-radius: 6px;\n"
        #                                      "    border-width: 1px;\n"
        #                                      "    border-top-color: rgba(255,150,60,200);\n"
        #                                      "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
        #                                      "    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
        #                                      "    border-bottom-color: rgba(200,70,20,200);\n"
        #                                      "    border-style: solid;\n"
        #                                      "    padding: 2px;\n"
        #                                      "    \n"
        #                                      "    background-color: rgb(129, 156, 169);\n"
        #                                      "    \n"
        #                                      "}")
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap(":/icon/pic/change.png"),
        #                 QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.pushButton_modify.setIcon(icon1)
        # self.pushButton_modify.setObjectName("pushButton_modify")
        self.tableWidget_db = QtWidgets.QTableWidget(FaceDatabase)
        self.tableWidget_db.setGeometry(QtCore.QRect(20, 40, 800, 650))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_db.setFont(font)
        self.tableWidget_db.setStyleSheet("background:#ffffff;color:#000000;border-style: solid;border-width: 1px;border-radius: 10px; border-color:#000000")
        self.tableWidget_db.setObjectName("tableWidget")
        self.tableWidget_db.setColumnCount(5)
        self.tableWidget_db.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        item.setFont(font)
        self.tableWidget_db.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setUnderline(False)
        item.setFont(font)
        self.tableWidget_db.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        item.setFont(font)
        self.tableWidget_db.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        item.setFont(font)
        self.tableWidget_db.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_db.setHorizontalHeaderItem(4, item)
        self.pushButton_delete = QtWidgets.QPushButton(FaceDatabase)
        self.pushButton_delete.setGeometry(QtCore.QRect(700, 700, 101, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setStyleSheet("QPushButton{\n"
                                             "    \n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    border-width: 1px;\n"
                                             "    border-radius: 6px;\n"
                                             "    border-bottom-color: rgb(150,150,150);\n"
                                             "    border-right-color: rgb(165,165,165);\n"
                                             "    border-left-color: rgb(165,165,165);\n"
                                             "    border-top-color: rgb(180,180,180);\n"
                                             "    border-style: solid;\n"
                                             "    padding: 4px;\n"
                                             "    background-color: rgb(69, 90, 100);\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    border-width: 1px;\n"
                                             "    border-radius:6px;\n"
                                             "    border-top-color: rgb(255,150,60);\n"
                                             "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
                                             "    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
                                             "    border-bottom-color: rgb(200,70,20);\n"
                                             "    border-style: solid;\n"
                                             "    padding: 2px;\n"
                                             "    background-color: rgb(69, 90, 100);\n"
                                             "}\n"
                                             "QPushButton:default{\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    border-width: 1px;\n"
                                             "    border-radius:6px;\n"
                                             "    border-top-color: rgb(255,150,60);\n"
                                             "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
                                             "    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
                                             "    border-bottom-color: rgb(200,70,20);\n"
                                             "    border-style: solid;\n"
                                             "    padding: 2px;\n"
                                             "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                             "}\n"
                                             "QPushButton:pressed{\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    border-width: 1px;\n"
                                             "    border-radius: 6px;\n"
                                             "    border-width: 1px;\n"
                                             "    border-top-color: rgba(255,150,60,200);\n"
                                             "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
                                             "    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
                                             "    border-bottom-color: rgba(200,70,20,200);\n"
                                             "    border-style: solid;\n"
                                             "    padding: 2px;\n"
                                             "    \n"
                                             "    background-color: rgb(129, 156, 169);\n"
                                             "    \n"
                                             "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/pic/delete (1).png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon2)
        self.pushButton_delete.setObjectName("pushButton_delete")
        # self.lineEdit_search = QtWidgets.QLineEdit(FaceDatabase)
        # self.lineEdit_search.setGeometry(QtCore.QRect(20, 42, 121, 30))
        # font = QtGui.QFont()
        # font.setFamily("等线")
        # font.setPointSize(10)
        # font.setBold(True)
        # font.setWeight(75)
        # self.lineEdit_search.setFont(font)
        # self.lineEdit_search.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        #                                    "border: 2px solid;\n"
        #                                    "border-color: rgb(69, 90, 100);\n"
        #                                    "border-radius:8px;")
        # self.lineEdit_search.setObjectName("lineEdit_search")

        self.retranslateUi_page5(FaceDatabase)
        QtCore.QMetaObject.connectSlotsByName(FaceDatabase)

    def retranslateUi_page5(self, FaceDatabase):
        _translate = QtCore.QCoreApplication.translate
        FaceDatabase.setWindowTitle(_translate("FaceDatabase", "Form"))
        # self.pushButton_search.setText(_translate("FaceDatabase", " 搜索"))
        # self.pushButton_modify.setText(_translate("FaceDatabase", " 修改"))
        item = self.tableWidget_db.horizontalHeaderItem(0)
        item.setText(_translate("FaceDatabase", "学号"))
        item = self.tableWidget_db.horizontalHeaderItem(1)
        item.setText(_translate("FaceDatabase", "姓名"))
        item = self.tableWidget_db.horizontalHeaderItem(2)
        item.setText(_translate("FaceDatabase", "人脸特征点"))
        item = self.tableWidget_db.horizontalHeaderItem(3)
        item.setText(_translate("FaceDatabase", "进入时间"))
        item = self.tableWidget_db.horizontalHeaderItem(4)
        item.setText(_translate("FaceDatabase", "人脸照片"))
        self.pushButton_delete.setText(_translate("FaceDatabase", " 删除"))
