from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox, QWidget, QFileDialog
import sys
import requests
import re

class MAINWINDOW(object):
    def denglu(self, MainWindow):
        MainWindow.setWindowTitle('登陆设计签名')
        MainWindow.resize(400, 400)
        MainWindow.move(800, 300)
        MainWindow.setWindowIcon(QtGui.QIcon('Imgs/title.jpg'))
        background_img = QtGui.QPalette()
        background_img.setBrush(MainWindow.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('Imgs/normal.jpg').scaled(669, 450)))
        MainWindow.setPalette(background_img)
        self.centralwidget = MainWindow
        self.centralwidget.setObjectName("centralwidget")

        # 欢迎使用标签
        self.label = QtWidgets.QLabel('欢迎登陆设计签名', self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPixelSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.resize(250, 50)
        self.label.move(80, 30)

        # 账号标签
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPixelSize(22)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setText('账 号：')
        self.label1.resize(150, 50)
        self.label1.move(150, 150)

        # # 账号输入框
        # self.textbox1 = QtWidgets.QLineEdit(self.centralwidget)
        # font = QtGui.QFont('楷体')
        # font.setPixelSize(20)
        # font.setBold(True)
        # self.textbox1.setFont(font)
        # self.textbox1.resize(150, 30)
        # self.textbox1.move(230, 160)

        # 设置账号只能输入数字
        self.textbox3 = Qt.QDoubleValidator(self.centralwidget)
        # self.textbox3 = Qt.QIntValidator(self.centralwidget)
        # self.textbox3.setRange(1, 2)
        self.textbox1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPixelSize(20)
        font.setBold(True)
        self.textbox1.setFont(font)
        self.textbox1.resize(150, 30)
        self.textbox1.move(230, 160)
        self.textbox1.setValidator(self.textbox3)

        # 密码标签
        self.label2 = QtWidgets.QLabel('密 码：', self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPixelSize(22)
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.resize(150, 50)
        self.label2.move(150, 220)

        # 密码输入框
        self.textbox2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPixelSize(20)
        font.setBold(True)
        self.textbox2.setFont(font)
        self.textbox2.resize(150, 30)
        self.textbox2.move(230, 230)
        # 设置密码不可见
        self.textbox2.setEchoMode(2)
        # 回车登录
        self.textbox2.returnPressed.connect(self.Click_denglu)

        # 登陆按键
        self.button1 = QtWidgets.QPushButton('登 陆', self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPixelSize(26)
        font.setBold(True)
        self.button1.setFont(font)
        self.button1.resize(100, 50)
        self.button1.move(230, 300)
        self.button1.clicked.connect(self.Click_denglu)

    def Click_denglu(self):
        # print('登陆成功！')
        user_name = QtWidgets.QLineEdit.text(self.textbox1)
        user_password = QtWidgets.QLineEdit.text(self.textbox2)
        if user_name == '1' and user_password == '1':
            self.tiaozhuan()
        elif user_name == "":
            self.msg_box = QMessageBox(QMessageBox.Warning, '警告', '账号不能为空！')
            self.msg_box.exec_()
        elif user_password == "":
            self.msg_box = QMessageBox(QMessageBox.Warning, '警告', '密码不能为空！')
            self.msg_box.exec_()
        else:
            self.msg_box = QMessageBox(QMessageBox.Warning, '警告', '密码或用户名错误！')
            self.msg_box.exec_()

    def tiaozhuan(self):
        self.centralwidget.close()
        self.Windows = QMainWindow()
        self.Ui = MainWindow()
        self.Ui.qianming(self.Windows)
        self.Windows.show()

class MainWindow(object):
    def qianming(self, MainWindow):
        MainWindow.setWindowTitle('设计个性签名')
        MainWindow.setWindowIcon(QtGui.QIcon('Imgs/title.jpg'))
        background_img = QtGui.QPalette()
        background_img.setBrush(MainWindow.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('Imgs/login1.jpg').scaled(669, 700)))
        MainWindow.setPalette(background_img)
        MainWindow.resize(680, 600)
        MainWindow.move(620, 250)
        self.centralwidget = MainWindow
        self.centralwidget.setObjectName("centralwidget")

        # 设置标签  姓名
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 108, 87))
        self.label.setText('姓名：')
        self.label.setFont(Qt.QFont("宋体"))
        self.label.setStyleSheet("color: red;font-size: 30px;font-weight: bold")
        # label.setObjectName('姓名')

        # 设置输入框  姓名
        self.textbox = Qt.QLineEdit(self.centralwidget)
        font = Qt.QFont("楷体")
        font.setPixelSize(30)
        self.textbox.setFont(font)
        self.textbox.resize(150, 50)
        self.textbox.move(180, 30)

        # 设置标签   样式
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(100, 10, 150, 200))
        self.label1.setText('签名样式：')
        self.label1.setStyleSheet("color: red;font-size: 30px;font-style: '楷体';font-weight: bold")

        # 设置输入框  样式
        self.textbox1 = Qt.QComboBox(self.centralwidget)
        self.textbox1.resize(130, 50)
        self.textbox1.move(250, 85)
        # 设置输入框中字体
        font = Qt.QFont("楷体")
        font.setPixelSize(30)
        font.setBold(True)
        self.textbox1.setFont(font)
        self.list_name = ['艺术签', '连笔签', '商务签', '楷书签', '潇洒签', '草体签', '行书签', '个性签', '可爱签']
        self.textbox1.addItems(self.list_name)

        # 默认图片
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(60, 200, 535, 205))
        self.image = QtGui.QPixmap('Imgs/login.png').scaled(535, 205)
        self.label2.setPixmap(self.image)

        # 按键设置
        self.button = QPushButton(self.centralwidget)
        self.button.resize(144, 100)
        self.button.setText('设计签名')
        self.button.move(400, 35)
        self.button.setStyleSheet("background-color: orange;color: white;font-size: 25px;font-weight: bold")
        self.button.clicked.connect(self.click)

        # 显示获取到的图片
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(60, 200, 535, 205))

        # 保存图片按键
        self.button7 = QtWidgets.QPushButton('保存图片', self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPixelSize(20)
        font.setBold(True)
        self.button7.setFont(font)
        self.button7.resize(150, 50)
        self.button7.move(80, 450)
        self.button7.clicked.connect(self.WENJIAN_save)

        # 保存文件路径框
        self.label4 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPixelSize(14)
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.resize(250, 40)
        self.label4.move(350, 455)

        # 保存路径为： 标签
        self.label5 = QtWidgets.QLabel('保存路径为：', self.centralwidget)
        font = QtGui.QFont('楷体')
        font.setPixelSize(16)
        font.setBold(True)
        self.label5.setFont(font)
        self.label5.resize(100, 40)
        self.label5.move(250, 455)

        # 查看图片按键
        self.button8 = QtWidgets.QPushButton('查看图片', self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPixelSize(20)
        font.setBold(True)
        self.button8.setFont(font)
        self.button8.resize(150, 50)
        self.button8.move(80, 520)
        self.button8.clicked.connect(self.WENJIAN_open)

        # 退出登录按键
        self.button9 = QtWidgets.QPushButton('退出登陆', self.centralwidget)
        font = QtGui.QFont('方正舒体')
        font.setPixelSize(20)
        font.setBold(True)
        self.button9.setFont(font)
        self.button9.resize(150, 50)
        self.button9.move(450, 520)
        self.button9.clicked.connect(self.TUICHU_click)

    def TUICHU_click(self):
        tuichu = QMessageBox.question(self.centralwidget, '提示', '是否确定退出登陆？', QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)
        if tuichu == QMessageBox.Yes:
            self.centralwidget.close()
            self.windows2 = QMainWindow()
            self.UI2 = MAINWINDOW()
            self.UI2.denglu(self.windows2)
            self.windows2.show()

        # button1 = QPushButton(windows)
        # button1.resize(50, 50)
        # button1.setText('开始')
        # button1.move(200, 150)
        # button1.clicked.connect(Picture_xianshi)

        # label4 = QtWidgets.QLabel(windows)
        # label2.setGeometry(QtCore.QRect(60, 200, 682, 365))
        # label4.setPixmap(QtGui.QPixmap('123.jpg').scaled(535, 205))

    # def click_error(self):
    #     self.btn = Qt.QPushButton()
    # self.btn.setText("错误")
    # self.btn.clicked.connect(Qt.)

    # 设置按键
    def click(self):
        self.name = Qt.QLineEdit.text(self.textbox)
        self.style_name = Qt.QComboBox.currentText(self.textbox1)
        if self.name == "":
            self.msg_box = QMessageBox(QMessageBox.Warning, '警告', '您输入的内容为空！')
            self.msg_box.exec_()
        # elif eval(name) == 1:
        #     msg_box1 = QMessageBox(QMessageBox.Critical, '错误', '不能为数字!')
        #     msg_box1.exec_()
        else:
            # print('被点击了一下！')
            # print(name)
            # print(style_name)
            self.url_name()
    # 设计签名
    def url_name(self):
        self.url = 'http://www.uustv.com/'
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
        }
        self.style_data = {
            "艺术签": "1.ttf",
            "连笔签": "zql.ttf",
            "商务签": "8.ttf",
            "楷书签": "6.ttf",
            "潇洒签": "bzcs.ttf",
            "草体签": "lfc.ttf",
            "行书签": "2.ttf",
            "个性签": "3.ttf",
            "可爱签": "yqk.ttf",
        }
        self.data = {
            "word": self.name,
            "sizes": "60",
            "fonts": self.style_data[self.style_name],
            "fontcolor": "#000000"
        }
        self.response = requests.post(url=self.url, headers=self.header, data=self.data)
        self.response.encoding = 'utf8'
        # print(response.text)
        self.img_list = re.findall('<div class="tu">﻿<img src="(.*?)"/></div>', self.response.text)[0]
        # print((img_list))
        self.img_url = "http://www.uustv.com/" + self.img_list
        # print(img_url)
        # http://www.uustv.com/tmp/165180897555823.gif
        self.response1 = requests.get(url=self.img_url, headers=self.header)
        # print(response1.content)
        # time.sleep(2)
        with open('Imgs/normalsignatue.jpg', 'wb') as fp:
            fp.write(self.response1.content)
        # # 图片显示
        # # toolpush = Qt.QToolBox(windows)
        # # toolpush.resize(535, 205)
        # # toolpush.move(500, 500)
        # label3 = QtWidgets.QLabel(windows)
        # label3.setGeometry(QtCore.QRect(60, 200, 682, 365))

        # 显示获得的图片
        self.image1 = QtGui.QPixmap('Imgs/normalsignatue.jpg').scaled(535, 205)
        self.label3.setPixmap(self.image1)

    def WENJIAN_save(self):
        # 避免报错闪退
        try:
            # 可以自己更改文件保存路径
            file_path, type = QFileDialog.getSaveFileName(None, '文件保存', 'F:/个性签名', 'Image files(*.jpg)')
            with open(file_path, 'wb') as fp:
                fp.write(self.response1.content)
            # print(file_path)
            self.label4.setText(file_path)
        except:
            pass

    def WENJIAN_open(self):
        try:
            # 可以自己更改文件打开路径
            file_path1, type = QFileDialog.getOpenFileName(None, '文件查看', 'F:/个性签名', 'Image files(*.jpg)')
            # print(file_path1)
            # self.label10.setPixmap(QtGui.QPixmap(file_path1).scaled(535, 205))
            # with open(file_path1, 'rb') as fp:
            #     fp.read()

            # self.windows1 = QMainWindow()
            # self.UI1 = MainWindow1()
            # self.UI1.CHAKAN(self.windows1)
            # self.windows1.show()
        except:
            pass

        # label4.setGeometry(QtCore.QRect(60, 200, 682, 365))
        # # label4.resize(200,250)
        # label4.setScaledContents(True)

    # def Picture_xianshi():
    #     print('12')
    #     # label3 = QtWidgets.QLabel(windows)
    #     # label3.setGeometry(QtCore.QRect(60, 200, 682, 365))
    #     image1 = QtGui.QPixmap('login.png').scaled(535, 205)
    #     label3.setPixmap(image1)

    # def closeEvent(self, event, Qwidget):
    #     reply = QMessageBox.question(self.QWidget, "标题", "确认退出吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

# class Close_dialog(QWidget):
#     def closeEvent(self, event):
#         reply = QMessageBox.question(self.centralwidget, '信息', '你确定退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#         if reply == QMessageBox.Yes:
#             event.accept()
#             # self.centralwidget.close()
#         else:
#             event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = QMainWindow()
    ui = MAINWINDOW()
    ui.denglu(windows)
    windows.show()
    sys.exit(app.exec_())

