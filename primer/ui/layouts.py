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
        self.setMinimumHeight(250)
        self.setFixedWidth(300)

        # An example of setting a Vertical box layout
        # self.setLayout(QtWidgets.QVBoxLayout())
        #
        # btn_1 = QtWidgets.QPushButton('Button 1')
        # btn_2 = QtWidgets.QPushButton('Button 2')
        # btn_3 = QtWidgets.QPushButton('Button 3')
        #
        # self.layout().addWidget(btn_1)
        # self.layout().addWidget(btn_2)
        # self.layout().addWidget(btn_3)

        # An example of setting a horizontal box layout
        # self.setLayout(QtWidgets.QHBoxLayout())
        #
        # btn_1 = QtWidgets.QPushButton('Button 1')
        # btn_2 = QtWidgets.QPushButton('Button 2')
        # btn_3 = QtWidgets.QPushButton('Button 3')
        #
        # self.layout().addWidget(btn_1)
        # self.layout().addWidget(btn_2)
        # self.layout().addWidget(btn_3)

        # An example of setting a form layout
        # self.setLayout(QtWidgets.QFormLayout())
        #
        # name_le = QtWidgets.QLineEdit()
        # email_le = QtWidgets.QLineEdit()
        # age_sb = QtWidgets.QSpinBox()
        #
        # self.layout().addWidget(name_le)
        # self.layout().addWidget(email_le)
        # self.layout().addWidget(age_sb)
        #
        # self.layout().addRow('Name:', name_le)
        # self.layout().addRow('Email:', email_le)
        # self.layout().addRow('Age:', age_sb)

        # # An example of a grid layout
        # self.setLayout(QtWidgets.QGridLayout())
        #
        # font_name_lb = QtWidgets.QLabel('Font')
        # font_style_lb = QtWidgets.QLabel('Font Style')
        # font_size_lb = QtWidgets.QLabel('Size')
        #
        # font_names_list = QtWidgets.QListWidget()
        # font_names_list.addItem('Times')
        # font_names_list.addItem('Helvetica')
        # font_names_list.addItem('Courier')
        #
        # font_style_list = QtWidgets.QListWidget()
        # font_style_list.addItem('Roman')
        # font_style_list.addItem('Italic')
        # font_style_list.addItem('Oblique')
        #
        # font_size_list = QtWidgets.QListWidget()
        # for index in range(10, 30, 2):
        #     font_size_list.addItem(str(index))
        #
        # self.layout().addWidget(font_name_lb, 0, 0)
        # self.layout().addWidget(font_names_list, 1, 0)
        #
        # self.layout().addWidget(font_style_lb, 0, 1)
        # self.layout().addWidget(font_style_list, 1, 1)
        #
        # self.layout().addWidget(font_size_lb, 0, 2)
        # self.layout().addWidget(font_size_list, 1, 2)

        # An example of a stacked layout
        self.setLayout(QtWidgets.QVBoxLayout())
        self.stacked_layout = QtWidgets.QStackedLayout()
        self.layout().addLayout(self.stacked_layout)

        button_layout = QtWidgets.QHBoxLayout()
        layout_btn_1 = QtWidgets.QPushButton('Layout 1')
        layout_btn_2 = QtWidgets.QPushButton('Layout 2')
        layout_btn_3 = QtWidgets.QPushButton('Layout 3')
        layout_btn_4 = QtWidgets.QPushButton('Layout 4')
        button_layout.addWidget(layout_btn_1)
        button_layout.addWidget(layout_btn_2)
        button_layout.addWidget(layout_btn_3)
        button_layout.addWidget(layout_btn_4)

        self.layout().addLayout(button_layout)

        hbox_widget = QtWidgets.QWidget()
        hbox_widget.setLayout(QtWidgets.QHBoxLayout())

        btn_1 = QtWidgets.QPushButton('Button 1')
        btn_2 = QtWidgets.QPushButton('Button 2')
        btn_3 = QtWidgets.QPushButton('Button 3')
        btn_4 = QtWidgets.QPushButton('Button 4')
        btn_5 = QtWidgets.QPushButton('Button 5')

        hbox_widget.layout().addWidget(btn_1)
        hbox_widget.layout().addWidget(btn_2)
        hbox_widget.layout().addWidget(btn_3)
        hbox_widget.layout().addWidget(btn_4)
        hbox_widget.layout().addWidget(btn_5)

        vbox_widget = QtWidgets.QWidget()
        vbox_widget.setLayout(QtWidgets.QVBoxLayout())

        btn_1 = QtWidgets.QPushButton('Button 1')
        btn_2 = QtWidgets.QPushButton('Button 2')
        btn_3 = QtWidgets.QPushButton('Button 3')
        btn_4 = QtWidgets.QPushButton('Button 4')
        btn_5 = QtWidgets.QPushButton('Button 5')

        vbox_widget.layout().addWidget(btn_1)
        vbox_widget.layout().addWidget(btn_2)
        vbox_widget.layout().addWidget(btn_3)
        vbox_widget.layout().addWidget(btn_4)
        vbox_widget.layout().addWidget(btn_5)

        form_widget = QtWidgets.QWidget()
        form_widget.setLayout(QtWidgets.QFormLayout())

        name_le = QtWidgets.QLineEdit()
        email_le = QtWidgets.QLineEdit()
        age_sb = QtWidgets.QSpinBox()

        form_widget.layout().addRow('Name: ', name_le)
        form_widget.layout().addRow('Email: ', email_le)
        form_widget.layout().addRow('Age: ', age_sb)

        grid_widget = QtWidgets.QWidget()
        grid_widget.setLayout(QtWidgets.QGridLayout())

        font_name_lb = QtWidgets.QLabel('Font')
        font_style_lb = QtWidgets.QLabel('Font Style')
        font_size_lb = QtWidgets.QLabel('Size')

        font_names_list = QtWidgets.QListWidget()
        font_names_list.addItem('Times')
        font_names_list.addItem('Helvetica')
        font_names_list.addItem('Courier')

        font_style_list = QtWidgets.QListWidget()
        font_style_list.addItem('Roman')
        font_style_list.addItem('Italic')
        font_style_list.addItem('Oblique')

        font_size_list = QtWidgets.QListWidget()
        for index in range(10, 30, 2):
            font_size_list.addItem(str(index))

        grid_widget.layout().addWidget(font_name_lb, 0, 0)
        grid_widget.layout().addWidget(font_names_list, 1, 0)

        grid_widget.layout().addWidget(font_style_lb, 0, 1)
        grid_widget.layout().addWidget(font_style_list, 1, 1)

        grid_widget.layout().addWidget(font_size_lb, 0, 2)
        grid_widget.layout().addWidget(font_size_list, 1, 2)

        self.stacked_layout.addWidget(vbox_widget)
        self.stacked_layout.addWidget(hbox_widget)
        self.stacked_layout.addWidget(form_widget)
        self.stacked_layout.addWidget(grid_widget)

        layout_btn_1.clicked.connect(partial(self.stacked_layout.setCurrentIndex, 0))
        layout_btn_2.clicked.connect(partial(self.stacked_layout.setCurrentIndex, 1))
        layout_btn_3.clicked.connect(partial(self.stacked_layout.setCurrentIndex, 2))
        layout_btn_4.clicked.connect(partial(self.stacked_layout.setCurrentIndex, 3))


dialog = QtUi()
dialog.show()
