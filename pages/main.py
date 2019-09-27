import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtCore import Qt

from PyQt5.QtCore import pyqtSlot

# from pages import loginPage

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setGeometry(50,50,500,300)
        self.setWindowTitle("My First App")

        # widgets. See: http://doc.qt.io/qt-5/qt.html

        # self.login = loginPage(self)

        self.home()


    def home(self):
        label = QLabel("This is a PyQt5 window!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        button = QPushButton('Quit', self)
        button.clicked.connect(self.close_application)
        button.resize(100, 70)
        button.move(100, 70)
        button.setToolTip('This is quit button')

        self.button2 = QPushButton('Go to login page', self)
        # self.button2.clicked.connect(self.goto_login_page)
        self.button2.resize(100, 70)
        self.button2.move(210, 70)
        self.button2.setToolTip('Go to login page')



    @pyqtSlot()
    def close_application(self):
        print('PyQt5 button click')
        sys.exit()

    # def goto_login_page(self):
    #     # self.login.show()
    #     # window.hide()
    #     changeWindow(main,login)


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec_()

# def changeWindow(w1, w2):
#     w1.hide()
#     w2.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main = MainWindow()
#     login = loginPage()

#     main.button2.clicked.connect(lambda: changeWindow(main, login))
#     login.button2.clicked.connect(
#         lambda: changeWindow(login, main))

#     main.show()
#     sys.exit(app.exec_())
