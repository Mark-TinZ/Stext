import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction

from MainWin import Main_window as Stext
from SettingsWin import Main_window as Settings
from ImageEditorWin import Main_window as Editor



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Stext()
    window.show()
    app.exec_()