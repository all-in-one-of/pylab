from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    # win.setGeometry(xpos, ypos, width, height)
    win.setGeometry(200, 200, 300, 300)
    win.setTWindowTitle("Tech Tittle")

    label = QtWidgets.QLabel(win)
    label.setText('my awesome label')
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())

    # pyuic5 -x ui_file -o export.py

window()