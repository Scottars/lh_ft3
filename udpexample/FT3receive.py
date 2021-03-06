#-*-coding:utf-8-*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from   PyQt5 import QtCore,sip
import sys,random

import numpy as np
from udpexample.udpserver import Ui_Dialog
import time
# import matplotlib,time
# matplotlib.use("Qt5Agg")  # 声明使用QT5
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
import socket
import copy
global flagthreadstop
flagthreadstop=False
global msg
msg=b'\x00\x03'
class WorkThread(QThread):
    trigger = pyqtSignal()

    def __int__(self):
        super(WorkThread, self).__init__()
    def run(self):
        #这一部分就可以写入你想要执行的代码就好
        # print('开始执行了run')
        # self.ip_port = ('192.168.0.3', 32768)
        #
        self.ip_port = ('127.0.0.1', 44233)
        BUFSIZE = 1024
        self.udp_server_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.udp_server_client.bind(self.ip_port)
        print('we have bind this ip')

        while True:
            if flagthreadstop:
                self.udp_server_client.close()
                break


            else:
                global msg
                print('BEFORE')
                msg, addr =self.udp_server_client.recvfrom(BUFSIZE)
                print("recv", msg, addr)
                # self.trigger.emit()



            # self.udp_server_client.sendto(msg.upper(), addr)#我们得到了这个socket 然后通过socket发送到原来接收得到的地址

                # 循环完毕后发出信号






