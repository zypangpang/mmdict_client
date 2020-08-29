from PyQt5.QtWidgets import QApplication
from gui_client.gui import MainWindow
import constants
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
        if not dict_host:
            print("dict_host is required.")
            return
        constants.DICT_HOST=dict_host
        if dict_host=='unix':
            if not http_host or not http_port:
                print("http_host and http_port is required.")
                return
            constants.HTTP_HOST=http_host
            constants.HTTP_PORT=int(http_port)
        else:
            if not dict_port:
                print("dict_port is required.")
                return
            constants.DICT_PORT=int(dict_port)

            if not http_host:
                print("Use dict_host as http_host.")
                constants.HTTP_HOST=dict_host
            else:
                constants.HTTP_HOST=http_host

            if not http_port:
                print("http_port is required.")
                return
            constants.HTTP_PORT=int(http_port)

        run_gui()





if __name__ == '__main__':
    fire.Fire(Main)


