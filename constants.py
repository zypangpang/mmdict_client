from enum import Enum
import platform,os
from pathlib import Path

from PyQt5.QtGui import QColorConstants

from gui_client.gui_config import GuiConfigs
OS_NAME=platform.system()

DEFAULT_CONFIG_PATH=Path.home().joinpath(".mmdict_client/configs.ini")

class FRONT_END(Enum):
    QTWEBENGINE=1
    CONSOLE=2

SOCKET_LOCATION = "/tmp/mmdict_socket"


color_map = {
    'white': QColorConstants.White,
    'black': QColorConstants.Black,
    'yellow': QColorConstants.Cyan,
    'green': QColorConstants.Green
}

SHORTCUTS_DESC='''
Keyboard shortcuts:
    Enter: Lookup/Search
    Ctrl+L: focus input line edit
    j/k: Scroll down/up
    g: Back to top
    Ctrl+Plus/Minus: Zoom out/in
'''
HELP_TEXT='''
[mmDict qt client] Another mdict application.
Combined with mmDict server program.
Github pages:
   Client: https://github.com/zypangpang/mmdict_client
   Server: https://github.com/zypangpang/mmdict_daemon
Feel free to create issues!
'''
configs=None
SHOW_SETTING_DIALOG=False

if not GuiConfigs.check_config_file(DEFAULT_CONFIG_PATH):
    os.makedirs(DEFAULT_CONFIG_PATH.parent, 0o0755,True)
    path = GuiConfigs.generate_init_configs(DEFAULT_CONFIG_PATH)
    SHOW_SETTING_DIALOG = True
    print(f"Cannot find the config file. Auto generated a config file {path}.")

configs = GuiConfigs(DEFAULT_CONFIG_PATH)

