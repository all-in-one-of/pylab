# 
#  UI creation for Maya
# 


from Qt import QtGui, QtCore, uic
from pymel.core import *
import pymel.core as pm
from pymel import *

# Path to desginer UI file
ui_filename = 'path/file.ui'
form_class, base_class = uic.loadUiType(ui_filename)


# Interface class
class interface(base_class, form_class):
    def __init__(self):
        super(base_class, self).__init__()
        self.setupUi(self)
        self.serObjectName('windowName')
        self.setDockNestingEnabled(True)
        # self.connectInterface()

#  Main
def main():
    global ui
    ui = interface()
    ui.show()

if __name__ == "__main__":
    main()