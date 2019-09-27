import sys
from PyQt5.QtWidgets import QApplication


from pages import MainWindow, loginPage


def changeWindow(w1, w2):
    w1.hide()
    w2.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    login = loginPage()

    main.button2.clicked.connect(lambda: changeWindow(main, login))
    login.button2.clicked.connect(lambda: changeWindow(login, main))

    main.show()
    sys.exit(app.exec_())
