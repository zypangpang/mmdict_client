from PyQt5.QtCore import QThread, pyqtSignal

from gui_client.socket_client import SocketClient


class LookupThread(QThread):
    result_ready=pyqtSignal(str,dict,int)
    def __init__(self):
        super().__init__()
        self.word=None
        self.dicts=None

    def run(self) -> None:
        print(f"lookup {self.word} start")
        result_obj={}
        status_code=0
        try:
            result_obj = SocketClient.lookup(self.word,self.dicts)
        except Exception as e:
            print(e)
            status_code=1
        print(f"lookup {self.word} done")
        self.result_ready.emit(self.word,result_obj,status_code)

class IndexSearchThread(QThread):
    result_ready=pyqtSignal(str,dict,int)
    def __init__(self):
        super().__init__()
        self.word=None
        self.dict_name=None

    def run(self) -> None:
        print(f"lookup index {self.word} start")
        all_words={}
        status_code=0
        try:
            all_words= SocketClient.search_word_index(self.dict_name,self.word)
        except:
            status_code=1
        print(f"lookup index {self.word} done")
        self.result_ready.emit(self.word,all_words,status_code)

class InitDictThread(QThread):
    result_ready=pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def run(self) -> None:
        print(f"init dicts...")
        try:
            dicts=SocketClient.list_dicts()
        except:
            print(f"init dicts done...")
            self.result_ready.emit({})
            return

        print(f"init dicts done...")
        self.result_ready.emit(dicts)






