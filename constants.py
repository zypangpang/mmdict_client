from enum import Enum
import platform,os
from pathlib import Path
from gui_client.gui_config import GuiConfigs
OS_NAME=platform.system()

DEFAULT_CONFIG_PATH=Path.home().joinpath(".mmdict_client/configs.ini")

class FRONT_END(Enum):
    QTWEBENGINE=1
    CONSOLE=2

SOCKET_LOCATION = "/tmp/mmdict_socket"

if not GuiConfigs.check_config_file(DEFAULT_CONFIG_PATH):
    os.makedirs(DEFAULT_CONFIG_PATH.parent, 0o0755,True)
    path = GuiConfigs.generate_init_configs(DEFAULT_CONFIG_PATH)
    print(f"Cannot find the config file. Auto generated a config file {path}. Change its "
                         f"content accordingly. Click OK to exit.")
    exit(0)

configs = GuiConfigs(DEFAULT_CONFIG_PATH)



