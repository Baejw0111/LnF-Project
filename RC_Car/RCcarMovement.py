#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
import mysql.connector
from threading import Timer
from time import sleep
from CheckText import isSame
import signal
import sys

import mysql.connector
import time
import atexit
# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)
pwm = PWM(0x6F)
pwm.setPWMFreq(60)
# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
myMotor = mh.getMotor(2)
pwm.setPWM(0,0,555)
# set the speed to start, from 0 (off) to 255 (max speed)
myMotor.setSpeed(150)


#pwm.setPWM(0,0,610)
# turn on motor
#myMotor.run(Raspi_MotorHAT.RELEASE);
myHost = '13.209.64.54'
myUser = 'ssafy'
myPassword ='ssafy1234'
myDB = 'minDB'

#속도 셋팅, 방향은 0,0,555로,  직진모드로
#현재위치를 저장한다. (x,y)
p = [0,0]
SearchPoint = [(0, 44), (0, 88), (44, 132)];
unit = 44 #속도 150, 1초간 갈 수 있는 거리
stopPoint = 0 #목표 사물함을 찾으면 인덱스를 저장한다.
mode = True #세로모드 or 가로모드
#텍스트인식 함수 추가
db = mysql.connector.connect(host = myHost, user = myUser, password = myPassword, database = myDB)
cur = db.cursor()
timer = None

def closeDB(signal, frame):
    print("BYE.")
    cur.close()
    db.close()
    timer.cancel()
    sys.exit(0)










#시작좌표는 0,0으로 한다.
#차량이 정차할 위치는  사물함과 x축상으로 50cm정도 떨어져 있다.
#그리고 탐색시에 사물함 전방 50cm거리에서 텍스트를 인식하므로 이점 유의해 둔다.

#모든 사물함 앞에는 1번씩 정차한다. 차량이 정차할 위치좌표를 튜플로 표현하고 이 위치들을 배열로 저장한다. 단위는 cm이다.
#카메라는 차량의 왼쪽에 부탁되어 있으므로 차량은 탐색시에 항상 우회전한다.



#좌회전 함수 추가
def turnLeft() :
    for i in range(7):
        pwm.setPWM(0, 0, 470)
        myMotor.run(Raspi_MotorHAT.BACKWARD);
        time.sleep(0.5)
        pwm.setPWM(0, 0, 610)
        myMotor.run(Raspi_MotorHAT.FORWARD);
        time.sleep(0.5)
    pwm.setPWM(0,0,555)

#우회전 함수 추가
def turnRight() :
    for i in range(7):
        pwm.setPWM(0, 0, 610)
        myMotor.run(Raspi_MotorHAT.BACKWARD);
        time.sleep(0.5)
        pwm.setPWM(0, 0, 470)
        myMotor.run(Raspi_MotorHAT.FORWARD);
        time.sleep(0.5)
    pwm.setPWM(0,0,555)

#물건 가져오기 함수 추가
def bring():
    print("bring!")
    turnLeft()
    time.sleep(3) #3초간 대기
    myMotor.run(Raspi_MotorHAT.FORWARD)
    time.sleep(1) #1 초 만큼 전진
    myMotor.run(Raspi_MotorHAT.RELEASE)
    time.sleep(3) #3초간 대기
    myMotor.run(Raspi_MotorHAT.BACKWARD)
    time.sleep(0.6) #0.4초 만큼 후진
    myMotor.run(Raspi_MotorHAT.RELEASE)
    time.sleep(5)
    myMotor.run(Raspi_MotorHAT.BACKWARD)
    time.sleep(0.4) #0.6초 만큼 후진
    turnRight()

def absdis(a,b) :
    if a>b:
        return a-b
    else :
        return b-a

