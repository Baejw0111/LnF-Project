# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'developerMode.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QLCDNumber, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(658, 603)
        font = QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.picture = QPushButton(self.centralwidget)
        self.picture.setObjectName(u"picture")
        self.picture.setGeometry(QRect(10, 400, 401, 161))
        self.vn = QLCDNumber(self.centralwidget)
        self.vn.setObjectName(u"vn")
        self.vn.setGeometry(QRect(420, 70, 231, 61))
        self.dirn = QLCDNumber(self.centralwidget)
        self.dirn.setObjectName(u"dirn")
        self.dirn.setGeometry(QRect(420, 190, 231, 61))
        self.velocity = QLabel(self.centralwidget)
        self.velocity.setObjectName(u"velocity")
        self.velocity.setGeometry(QRect(420, 10, 231, 51))
        self.velocity.setBaseSize(QSize(0, 0))
        self.velocity.setFont(font)
        self.direction = QLabel(self.centralwidget)
        self.direction.setObjectName(u"direction")
        self.direction.setGeometry(QRect(420, 140, 231, 51))
        self.direction.setFont(font)
        self.forward = QPushButton(self.centralwidget)
        self.forward.setObjectName(u"forward")
        self.forward.setGeometry(QRect(500, 360, 61, 61))
        font1 = QFont()
        font1.setPointSize(13)
        self.forward.setFont(font1)
        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(500, 500, 61, 61))
        self.back.setFont(font1)
        self.left = QPushButton(self.centralwidget)
        self.left.setObjectName(u"left")
        self.left.setGeometry(QRect(430, 430, 61, 61))
        self.left.setFont(font1)
        self.right = QPushButton(self.centralwidget)
        self.right.setObjectName(u"right")
        self.right.setGeometry(QRect(570, 430, 61, 61))
        self.right.setFont(font1)
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(420, 260, 231, 81))
        self.mid = QPushButton(self.centralwidget)
        self.mid.setObjectName(u"mid")
        self.mid.setGeometry(QRect(500, 430, 61, 61))
        self.mid.setFont(font1)
        self.picture_2 = QLabel(self.centralwidget)
        self.picture_2.setObjectName(u"picture_2")
        self.picture_2.setGeometry(QRect(17, 15, 391, 381))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.forward.clicked.connect(MainWindow.forward)
        self.left.clicked.connect(MainWindow.left)
        self.right.clicked.connect(MainWindow.right)
        self.back.clicked.connect(MainWindow.back)
        self.picture.clicked.connect(MainWindow.takep)
        self.stop.clicked.connect(MainWindow.stop)
        self.mid.clicked.connect(MainWindow.mid)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.picture.setText(QCoreApplication.translate("MainWindow", u"take picture", None))
        self.velocity.setText(QCoreApplication.translate("MainWindow", u"        velocity", None))
        self.direction.setText(QCoreApplication.translate("MainWindow", u"       direction", None))
        self.forward.setText(QCoreApplication.translate("MainWindow", u"forward", None))
        self.back.setText(QCoreApplication.translate("MainWindow", u"back", None))
        self.left.setText(QCoreApplication.translate("MainWindow", u"left", None))
        self.right.setText(QCoreApplication.translate("MainWindow", u"right", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.mid.setText(QCoreApplication.translate("MainWindow", u"mid", None))
        self.picture_2.setText("")
    # retranslateUi

