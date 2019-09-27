import sys
from PyQt5.QtWidgets import QApplication


from pages import MainWindow, loginPage


def changeWindow(w1, w2):
    w2.show()
    w1.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    login = loginPage()

    main.btn_login.clicked.connect(lambda: changeWindow(main, login))
    login.btn_go_home.clicked.connect(lambda: changeWindow(login, main))

    main.show()
    sys.exit(app.exec_())
