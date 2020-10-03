from PyQt5 import QtWidgets
from .ui.ui_setting_dialog import Ui_SettingDialog
from constants import configs

class SettingDialog(QtWidgets.QDialog):

    def __init__(self,parent):
        super().__init__(parent)

        self.ui= Ui_SettingDialog()
        self.ui.setupUi(self)

        self.ui.bg_box.setCurrentText(configs.get_bg_color())
        self.ui.bg_box.currentTextChanged.connect(self.set_bg_color)

        self.staged_settings={}

    def set_bg_color(self,color):
        self.staged_settings['set_bg_color']=color

    def accept(self) -> None:
        for func,val in self.staged_settings.items():
            getattr(configs,func)(val)
        super().accept()



