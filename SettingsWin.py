import sys
from PyQt5 import QtWidgets, QtCore
from GUI.Stext_Settings import Ui_MainWindow

# main class Stext
class Main_window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loop = QtCore.QEventLoop(self)

        try:
            pass
            # self.Apply_settings.clicked.connect(self.apply)
            # self.Reset_settings.clicked.connect(self.reset)
            # self.Close_settings.clicked.connect(self.close)
        except Exception as Err:
            print(Err.__doc__)
            print(str(Err))

    def apply(self):
        print("apply")
        self.loop.quit()

    def reset(self):
        print("reset")
        self.loop.quit()

    def close(self):
        print("close")
        self.loop.quit()

    def exec_(self):
        self.show()
        self._raise()
        res = self.loop.exec_()
        self.hide()
        return res


if __name__ == "__main__":
    print(sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    window = Main_window()
    window.show()
    app.exec_()