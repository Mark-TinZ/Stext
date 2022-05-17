import sys
from PyQt5 import QtWidgets

from MainWin import Main_window as Stext
from SettingsWin import Main_window as Settings
from ImageEditorWin import Main_window as Editor

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Stext()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
