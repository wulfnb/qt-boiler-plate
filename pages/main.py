import sys
from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton, QMenu, QAction, QGridLayout
from PyQt5.QtCore import Qt

from PyQt5.QtCore import pyqtSlot


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # grid_layout = QGridLayout()
        # self.setLayout(grid_layout)

        self.setGeometry(50,50,500,300)
        self.setWindowTitle("My First App")

        self.initUI()
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

        self.btn_login = QPushButton('Go to login page', self)
        # self.btn_login.clicked.connect(self.goto_login_page)
        self.btn_login.resize(100, 70)
        self.btn_login.move(210, 70)
        self.btn_login.setToolTip('Go to login page')

    def initUI(self):

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)
        quit1 = QAction('Quit', self)
        quit1.setShortcut("Ctrl+Q")
        # self.quit1.clicked.connect(self.goto_login_page)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(quit1)
        fileMenu.triggered[QAction].connect(self.processtrigger)

    def processtrigger(self, q):
        if q.text() == 'Quit':
            sys.exit()
        else:
            print(q.text()+ " is triggered")




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

