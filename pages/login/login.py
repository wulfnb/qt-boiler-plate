from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtCore import Qt

# from alpha import *

class loginPage(QMainWindow):
    def __init__(self, *args, **kwargs):
        print(dir(*args))
        super(loginPage, self).__init__(*args, **kwargs)
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Loginpage - New")
        label = QLabel("This is a Login page")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        # self.home = MainWindow(self)
        self.bind_home()


    def bind_home(self):
        self.button2 = QPushButton('Goto home', self)
        self.button2.clicked.connect(self.goto_home)
        # button2.resize(100, 70)
        self.button2.move(210, 70)

    def goto_home(self):
        pass

