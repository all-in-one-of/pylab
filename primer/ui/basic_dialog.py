from PySide2 import QtGui, QtCore, QtWidgets


"""
[Creating a dialog window using Qt module]
"""


dialog = QtWidgets.QDialog()
dialog.setWindowTitle('SimpleUI')
# dialog.setWindowFlags(Qt.WindowStaysOnTopHint)
dialog.setModal(False)
dialog.SetFixedHeight(200)
dialog.SetFixedWidth(300)

# dialog.SetMinimumHeight(200)
# dialog.SetMinimumWidth(300)
# 
# dialog.SetMaximumHeight(200)
# dialog.SetMaximumWidth(300)


dialog.show()