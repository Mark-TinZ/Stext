import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QAction

from GUI.Stext import Ui_MainWindow as MainWin
from GUI.Stext_Settings import Ui_MainWindow as SettingWin
import pytesseract
#pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')
#pytesseract.run_and_get_output()
class Settings(QtWidgets.QMainWindow, SettingWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class ExampleApp(QtWidgets.QMainWindow, MainWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = None

        try:
            self.footerbar = self.statusbar
            self.headerbar = self.menubar
        except Exception:
            self.critical(Exception)


        try:
            self.footerbar.showMessage("test", 10000)
            self.headerbar.triggered[QAction].connect(self.menubarconect)
        except Exception:
            self.critical(Exception)

    def menubarconect(self, obj):
        print(obj.objectName())
        match obj.objectName():
            case "actionOpen":
                self.footerbar.showMessage("is clicked", 2000)
            case "actionSettings":
                self.openwin_settings()
            case "actionQuit":
                self.close()
            case "actionAbout_Stext":
                pass
            case "actionAbout_image_editor":
                pass
            case "actionabout_the_program":
                pass

    def openwin_settings(self):
        self.settings = Settings()
        self.settings.show()

    def critical(self, Error: IndexError):
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
