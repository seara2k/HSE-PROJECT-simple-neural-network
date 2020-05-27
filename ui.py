# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path("Dawnbringer.jpg")
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(659, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Logo),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget{\n"
                           "    background-color:;\n"
                           "}")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.pushButton1.setStyleSheet("QPushButton{\n"
                                       "    background-color:white;\n"
                                       "}\n"
                                       "QPushButton:checked{\n"
                                       "    background-color:black;\n"
                                       "}")
        self.pushButton1.setText("")
        self.pushButton1.setCheckable(True)
        self.pushButton1.setAutoExclusive(False)
        self.pushButton1.setAutoDefault(False)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(60, 20, 41, 41))
        self.pushButton2.setStyleSheet("QPushButton{\n"
                                       "    background-color:white;\n"
                                       "}\n"
                                       "QPushButton:checked{\n"
                                       "    background-color:black;\n"
                                       "}")
        self.pushButton2.setText("")
        self.pushButton2.setCheckable(True)
        self.pushButton2.setAutoExclusive(False)
        self.pushButton2.setAutoDefault(False)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(Form)
        self.pushButton3.setGeometry(QtCore.QRect(100, 20, 41, 41))
        self.pushButton3.setStyleSheet("QPushButton{\n"
                                       "    background-color:white;\n"
                                       "}\n"
                                       "QPushButton:checked{\n"
                                       "    background-color:black;\n"
                                       "}")
        self.pushButton3.setText("")
        self.pushButton3.setCheckable(True)
        self.pushButton3.setAutoExclusive(False)
        self.pushButton3.setAutoDefault(False)
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton4 = QtWidgets.QPushButton(Form)
        self.pushButton4.setGeometry(QtCore.QRect(20, 60, 41, 41))
        self.pushButton4.setStyleSheet("QPushButton{\n"
                                       "    background-color:white;\n"
                                       "}\n"
                                       "QPushButton:checked{\n"
                                       "    background-color:black;\n"
                                       "}")
        self.pushButton4.setText("")
        self.pushButton4.setCheckable(True)
        self.pushButton4.setAutoExclusive(False)
        self.pushButton4.setAutoDefault(False)
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton5 = QtWidgets.QPushButton(Form)
        self.pushButton5.setGeometry(QtCore.QRect(60, 60, 41, 41))
        self.pushButton5.setStyleSheet("QPushButton{\n"
                                       "    background-color:white;\n"
                                       "}\n"
                                       "QPushButton:checked{\n"
                                       "    background-color:black;\n"
                                       "}")
        self.pushButton5.setText("")
        self.pushButton5.setCheckable(True)
        self.pushButton5.setAutoExclusive(False)
        self.pushButton5.setAutoDefault(False)
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton6 = QtWidgets.QPushButton(Form)
        self.pushButton6.setGeometry(QtCore.QRect(100, 60, 41, 41))
        self.pushButton6.setStyleSheet("QPushButton{\n"
                                       "    background-color:white;\n"
                                       "}\n"
                                       "QPushButton:checked{\n"
                                       "    background-color:black;\n"
                                       "}")
        self.pushButton6.setText("")
        self.pushButton6.setCheckable(True)
        self.pushButton6.setAutoExclusive(False)
        self.pushButton6.setAutoDefault(False)
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton7 = QtWidgets.QPushButton(Form)
        self.pushButton7.setGeometry(QtCore.QRect(20, 100, 41, 41))
        self.pushButton7.setStyleSheet("QPushButton{\n"
                                       "    background-color:white;\n"
                                       "}\n"
                                       "QPushButton:checked{\n"
                                       "    background-color:black;\n"
                                       "}")
        self.pushButton7.setText("")
        self.pushButton7.setCheckable(True)
        self.pushButton7.setAutoExclusive(False)
        self.pushButton7.setAutoDefault(False)
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton8 = QtWidgets.QPushButton(Form)
        self.pushButton8.setGeometry(QtCore.QRect(60, 100, 41, 41))
        self.pushButton8.setStyleSheet("QPushButton{\n"
                                       "    background-color:white;\n"
                                       "}\n"
                                       "QPushButton:checked{\n"
                                       "    background-color:black;\n"
                                       "}")
        self.pushButton8.setText("")
        self.pushButton8.setCheckable(True)
        self.pushButton8.setAutoExclusive(False)
        self.pushButton8.setAutoDefault(False)
        self.pushButton8.setObjectName("pushButton8")
        self.pushButton9 = QtWidgets.QPushButton(Form)
        self.pushButton9.setGeometry(QtCore.QRect(100, 100, 41, 41))
        self.pushButton9.setStyleSheet("QPushButton{\n"
                                       "    background-color:white;\n"
                                       "}\n"
                                       "QPushButton:checked{\n"
                                       "    background-color:black;\n"
                                       "}")
        self.pushButton9.setText("")
        self.pushButton9.setCheckable(True)
        self.pushButton9.setAutoExclusive(False)
        self.pushButton9.setAutoDefault(False)
        self.pushButton9.setObjectName("pushButton9")
        self.pushButton10 = QtWidgets.QPushButton(Form)
        self.pushButton10.setGeometry(QtCore.QRect(20, 140, 41, 41))
        self.pushButton10.setStyleSheet("QPushButton{\n"
                                        "    background-color:white;\n"
                                        "}\n"
                                        "QPushButton:checked{\n"
                                        "    background-color:black;\n"
                                        "}")
        self.pushButton10.setText("")
        self.pushButton10.setCheckable(True)
        self.pushButton10.setAutoExclusive(False)
        self.pushButton10.setAutoDefault(False)
        self.pushButton10.setObjectName("pushButton10")
        self.pushButton11 = QtWidgets.QPushButton(Form)
        self.pushButton11.setGeometry(QtCore.QRect(60, 140, 41, 41))
        self.pushButton11.setStyleSheet("QPushButton{\n"
                                        "    background-color:white;\n"
                                        "}\n"
                                        "QPushButton:checked{\n"
                                        "    background-color:black;\n"
                                        "}")
        self.pushButton11.setText("")
        self.pushButton11.setCheckable(True)
        self.pushButton11.setAutoExclusive(False)
        self.pushButton11.setAutoDefault(False)
        self.pushButton11.setObjectName("pushButton11")
        self.pushButton12 = QtWidgets.QPushButton(Form)
        self.pushButton12.setGeometry(QtCore.QRect(100, 140, 41, 41))
        self.pushButton12.setStyleSheet("QPushButton{\n"
                                        "    background-color:white;\n"
                                        "}\n"
                                        "QPushButton:checked{\n"
                                        "    background-color:black;\n"
                                        "}")
        self.pushButton12.setText("")
        self.pushButton12.setCheckable(True)
        self.pushButton12.setAutoExclusive(False)
        self.pushButton12.setAutoDefault(False)
        self.pushButton12.setObjectName("pushButton12")
        self.pushButton13 = QtWidgets.QPushButton(Form)
        self.pushButton13.setGeometry(QtCore.QRect(20, 180, 41, 41))
        self.pushButton13.setStyleSheet("QPushButton{\n"
                                        "    background-color:white;\n"
                                        "}\n"
                                        "QPushButton:checked{\n"
                                        "    background-color:black;\n"
                                        "}")
        self.pushButton13.setText("")
        self.pushButton13.setCheckable(True)
        self.pushButton13.setAutoExclusive(False)
        self.pushButton13.setAutoDefault(False)
        self.pushButton13.setObjectName("pushButton13")
        self.pushButton14 = QtWidgets.QPushButton(Form)
        self.pushButton14.setGeometry(QtCore.QRect(60, 180, 41, 41))
        self.pushButton14.setStyleSheet("QPushButton{\n"
                                        "    background-color:white;\n"
                                        "}\n"
                                        "QPushButton:checked{\n"
                                        "    background-color:black;\n"
                                        "}")
        self.pushButton14.setText("")
        self.pushButton14.setCheckable(True)
        self.pushButton14.setAutoExclusive(False)
        self.pushButton14.setAutoDefault(False)
        self.pushButton14.setObjectName("pushButton14")
        self.pushButton15 = QtWidgets.QPushButton(Form)
        self.pushButton15.setGeometry(QtCore.QRect(100, 180, 41, 41))
        self.pushButton15.setStyleSheet("QPushButton{\n"
                                        "    background-color:white;\n"
                                        "}\n"
                                        "QPushButton:checked{\n"
                                        "    background-color:black;\n"
                                        "}")
        self.pushButton15.setText("")
        self.pushButton15.setCheckable(True)
        self.pushButton15.setAutoExclusive(False)
        self.pushButton15.setAutoDefault(False)
        self.pushButton15.setObjectName("pushButton15")
        self.goButton = QtWidgets.QPushButton(Form)
        self.goButton.setGeometry(QtCore.QRect(250, 450, 91, 51))
        self.goButton.setObjectName("goButton")
        self.labelresult = QtWidgets.QLabel(Form)
        self.labelresult.setGeometry(QtCore.QRect(150, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.labelresult.setFont(font)
        self.labelresult.setObjectName("labelresult")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 230, 121, 171))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 410, 631, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.clearButton = QtWidgets.QPushButton(Form)
        self.clearButton.setGeometry(QtCore.QRect(450, 450, 93, 51))
        self.clearButton.setObjectName("clearButton")
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(550, 450, 93, 51))
        self.exitButton.setObjectName("exitButton")
        self.teachButton = QtWidgets.QPushButton(Form)
        self.teachButton.setGeometry(QtCore.QRect(350, 450, 93, 51))
        self.teachButton.setObjectName("teachButton")
        self.console = QtWidgets.QTextEdit(Form)
        self.console.setGeometry(QtCore.QRect(150, 50, 461, 341))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.console.setFont(font)
        self.console.setAcceptDrops(True)
        self.console.setReadOnly(True)
        self.console.setObjectName("console")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "seara2k neural network"))
        self.goButton.setText(_translate("Form", "Go"))
        self.labelresult.setText(_translate("Form", "000000000000000"))
        self.clearButton.setText(_translate("Form", "Clear"))
        self.exitButton.setText(_translate("Form", "Exit"))
        self.teachButton.setText(_translate("Form", "Teach!"))
