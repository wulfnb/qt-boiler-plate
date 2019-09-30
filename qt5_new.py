import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('Main window')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        # Menubar content
        extractAction = QtWidgets.QAction("&Get to the chopper", self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.close_application)

        # Editor
        openEditor = QtWidgets.QAction('&Edotor', self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        # open file
        openFile = QtWidgets.QAction('&Open File', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open file')
        openFile.triggered.connect(self.open_file)

        # save file
        saveFile = QtWidgets.QAction('&Save File', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save file')
        saveFile.triggered.connect(self.save_file)


        self.statusBar()
        # Menubar
        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        # Edotor menu
        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)

        self.home()

    def home(self):
        btn = QtWidgets.QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 100)
        # Tool Bar
        extractAction = QtWidgets.QAction(QtGui.QIcon('icon.png'), 'Wow im here', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)
        
        #  Font menu
        fontChoice = QtWidgets.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)
        # for new toolbar uncoment next line
        # self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)

        #font colour
        color = QtGui.QColor(5, 3, 0)

        fontColor = QtWidgets.QAction('Font bg color', self)
        fontColor.triggered.connect(self.color_picker)
        self.toolBar.addAction(fontColor)


        # checkbox
        checkBox = QtWidgets.QCheckBox('Enlarge Window', self)
        checkBox.move(300, 25)
        checkBox.stateChanged.connect(self.enlarge_window)
        
        #Progress bar 
        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        #Progress bar action button
        self.btn = QtWidgets.QPushButton('Download',self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)

        # Style
        # print(self.style().objectName)
        self.styleChoice = QtWidgets.QLabel("Windows Vista", self)

        comboBox = QtWidgets.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")

        comboBox.move(50, 250)
        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)

        # Calender
        cal = QtWidgets.QCalendarWidget(self)
        cal.move(500, 200)
        cal.resize(200, 200)

        self.show()

    def save_file(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self,'Open File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()


    def open_file(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self,'Open File')
        file = open(name, 'r')

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)


    def editor(self):
        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)


    def color_picker(self):
        color = QtWidgets.QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget { background-color: %s}' % color.name())


    def font_choice(self):
        font, valid = QtWidgets.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)


    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))

    def download(self):
        self.completed = 0

        while self.completed <100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)


    def enlarge_window(self,state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)


    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self,'Extract', 'Exit the application', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()