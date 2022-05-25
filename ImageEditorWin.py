import sys
from PyQt5 import QtWidgets
from GUI.Stext_Image_editor import Ui_MainWindow

# main class Stext
class Main_window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main_window()
    window.show()
    app.exec_()