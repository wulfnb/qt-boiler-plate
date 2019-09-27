import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtCore import Qt

from PyQt5.QtCore import pyqtSlot

# Subclass QMainWindow to customise your application's main window


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setGeometry(50,50,500,300)
        self.setWindowTitle("My First App")

        label = QLabel("This is a PyQt5 window!")
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        self.home()


    def home(self):

        button = QPushButton('PyQt5 button', self)
        button.clicked.connect(self.close_application)
        # button.move(100, 70)
        button.move(100, 70)
        # sys.exit()
        # button.setToolTip('This is an example button')
        # print(dir(button.clicked.connect))


    @pyqtSlot()
    def close_application(self):
        print('PyQt5 button click')
        sys.exit()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
