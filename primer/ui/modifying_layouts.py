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
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.setFixedHeight(250)
        self.setMinimumWidth(300)

        # An example of setting a the margins/padding size in a vertical box layout
        # Parameters for setContentsMargins(Left, Up, Right, Bottom)
        #
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setContentsMargins(5, 5, 5, 5)
        self.layout().setSpacing(5)
        self.layout().setAlignment(QtCore.Qt.AlignTop)

        # An example of adding a raised frame
        top_frame = QtWidgets.QFrame()
        top_frame.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Raised)
        middle_frame = QtWidgets.QFrame()
        middle_frame.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Raised)
        btm_frame = QtWidgets.QFrame()
        btm_frame.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Raised)

        # self.layout().addWidget(top_frame)
        self.layout().addWidget(middle_frame)
        # self.layout().addWidget(btm_frame)

        middle_frame.setLayout(QtWidgets.QHBoxLayout())
        middle_frame.layout().setContentsMargins(0, 0, 0, 0)
        middle_frame.layout().setSpacing(0)
        middle_frame.layout().setAlignment(QtCore.Qt.AlignTop)

        middle_frame.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        btn_1 = QtWidgets.QPushButton('1')
        btn_2 = QtWidgets.QPushButton('2')
        btn_3 = QtWidgets.QPushButton('3')
        btn_4 = QtWidgets.QPushButton('4')
        btn_5 = QtWidgets.QPushButton('5')

        middle_frame.layout().addWidget(btn_1)
        middle_frame.layout().addWidget(btn_2)
        middle_frame.layout().addWidget(btn_3)
        middle_frame.layout().addWidget(btn_4)
        middle_frame.layout().addWidget(btn_5)


dialog = QtUi()
dialog.show()
