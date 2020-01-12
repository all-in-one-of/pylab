from PySide2 import QtGui, QtCore, QtWidgets
from functools import partial


class QtUi(QtWidgets.QDialog):
    """

    """

    def __init__(self):
        """

        """
        QtWidgets.QDialog.__init__(self)
        self.setWindowTitle('Simple QT UI')
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.setFixedHeight(250)
        self.setMinimumWidth(300)

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setContentsMargins(5, 5, 5, 5)
        self.layout().setSpacing(5)

        text_layout = QtWidgets.QHBoxLayout()
        text_layout.setSpacing(5)
        self.layout().addLayout(text_layout)

        example_lb = QtWidgets.QLabel('Title: ')
        example_lb.setText('Foo')

        bold_font = QtGui.QFont()
        bold_font.setBold(True)
        example_lb.setFont(bold_font)



        text_layout.addWidget(example_lb)

dialog = QtUi()
dialog.show()
