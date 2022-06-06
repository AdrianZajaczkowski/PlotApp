from PyQt5.QtWidgets import QApplication
import sys
from WelcomeWindow import WelcomeWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()               # wyświetlenie głównego okna ustawień
    sys.exit(app.exec_())
