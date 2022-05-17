import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QAction
from GUI.Stext import Ui_MainWindow

# main class Stext
class Main_window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        try:
            # todo Create protection for error understanding and stress tolerance
            self.headerbar = self.menubar
            self.headerbar.triggered[QAction].connect(self.menubarconnect)
        except Exception as Err:
            # todo Add pop-up windows in which you can conveniently observe the program error
            print(Err.__doc__)
            print(str(Err))

    def menubarconnect(self, Obj: Exception):
        print(Obj.objectName())
        # todo Handling top menu events

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main_window()
    window.show()
    app.exec_()