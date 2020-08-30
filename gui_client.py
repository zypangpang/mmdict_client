from PyQt5.QtWidgets import QApplication
from gui_client.gui import MainWindow
import constants,configs
import fire

#from signal import signal, SIGPIPE,  SIG_IGN
#signal(SIGPIPE, SIG_IGN)

def run_gui():
    app=QApplication([])
    ex=MainWindow()
    ex.show()
    app.exec()

class Main:
    def run(self,dict_host=None,dict_port=None,http_host=None,http_port=None):
        if dict_host:
            configs.DICT_HOST=dict_host
        if dict_port:
            configs.DICT_PORT=int(dict_port)
        if http_host:
            configs.HTTP_HOST=http_host
        if http_port:
            configs.HTTP_PORT=http_port

        run_gui()





if __name__ == '__main__':
    fire.Fire(Main)


