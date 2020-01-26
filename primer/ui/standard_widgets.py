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
        example_lb.setText('Text')

        bold_font = QtGui.QFont()
        bold_font.setBold(True)
        example_lb.setFont(bold_font)

        example_le = QtWidgets.QLineEdit()
        example_le.setPlaceholderText('Enter something here...')

        reg_ex = QtCore.QRegExp('[a-zA-Z_')
        text_validator = QtGui.QRegExpValidator(reg_ex, example_le)
        example_le.setValidator(text_validator)

        self.example_te = QtWidgets.QTextEdit()
        self.example_te.setWordWrapMode(QtGui.QTextOption.WrapAtWordBoundaryOrAnywhere)

        text_layout.addWidget(example_lb)
        text_layout.addWidget(example_le)
        text_layout.addWidget(self.example_te)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(5)
        self.layout().addLayout(button_layout)

        example_btn = QtWidgets.QPushButton('Button')

        radio_a = QtWidgets.QRadioButton('a')
        radio_b = QtWidgets.QRadioButton('b')
        radio_c = QtWidgets.QRadioButton('c')
        radio_d = QtWidgets.QRadioButton('d')

        radio_a.setChecked(True)

        btn_grp_1 = QtWidgets.QButtonGroup(self)
        btn_grp_2 = QtWidgets.QButtonGroup(self)

        btn_grp_1.addButton(radio_a)
        btn_grp_1.addButton(radio_b)

        btn_grp_2.addButton(radio_c)
        btn_grp_2.addButton(radio_d)

        example_checkbox = QtWidgets.QCheckBox('Check')
        example_checkable = QtWidgets.QCheckBox('Not checkable')

        example_checkable.setCheckable(False)

        button_layout.addWidget(example_btn)
        button_layout.addWidget(radio_a)
        button_layout.addWidget(radio_b)
        button_layout.addWidget(radio_c)
        button_layout.addWidget(radio_d)
        button_layout.addWidget(example_checkbox)
        button_layout.addWidget(example_checkable)

        counter_layout = QtWidgets.QHBoxLayout()
        counter_layout.setSpacing(5)
        self.layout().addLayout(counter_layout)

        example_slider = QtWidgets.QSlider()
        example_slider.setOrientation(QtCore.Qt.Horizontal)
        example_slider.setRange(0, 10)

        example_spin = QtWidgets.QSpinBox()
        example_spin.setRange(0, 10)

        counter_layout.addWidget(example_slider)
        counter_layout.addWidget(example_spin)

        # self.connect(example_slider, QtCore.SIGNAL('valueChanged(int)'), example_spin.setValue)
        # self.connect(example_spin, QtCore.SIGNAL('valueChanged(int)'), example_slider.setValue)

        # Alternate method of connecting two widgets
        example_slider.valueChanged.connect(example_spin.setValue)
        example_spin.valueChanged.connect(example_slider.setValue)

        example_btn.clicked.connect(self.print_text)
        example_checkbox.stateChanged.connect(example_btn.setDisabled)

        btn_grp_1.buttonClicked.connect(self.add_to_text)

    def print_text(self):
        print(self.example_te.toPlainText())

    def add_to_text(self, button):
        button_text = button.text()
        self.example_te.setText(self.example_te.toPlainText() + button_text)


dialog = QtUi()
dialog.show()
