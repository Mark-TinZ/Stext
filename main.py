import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from GUI.Stext import Ui_MainWindow


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def critical(self, Error):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Error')
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(Error.__doc__)
        msgBox.setStandardButtons(QMessageBox.Close)
        msgBox.setDefaultButton(QMessageBox.Close)
        msgBox.setDetailedText(str(Error))
        reply = msgBox.exec()

        if reply == QMessageBox.Close:
            quit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
