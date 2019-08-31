
"""
[Creating a dialog window using Qt module]
"""


import Qt
dialog = Qt.QtWidgets.QDialog()
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