from enum import Enum

class FRONT_END(Enum):
    QTWEBENGINE=1
    CONSOLE=2

SOCKET_LOCATION = "/tmp/mmdict_socket"

DICT_HOST="unix"
DICT_PORT=9999

HTTP_HOST="localhost"
HTTP_PORT="8000"

SOUND_PLAYER='mpv'
