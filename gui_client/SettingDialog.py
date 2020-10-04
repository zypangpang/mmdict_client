from PyQt5 import QtWidgets
from .ui.ui_setting_dialog import Ui_SettingDialog
from constants import configs
from .gui_config import GuiConfigs
from .gui_utils import get_widget_value,set_widget_value

class SettingDialog(QtWidgets.QDialog):

    def __init__(self,parent=None):
        super().__init__(parent)

        self.ui= Ui_SettingDialog()
        self.ui.setupUi(self)

        self.server_widgets = {}
        self.client_widgets = {}

        self.__organize_widgets()

        self.__load_settings()


    def set_bg_color(self,color):
        self.staged_settings['set_bg_color']=color

    def __organize_widgets(self):
        # server
        self.server_widgets[configs.DICT_HOST]=self.ui.dict_host_edit
        self.server_widgets[configs.DICT_PORT]=self.ui.dict_port_box
        self.server_widgets[configs.HTTP_PORT]=self.ui.http_port_box
        self.server_widgets[configs.HTTP_HOST]=self.ui.http_host_edit
        # client
        self.client_widgets[configs.BG_COLOR]=self.ui.bg_box
        self.client_widgets[configs.SOUND_PLAYER]=self.ui.sound_player_edit
        self.client_widgets[configs.ZOOM_FACTOR]=self.ui.zoom_factor_box
        self.client_widgets[configs.WELCOME_WORD]=self.ui.welcome_edit


    def __load_settings(self):
        for key,widget in self.server_widgets.items():
            set_widget_value(widget, configs.get_server_value(key))
        for key,widget in self.client_widgets.items():
            set_widget_value(widget,configs.get_client_value(key))

    def __export_settings(self):
        client_settings={}
        server_settings={}
        for key, widget in self.server_widgets.items():
            server_settings[key]=get_widget_value(widget)

        for name,widget in self.client_widgets.items():
            client_settings[name]=get_widget_value(widget)

        return server_settings,client_settings

    def accept(self) -> None:
        server_s,client_s=self.__export_settings()
        GuiConfigs.need_write_back=True
        configs.set_server_config(server_s)
        configs.set_client_config(client_s)
        #for func,val in self.staged_settings.items():
        #    getattr(configs,func)(val)
        super().accept()



