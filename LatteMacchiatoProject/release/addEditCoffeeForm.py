from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(619, 177)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.var_name = QtWidgets.QLineEdit(Form)
        self.var_name.setMinimumSize(QtCore.QSize(0, 50))
        self.var_name.setObjectName("var_name")
        self.gridLayout.addWidget(self.var_name, 2, 1, 1, 1)
        self.type = QtWidgets.QLineEdit(Form)
        self.type.setMinimumSize(QtCore.QSize(0, 50))
        self.type.setObjectName("type")
        self.gridLayout.addWidget(self.type, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.id = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id.sizePolicy().hasHeightForWidth())
        self.id.setSizePolicy(sizePolicy)
        self.id.setMinimumSize(QtCore.QSize(0, 50))
        self.id.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 2, 0, 1, 1)
        self.r_deg = QtWidgets.QLineEdit(Form)
        self.r_deg.setMinimumSize(QtCore.QSize(0, 50))
        self.r_deg.setObjectName("r_deg")
        self.gridLayout.addWidget(self.r_deg, 2, 2, 1, 1)
        self.price = QtWidgets.QLineEdit(Form)
        self.price.setMinimumSize(QtCore.QSize(0, 50))
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 2, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.t_desc = QtWidgets.QLineEdit(Form)
        self.t_desc.setMinimumSize(QtCore.QSize(0, 50))
        self.t_desc.setObjectName("t_desc")
        self.gridLayout.addWidget(self.t_desc, 2, 4, 1, 1)
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.pack_vol = QtWidgets.QLineEdit(Form)
        self.pack_vol.setMinimumSize(QtCore.QSize(0, 50))
        self.pack_vol.setObjectName("pack_vol")
        self.gridLayout.addWidget(self.pack_vol, 2, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 0, 1, 3)
        self.changeButton = QtWidgets.QPushButton(Form)
        self.changeButton.setObjectName("changeButton")
        self.gridLayout.addWidget(self.changeButton, 0, 4, 1, 3)
        self.error_label = QtWidgets.QLabel(Form)
        self.error_label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.gridLayout.addWidget(self.error_label, 3, 0, 1, 7)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add-change"))
        self.label_4.setText(_translate("Form", "type"))
        self.label_2.setText(_translate("Form", "variety_name"))
        self.label_5.setText(_translate("Form", "price"))
        self.label_3.setText(_translate("Form", "roasting_degree"))
        self.label_1.setText(_translate("Form", "id"))
        self.label.setText(_translate("Form", "taste_description"))
        self.label_6.setText(_translate("Form", "packing_volume"))
        self.addButton.setText(_translate("Form", "????????????????"))
        self.changeButton.setText(_translate("Form", "????????????????"))
