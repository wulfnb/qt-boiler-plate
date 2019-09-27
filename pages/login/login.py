import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

# from alpha import *

class loginPage(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(loginPage, self).__init__(*args, **kwargs)
        # self.setGeometry(50, 50, 1000, 600)
        # self.showMaximized()
        self.setWindowTitle("Loginpage - New")
        self.setWindowFlags(Qt.CustomizeWindowHint)
        # label = QLabel("This is a Login page")
        # label.setAlignment(Qt.AlignCenter)
        # self.setCentralWidget(label)
        # self.home = MainWindow(self)
        self.bind_home()
        # self.showFullScreen()


    def bind_home(self):

        # self.showFullScreen()
        button = QPushButton('X', self)
        button.clicked.connect(self.close_application)
        button.resize(20, 20)
        button.move(475, 5)
        button.setToolTip('Exit application')


        self.btn_go_home = QPushButton('Goto home', self)
        self.btn_go_home.move(360, 50)

        self.username_box = QLineEdit(self)
        self.username_box.move(20, 20)
        self.username_box.resize(280, 40)
        self.username_box.setPlaceholderText('Username')

        self.password_box = QLineEdit(self)
        self.password_box.move(20, 82)
        self.password_box.resize(280, 40)
        self.password_box.setPlaceholderText('Password')

        self.btn_login = QPushButton('Login', self)
        self.btn_login.clicked.connect(self.login_btn_click)
        self.btn_login.move(200, 130)


    def login_btn_click(self):
        username = self.username_box.text()
        password = self.password_box.text()
        if username and password and len(username)>6 and len(password)>6:
            print('Username and password is valid')

    def close_application(self):
        sys.exit()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_F11:
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()
