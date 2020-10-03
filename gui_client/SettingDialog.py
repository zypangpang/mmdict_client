from PyQt5 import QtWidgets
from .ui.ui_setting_dialog import Ui_SettingDialog

class SettingDialog(QtWidgets.QDialog):

    def __init__(self,parent):
        super().__init__(parent)

        Ui_SettingDialog().setupUi(self)