#동작시작
def Search(a,b,c,d) :
    global mode, stopPoint
    for i in range(len(SearchPoint)):
        print(i)
        if mode :
            if SearchPoint[i][0] == p[0] :
                print("vert forward")
                myMotor.run(Raspi_MotorHAT.BACKWARD);
                time.sleep(absdis(SearchPoint[i][1],p[1])/44)
                # (absdis(SearchPoint[i][1],p[1]))/44 초 동안 전진
        
            else :
                print("vert turn right")
                myMotor.run(Raspi_MotorHAT.BACKWARD);
                time.sleep(absdis(SearchPoint[i][1],p[1])/44)
                # (absdis(SearchPoint[i][1],p[1]))/44 초 동안 전진
                turnRight()
                # 우회전
                myMotor.run(Raspi_MotorHAT.BACKWARD);
                time.sleep(absdis(SearchPoint[i][0], p[0]) / 44)
                # (absdis(SearchPoint[i][0],p[0]))/44 초 동안 전진
                mode = False
        else :
            if SearchPoint[i][1] == p[1] :
                print("hori forward")
                myMotor.run(Raspi_MotorHAT.BACKWARD);
                time.sleep(absdis(SearchPoint[i][0], p[0]) / 44)
                # (absdis(SearchPoint[i][0],p[0]))/44 초 동안 전진
        
            else :
                print("hori turn right")
                myMotor.run(Raspi_MotorHAT.BACKWARD);
                time.sleep(absdis(SearchPoint[i][0], p[1]) / 44)
                # (absdis(SearchPoint[i][0],p[0]))/44 초 동안 전진

                turnRight()
                # 우회전

                myMotor.run(Raspi_MotorHAT.BACKWARD);
                time.sleep(absdis(SearchPoint[i][1], p[1]) / 44)
                # (absdis(SearchPoint[i][1],p[1]))/44 초 동안 전진
                mode = True

        p[0] = SearchPoint[i][0]
        p[1] = SearchPoint[i][1] #현재 위치 갱신

        myMotor.run(Raspi_MotorHAT.RELEASE)
        print("take photo")
        if isSame(a,b,c,d) :
            stopPoint = i
            bring()
            break
        else : continue

    #돌아오기 구현
    #이제 후진방향으로 세팅
    stopPoint = len(SearchPoint) - 1
    for i in range(stopPoint-1,-1,-1):
        if mode :
            if SearchPoint[i][0] == p[0] :
                print("vert back")
                myMotor.run(Raspi_MotorHAT.FORWARD);
                time.sleep(absdis(SearchPoint[i][1], p[1]) / 44)
                 # (absdis(SearchPoint[i][1],p[1]))/44 초 동안 후진

            else :
                print("vert turn left")
                myMotor.run(Raspi_MotorHAT.FORWARD);
                time.sleep(absdis(SearchPoint[i][1], p[1]) / 44)
                # (absdis(SearchPoint[i][1],p[1]))/44 초 동안 후진

                turnLeft()
                # 좌회전

                myMotor.run(Raspi_MotorHAT.FORWARD);
                time.sleep(absdis(SearchPoint[i][0], p[0]) / 44)
                # (absdis(SearchPoint[i][0],p[0]))/44 초 동안 후진
                mode = False
        else :
            if SearchPoint[i][1] == p[1] :
                print("hori back")
                myMotor.run(Raspi_MotorHAT.FORWARD);
                time.sleep(absdis(SearchPoint[i][0], p[0]) / 44)
                # (absdis(SearchPoint[i][0],p[0]))/44 초 동안 후진

            else :
                print("hori turn left")
                myMotor.run(Raspi_MotorHAT.FORWARD);
                time.sleep(absdis(SearchPoint[i][0], p[0]) / 44)
                # (absdis(SearchPoint[i][0],p[0]))/44 초 동안 후진

                turnLeft()
                # 좌회전

                myMotor.run(Raspi_MotorHAT.FORWARD);
                time.sleep(absdis(SearchPoint[i][1], p[1]) / 44)
                # (absdis(SearchPoint[i][1],p[1]))/44 초 동안 후진
                mode = True

        p[0] = SearchPoint[i][0]
        p[1] = SearchPoint[i][1] #현재 위치 갱신
        
        myMotor.run(Raspi_MotorHAT.RELEASE)
    #SeachPoint의 첫번째 위치에서 다시 0,0으로 와야한다.
    
    print("go back")
    if mode :
        myMotor.run(Raspi_MotorHAT.FORWARD);
        time.sleep(absdis(SearchPoint[i][1], p[1]) / 44)
        #(absdis(SearchPoint[i][1],p[1]))/44 초 동안 후진
    else :
        myMotor.run(Raspi_MotorHAT.FORWARD);
        time.sleep(absdis(SearchPoint[i][0], p[0]) / 44)
        # (absdis(SearchPoint[i][0],p[0]))/44 초 동안 후진

    myMotor.run(Raspi_MotorHAT.RELEASE)
    
    turnLeft()
    turnLeft()
    myMotor.run(Raspi_MotorHAT.RELEASE)
    #좌회전 2번해서 180도 회전한다.

#while문을 계속 돌면서 DB에 명령어가 추가되는지 확인하고, 추가되었으면 바로 bring함수 호출


def polling():
    global cur, db

    cur.execute("select * from COMMAND order by time desc limit 1")
    for (id, date, time, name, place, is_done) in cur: 
        #print("분실날짜 : {}, 분실품 : {}, 분실장소 : {}".format(time, name, place))
        f_date = str(date)
        f_time = str(time)
        f_name = str(name)
        f_place = str(place)
        now_id = id
        if is_done ==1 : break
        Search(f_date,f_time,f_name,f_place)
        cur.execute("update COMMAND set is_done=1 where id={}".format(now_id))

    db.commit()
    global timer
    timer = Timer(2, polling)
    timer.start()

# init

signal.signal(signal.SIGINT, closeDB)
polling()







# main Thread
while True:
    pass
