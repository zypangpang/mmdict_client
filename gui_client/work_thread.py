from PyQt5.QtCore import QThread, pyqtSignal

from gui_client.socket_client import SocketClient


class LookupThread(QThread):
    result_ready=pyqtSignal(str,dict)
    def __init__(self,word):
        super().__init__()
        self.word=word
        self.dicts=None

    def run(self) -> None:
        print(f"lookup {self.word} start")
        result_obj = SocketClient.lookup(self.word,self.dicts)
        print(f"lookup {self.word} done")
        self.result_ready.emit(self.word,result_obj)