import struct
class MainDialogImgBW(QDialog,Ui_Dialog):
    def __init__(self):
        super(MainDialogImgBW,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("FT3Data Receive")
        self.setMinimumSize(0,0)

        self.pushButton.clicked.connect(self.EquipmentCStopFunction)
        self.pushButton_2.clicked.connect(self.receivestop)

    def receivestart(self):
        global flagthreadstop
        flagthreadstop=False
        msgcopy=copy.deepcopy(msg)
        if len(msgcopy)<10:
            pass
        else:
            #模拟数字
            moni_shuzi=msgcopy[0]
            #通道号
            tongdaohao=msgcopy[1]
            #采样点数
            caiyangdian=struct.unpack('!h',msgcopy[2:4])
            #报文长度i
            baowenchangdu=msg[4]
            #超时表示
            chaoshi=msgcopy[5]
            #crc校验
            crcjiaoyan=struct.unpack('!h',msgcopy[6:8])
            #b包的序号
            baoxuhao=struct.unpack('!i',msgcopy[8:12])
            #启动一个线程tcp服务器线程
            print('触发了信号')
            # print(msg)

            if moni_shuzi== 0:   #数字量  数据格式为:缓冲数据的师表+帧头+数据
                self.textBrowser.setText(str(moni_shuzi))
                self.textBrowser_2.setText(str(tongdaohao))
                self.textBrowser_3.setText(str(caiyangdian[0]))
                self.textBrowser_4.setText(str(baowenchangdu))
                self.textBrowser_5.setText(str(chaoshi))
                self.textBrowser_6.setText(str(crcjiaoyan[0]))
                self.textBrowser_7.setText(str(baoxuhao[0]))
                print('we are receiving 数字量')

                dataall=''
                for i in range(caiyangdian[0]):  #总共有12个点

                    data= msgcopy[12+i*baowenchangdu:12+baowenchangdu*(i+1)]

                    time= str(hex(data[0]))+':'+str(hex(data[1]))+':'+str(hex(data[2]))+':'+str(hex(data[3]))+':'
                    # print(time)
                    zhentou=str(hex(data[4]))+':'+str(hex(data[5]))+'\n'
                    a=''
                    for i in (data[6:24]):
                        if i >16:
                            a = a + str(hex(i))[2:]+':'
                        else:
                            a = a + '0' + str(hex(i))[2:]+':'
                    a= a + '\n'
                    for i in (data[24:42]):
                        if i >16:
                            a = a + str(hex(i))[2:]+':'
                        else:
                            a = a + '0' + str(hex(i))[2:]+':'
                    a= a + '\n'
                    for i in (data[42:60]):

                        if i >16:
                            a = a + str(hex(i))[2:]+':'
                        else:
                            a = a + '0' + str(hex(i))[2:]+':'
                    a= a + '\n'
                    for i in (data[60:78]):
                        if i >16:
                            a = a + str(hex(i))[2:]+':'
                        else:
                            a = a + '0' + str(hex(i))[2:]+':'
                    a1=time+zhentou+a+'\n'
                    dataall = dataall + a1

                self.textBrowser_8.setText(dataall)


                pass
            elif moni_shuzi==1:   #GPIB  数据格式为:缓冲数据的师表+序号+数据 :这个时候没有帧头了
                self.textBrowser_14.setText(str(moni_shuzi))
                self.textBrowser_16.setText(str(tongdaohao))
                self.textBrowser_12.setText(str(caiyangdian[0]))
                self.textBrowser_15.setText(str(baowenchangdu))
                self.textBrowser_11.setText(str(chaoshi))
                self.textBrowser_13.setText(str(crcjiaoyan[0]))
                self.textBrowser_17.setText(str(baoxuhao[0]))
                print('we are receiving GPIB')

                dataall=''
                for i in range(caiyangdian[0]):  #总共有12个点
                    #数据:
                    data= msgcopy[12+i*baowenchangdu:12+baowenchangdu*(i+1)]
                    #时间标签
                    time= str(hex(data[0]))+':'+str(hex(data[1]))+':'+str(hex(data[2]))+':'+str(hex(data[3]))+':'
                    # print(time)
                    #4位的序号的长度+4个字节
                    xuhao=str(hex(data[4]))+':'+str(hex(data[5]))+':'+str(hex(data[6]))+':'+str(hex(data[7]))+'\n'

                    a=''
                    for i in (data[8:]):
                        if i >16:
                            a = a + str(hex(i))[2:]+':'
                        else:
                            a = a + '0' + str(hex(i))[2:]+':'
                    a= a + '\n'

                    a1=time+xuhao+a
                    dataall = dataall + a1
                self.textBrowser_9.setText(dataall)

            elif moni_shuzi == 2:
                self.textBrowser_19.setText(str(moni_shuzi))
                self.textBrowser_24.setText(str(tongdaohao))
                self.textBrowser_21.setText(str(caiyangdian[0]))
                self.textBrowser_22.setText(str(baowenchangdu))
                self.textBrowser_20.setText(str(chaoshi))
                self.textBrowser_23.setText(str(crcjiaoyan[0]))
                self.textBrowser_18.setText(str(baoxuhao[0]))
                dataall = ''
                print('we are receiving AD')
                for i in range(caiyangdian[0]): 

                    data= msgcopy[12+i*baowenchangdu:12+baowenchangdu*(i+1)]

                    time= str(hex(data[0]))+':'+str(hex(data[1]))+':'+str(hex(data[2]))+':'+str(hex(data[3]))+':'+'\n'
                    # print(time)
                    # zhentou=str(hex(data[4]))+':'+str(hex(data[5]))+'\n'
                    a=''
                    for i in (data[4:]):
                        if i >16:
                            a = a + str(hex(i))[2:]+':'
                        else:
                            a = a + '0' + str(hex(i))[2:]+':'
                    a= a + '\n'

                    a1=time+a
                    dataall = dataall + a1

                self.textBrowser_10.setText(dataall)

        pass


        pass
    def EquipmentCStopFunction(self):
        print('执行C物体停止功能开始')

        self.workThread=WorkThread()  #实例化一个线程对象
        # self.workThread.trigger.connect(self.receivestart)  #链接你执行完这个线程之后的想要触发的 函数的名字
        self.workThread.start()  #这个就是启动你的想要执行额线程，注意这个是start 而不是run

        self.timer = QTimer(self) #初始化一个定时器
        self.timer.timeout.connect(self.receivestart) #计时结束调用operate()方法
        self.timer.start(1) #设置计时间隔并启动  #单位是ms 为单位


        print('两个线程是否同步')
        # self.workThread1 = WorkThread()        #实例化一个线程对象
        # self.workThread1.trigger.connect(self.receivestop)#链接你执行完这个线程之后的想要触发的 函数的名字
        # self.workThread1.start()  #这个就是启动你的想要执行额线程，注意这个是start 而不是run
        # self.workThread.exit()

    #


    def receivestop(self):
        #启动一个线程tcp服务器线程
        print('we have trigger the receive stop')
        global flagthreadstop

        flagthreadstop=True
        self.timer.stop()

    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainDialogImgBW()
    main.show()
    #app.installEventFilter(main)
    sys.exit(app.exec_())
