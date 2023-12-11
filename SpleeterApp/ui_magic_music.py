# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 833)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.5, stop:0.3 rgba(46, 7, 89, 255), stop:1 rgba(131, 7, 95, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(191, 225, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 789, 719))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(4)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_16.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_16.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_3.addWidget(self.pushButton_16, 13, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_14.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_14.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_14.setSizeIncrement(QtCore.QSize(1, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_3.addWidget(self.pushButton_14, 13, 2, 1, 1)
        self.pushButton_output1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_output1.setObjectName("pushButton_output1")
        self.gridLayout_3.addWidget(self.pushButton_output1, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 5, 1, 1, 3)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_17.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_17.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_3.addWidget(self.pushButton_17, 13, 0, 1, 1)
        self.pushButton_play = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_play.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_play.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.pushButton_play.setFont(font)
        self.pushButton_play.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_play.setObjectName("pushButton_play")
        self.gridLayout_3.addWidget(self.pushButton_play, 8, 3, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_15.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_15.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_3.addWidget(self.pushButton_15, 13, 3, 1, 1)
        self.pushButton_input1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_input1.setObjectName("pushButton_input1")
        self.gridLayout_3.addWidget(self.pushButton_input1, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_12.setMinimumSize(QtCore.QSize(100, 130))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 170))
        self.label_12.setText("")
        self.label_12.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_12.setPixmap(QtGui.QPixmap("../../logo.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_10.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 12, 0, 1, 2)
        self.label_gif = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_gif.setMinimumSize(QtCore.QSize(280, 280))
        self.label_gif.setMaximumSize(QtCore.QSize(280, 280))
        self.label_gif.setText("")
        self.label_gif.setObjectName("label_gif")

        self.gif = QMovie("picture/music-9262_512.gif")
        self.label_gif.setMovie(self.gif)
        self.gif.stop()
        self.label_gif.setScaledContents(True)
        self.label_gif.setAlignment(QtCore.Qt.AlignCenter)


        self.gridLayout_3.addWidget(self.label_gif, 7, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 1, 1, 3)
        self.horizontalSlider = QtWidgets.QSlider(self.gridLayoutWidget_3)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_3.addWidget(self.horizontalSlider, 8, 1, 2, 2)
        self.label_time = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.label_time.setFont(font)
        self.label_time.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_time.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_time.setObjectName("label_time")
        self.gridLayout_3.addWidget(self.label_time, 8, 0, 1, 1)
        self.label_11.raise_()
        self.label_10.raise_()
        self.pushButton_input1.raise_()
        self.label_9.raise_()
        self.pushButton_17.raise_()
        self.pushButton_16.raise_()
        self.pushButton_14.raise_()
        self.pushButton_output1.raise_()
        self.pushButton_15.raise_()
        self.horizontalSlider.raise_()
        self.label_12.raise_()
        self.label_gif.raise_()
        self.pushButton_play.raise_()
        self.label_time.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 841, 721))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(4)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 9, 6, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 8, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_10.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_10.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 8, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 8, 5, 1, 1)
        self.label_gif_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_gif_2.setMinimumSize(QtCore.QSize(320, 320))
        self.label_gif_2.setMaximumSize(QtCore.QSize(320, 320))
        self.label_gif_2.setText("")
        self.label_gif_2.setObjectName("label_gif_2")

        self.gif2 = QMovie("picture/music-7683_512.gif")
        self.label_gif_2.setMovie(self.gif2)
        self.gif2.stop()
        self.label_gif_2.setScaledContents(True)
        self.label_gif_2.setAlignment(QtCore.Qt.AlignCenter)


        self.gridLayout_2.addWidget(self.label_gif_2, 6, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setMinimumSize(QtCore.QSize(100, 130))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 170))
        self.label_8.setText("")
        self.label_8.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_8.setPixmap(QtGui.QPixmap("../../logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 6)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 8, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 8, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 8, 2, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout_2.addWidget(self.horizontalSlider_2, 7, 2, 1, 3)
        self.pushButton_play_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_play_2.setMinimumSize(QtCore.QSize(70, 50))
        self.pushButton_play_2.setMaximumSize(QtCore.QSize(70, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.pushButton_play_2.setFont(font)
        self.pushButton_play_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_play_2.setObjectName("pushButton_play_2")
        self.gridLayout_2.addWidget(self.pushButton_play_2, 7, 5, 1, 1)
        self.label_time_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.label_time_2.setFont(font)
        self.label_time_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_time_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_time_2.setObjectName("label_time_2")
        self.gridLayout_2.addWidget(self.label_time_2, 7, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_16.setText(_translate("MainWindow", "drums"))
        self.pushButton_14.setText(_translate("MainWindow", "bass"))
        self.pushButton_output1.setText(_translate("MainWindow", "output"))
        self.label_11.setText(_translate("MainWindow", "C:/users"))
        self.pushButton_17.setText(_translate("MainWindow", "vocal"))
        self.pushButton_play.setText(_translate("MainWindow", "Play"))
        self.pushButton_play.setShortcut(_translate("MainWindow", "Space"))
        self.pushButton_15.setText(_translate("MainWindow", "piano"))
        self.pushButton_input1.setText(_translate("MainWindow", "input"))
        self.label_10.setText(_translate("MainWindow", "Choose a sound you like!"))
        self.label_9.setText(_translate("MainWindow", ".mp3"))
        self.label_time.setText(_translate("MainWindow", "0:00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Separator"))
        self.pushButton_12.setText(_translate("MainWindow", "input"))
        self.pushButton_10.setText(_translate("MainWindow", "Save"))
        self.label_5.setText(_translate("MainWindow", ".mp3/.mp3/.mp3"))
        self.pushButton_play_2.setText(_translate("MainWindow", "Play"))
        self.pushButton_play_2.setShortcut(_translate("MainWindow", "Space"))
        self.label_time_2.setText(_translate("MainWindow", "0:00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Combinator"))
