# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingDialog(object):
    def setupUi(self, SettingDialog):
        SettingDialog.setObjectName("SettingDialog")
        SettingDialog.setWindowModality(QtCore.Qt.WindowModal)
        SettingDialog.resize(430, 480)
        SettingDialog.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 430, 411, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(SettingDialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 411, 401))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_2 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_3 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.http_host_edit = QtWidgets.QLineEdit(self.widget)
        self.http_host_edit.setObjectName("http_host_edit")
        self.gridLayout_2.addWidget(self.http_host_edit, 2, 1, 1, 1)
        self.bg_label_2 = QtWidgets.QLabel(self.widget)
        self.bg_label_2.setObjectName("bg_label_2")
        self.gridLayout_2.addWidget(self.bg_label_2, 0, 0, 1, 1)
        self.dict_port_box = QtWidgets.QSpinBox(self.widget)
        self.dict_port_box.setMinimum(1)
        self.dict_port_box.setMaximum(65535)
        self.dict_port_box.setObjectName("dict_port_box")
        self.gridLayout_2.addWidget(self.dict_port_box, 1, 1, 1, 1)
        self.bg_label_4 = QtWidgets.QLabel(self.widget)
        self.bg_label_4.setObjectName("bg_label_4")
        self.gridLayout_2.addWidget(self.bg_label_4, 2, 0, 1, 1)
        self.dict_host_edit = QtWidgets.QLineEdit(self.widget)
        self.dict_host_edit.setObjectName("dict_host_edit")
        self.gridLayout_2.addWidget(self.dict_host_edit, 0, 1, 1, 1)
        self.bg_label_3 = QtWidgets.QLabel(self.widget)
        self.bg_label_3.setObjectName("bg_label_3")
        self.gridLayout_2.addWidget(self.bg_label_3, 1, 0, 1, 1)
        self.bg_label_5 = QtWidgets.QLabel(self.widget)
        self.bg_label_5.setObjectName("bg_label_5")
        self.gridLayout_2.addWidget(self.bg_label_5, 3, 0, 1, 1)
        self.http_port_box = QtWidgets.QSpinBox(self.widget)
        self.http_port_box.setMinimum(1)
        self.http_port_box.setMaximum(65535)
        self.http_port_box.setObjectName("http_port_box")
        self.gridLayout_2.addWidget(self.http_port_box, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_4 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.bg_box = QtWidgets.QComboBox(self.widget)
        self.bg_box.setObjectName("bg_box")
        self.bg_box.addItem("")
        self.bg_box.addItem("")
        self.bg_box.addItem("")
        self.bg_box.addItem("")
        self.gridLayout.addWidget(self.bg_box, 0, 1, 1, 1)
        self.zoom_factor_box = QtWidgets.QDoubleSpinBox(self.widget)
        self.zoom_factor_box.setDecimals(1)
        self.zoom_factor_box.setMinimum(0.1)
        self.zoom_factor_box.setMaximum(2.0)
        self.zoom_factor_box.setSingleStep(0.1)
        self.zoom_factor_box.setObjectName("zoom_factor_box")
        self.gridLayout.addWidget(self.zoom_factor_box, 2, 1, 1, 1)
        self.bg_label_6 = QtWidgets.QLabel(self.widget)
        self.bg_label_6.setObjectName("bg_label_6")
        self.gridLayout.addWidget(self.bg_label_6, 1, 0, 1, 1)
        self.sound_player_edit = QtWidgets.QLineEdit(self.widget)
        self.sound_player_edit.setObjectName("sound_player_edit")
        self.gridLayout.addWidget(self.sound_player_edit, 1, 1, 1, 1)
        self.bg_label_7 = QtWidgets.QLabel(self.widget)
        self.bg_label_7.setObjectName("bg_label_7")
        self.gridLayout.addWidget(self.bg_label_7, 2, 0, 1, 1)
        self.bg_label = QtWidgets.QLabel(self.widget)
        self.bg_label.setObjectName("bg_label")
        self.gridLayout.addWidget(self.bg_label, 0, 0, 1, 1)
        self.bg_label_8 = QtWidgets.QLabel(self.widget)
        self.bg_label_8.setObjectName("bg_label_8")
        self.gridLayout.addWidget(self.bg_label_8, 3, 0, 1, 1)
        self.welcome_edit = QtWidgets.QLineEdit(self.widget)
        self.welcome_edit.setObjectName("welcome_edit")
        self.gridLayout.addWidget(self.welcome_edit, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(SettingDialog)
        self.buttonBox.accepted.connect(SettingDialog.accept)
        self.buttonBox.rejected.connect(SettingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingDialog)

    def retranslateUi(self, SettingDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingDialog.setWindowTitle(_translate("SettingDialog", "Settings"))
        self.label_2.setText(_translate("SettingDialog", "Server settings"))
        self.bg_label_2.setText(_translate("SettingDialog", "dict host"))
        self.bg_label_4.setText(_translate("SettingDialog", "http host"))
        self.bg_label_3.setText(_translate("SettingDialog", "dict port"))
        self.bg_label_5.setText(_translate("SettingDialog", "http port"))
        self.label.setText(_translate("SettingDialog", "Client settings"))
        self.bg_box.setItemText(0, _translate("SettingDialog", "white"))
        self.bg_box.setItemText(1, _translate("SettingDialog", "black"))
        self.bg_box.setItemText(2, _translate("SettingDialog", "yellow"))
        self.bg_box.setItemText(3, _translate("SettingDialog", "green"))
        self.bg_label_6.setText(_translate("SettingDialog", "Sound player"))
        self.bg_label_7.setText(_translate("SettingDialog", "Zoom"))
        self.bg_label.setText(_translate("SettingDialog", "Background Color"))
        self.bg_label_8.setText(_translate("SettingDialog", "Welcome text"))
