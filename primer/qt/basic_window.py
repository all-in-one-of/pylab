

"""
[Creating a window using Qt module]
"""

window = Qt.QtWidgets.QMainWindow()

# Menubars
menubar = Qt.QtWidgets.QMenuBar()
menubar.addAction('File')
menubar.addAction('Edit')
menubar.addSeparator
menubar.addAction('Modify')
menubar.addAction('Create')
menubar.addAction('Display')
window.setMenuBar(menubar)

# Toolbars
toolbar = Qt.QtWidgets.QToolBar()
toolbar.addAction('File')
toolbar.addAction('Edit')
toolbar.addSeparator
toolbar.addAction('Modify')
toolbar.addAction('Create')
toolbar.addAction('Display')
window.addToolBar(toolbar)

statusBar = Qt.QtWidgets.QStatusBar()
# Message followed by the duration
statusBar.showMessage('Loading...', 2000)
window.setStatusBar(statusBar)


window.show()