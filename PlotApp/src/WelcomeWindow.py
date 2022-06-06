
from PyQt5 import QtCore
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QPushButton, QDialog, QFileDialog, QLabel
from PyQt5.QtGui import QFont


class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.openedfile = ''
        self.ui()

    def ui(self):  # init ui for app
        self.resize(300, 300)  # set window config
        self.setWindowTitle('Plot App')
        font = QFont()  # set font config
        font.setPixelSize(17)
        self.setFont(font)

        self.buttonsInit()

        self.desc = QLabel('Plot dataframes app')  # descritpion config
        self.desc.setWordWrap(True)
        self.desc.setFont(QFont('Times', 20))
        self.desc.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.widget = QWidget()  # layout config
        self.grid = QGridLayout()
        self.widget.setLayout(self.grid)
        self.grid.addWidget(self.desc, 0, 0)
        self.grid.addWidget(self.chooiseFileButton, 1, 0)
        self.grid.addWidget(self.startPlot, 2, 0)
        self.setCentralWidget(self.widget)

    # init buttons
    def buttonsInit(self):
        self.chooiseFileButton = QPushButton('Chooise File')
        self.startPlot = QPushButton('Start Plot')
        self.startPlot.clicked.connect(self.nextwindow)
        self.chooiseFileButton.clicked.connect(self.chooiseFile)

    # methood to chooise file from folder. The default path is redirected to the project location
    def chooiseFile(self):
        filterList = []
        typeOfFiles = {
            'csvfile': 'CSV file (*.csv)',
            'pickleFile': 'Pickle files (*.pbz2)',
            'hdf5File': 'HDF5 files (*.hdf5)'

        }
        for types in typeOfFiles:
            if typeOfFiles.get(types):
                filterList.append(typeOfFiles[types])
        file = f'{QDir.currentPath()}'
        dialog = QFileDialog()
        dialog.setWindowTitle('File')
        dialog.setNameFilters(
            filterList)
        dialog.setDirectory(file)
        dialog.setFileMode(QFileDialog.ExistingFile)

        if dialog.exec_() == QDialog.Accepted:
            self.openedfile = dialog.selectedFiles()
        else:
            self.openedfile = None

    def nextwindow(self):
        print(f'{self.openedfile} \n{self.openedfile[0]}')
