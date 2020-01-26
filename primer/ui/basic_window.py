from PySide2 import QtGui, QtCore, QtWidgets

"""
[Creating a window using Qt module]
"""

window = QtWidgets.QMainWindow()

# Menubars
menubar = QtWidgets.QMenuBar()
menubar.addAction('File')
menubar.addAction('Edit')
menubar.addSeparator
menubar.addAction('Modify')
menubar.addAction('Create')
menubar.addAction('Display')
window.setMenuBar(menubar)

# Toolbars
toolbar = QtWidgets.QToolBar()
toolbar.addAction('File')
toolbar.addAction('Edit')
toolbar.addSeparator
toolbar.addAction('Modify')
toolbar.addAction('Create')
toolbar.addAction('Display')
window.addToolBar(toolbar)

statusBar = QtWidgets.QStatusBar()
# Message followed by the duration
statusBar.showMessage('Loading...', 2000)
window.setStatusBar(statusBar)


window.show()