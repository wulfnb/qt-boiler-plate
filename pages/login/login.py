from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

# from alpha import *

class loginPage(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(loginPage, self).__init__(*args, **kwargs)
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Loginpage - New")
        # label = QLabel("This is a Login page")
        # label.setAlignment(Qt.AlignCenter)
        # self.setCentralWidget(label)
        # self.home = MainWindow(self)
        self.bind_home()


    def bind_home(self):
        self.btn_go_home = QPushButton('Goto home', self)
        self.btn_go_home.move(380, 0)

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
        print(self.username_box.text())
        print(self.password_box.text())

