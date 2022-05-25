import sys
from PyQt5 import QtWidgets
from traceback import format_exc
from PyQt5.QtWidgets import QMessageBox, QAction, QFileDialog
from GUI.Stext import Ui_MainWindow as Stext
from SettingsWin import Main_window as Settings


# main class Stext
class Main_window(QtWidgets.QMainWindow, Stext):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        try:
            # TODO Create protection for error understanding and stress tolerance
            self.menubar.triggered[QAction].connect(self.menubarconnect)
            self.statusbar.showMessage("Ready!", 0)
        except Exception as Err:
            self.critical(Err)

    def critical(self, Error: IndexError):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Stext - " + Error.__doc__)
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(str(Error))
        msgBox.setStandardButtons(QMessageBox.Close)
        msgBox.setDefaultButton(QMessageBox.Close)
        msgBox.setDetailedText(format_exc())
        reply = msgBox.exec()

        if reply == QMessageBox.Close:
            quit()

    def showDialogSettings(self):
        settings = Settings()
        settings.show()

    def menubarconnect(self, Obj):
        print(Obj.objectName())
        # TODO Handling top menu events
        try:
            match Obj.objectName():
                case "actionOpen":
                    print(QFileDialog.getOpenFileName(self, "Select a photo", None, "Image (*.png *.jpg)"))
                case "actionSettings":
                    self.showDialogSettings()
                case "actionQuit":
                    exit()
        except Exception as Err:
            self.critical(Err)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main_window()
    window.show()
    app.exec_()