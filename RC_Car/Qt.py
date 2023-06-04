#!/usr/bin/python
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from developerMode import Ui_MainWindow
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
import cv2
import time
import atexit

mh = Raspi_MotorHAT(addr = 0x6f)
velocity = 150
direc = 555
def turnOffMotors() :
    mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)
myMotor = mh.getMotor(2)
myMotor.setSpeed(velocity)
pwm = PWM(0x6F)
pwm.setPWMFreq(60)
pwm.setPWM(0,0,direc)

class MyApp(QMainWindow, Ui_MainWindow) :
    global velocity, direc, myMotor, pwm
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        self.ui.vn.display(velocity)
        self.ui.dirn.display(direc)
        pass
    def takep(self):
        cap = cv2.VideoCapture(0)
        cap.set(3,480)
        cap.set(4,320)
        ret, frame = cap.read()
        cv2.imwrite('pika.png',frame)
        cap.release()
        self.img = cv2.imread('pika.png')
        self.printImage(self.img, self.ui.picture_2)
    def printImage(self, imgBGR, pic):
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte*w, QImage.Format_RGB888)
        pic.setPixmap(QPixmap(img))


    def forward(self):
        myMotor.setSpeed(150)
        myMotor.run(Raspi_MotorHAT.BACKWARD)
        time.sleep(1)

    def back(self):
        myMotor.setSpeed(150)
        myMotor.run(Raspi_MotorHAT.FORWARD)
        time.sleep(1)

    def left(self):
        pwm.setPWM(0,0,470)
    def right(self):
        pwm.setPWM(0,0,610)
    def stop(self):
        myMotor.run(Raspi_MotorHAT.RELEASE)
    def mid(self):
        pwm.setPWM(0, 0, 555)
app = QApplication()
win = MyApp()
win.show()
app.exec_()
