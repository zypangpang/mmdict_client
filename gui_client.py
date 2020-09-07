from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from gui_client.gui import MainWindow
import constants,configs
import fire
from gui_client.current_state import CurrentState
from gui_client.gui_utils import ProgressDialog
from gui_client.work_thread import InitDictThread

#from signal import signal, SIGINT,  SIGTERM
#signal(SIGTERM, lambda : exit(0))
#signal(SIGINT,lambda :exit(0))

app = QApplication([])
ex = MainWindow()

def show_mainwindow(dicts):
    ProgressDialog.hide_progress()
    if not dicts:
        QtWidgets.QMessageBox.critical(ex,"Error",
                                       "It seems the mmdict daemon is not running."
                                       " Please first run the daemon. Click OK to exit.")
        exit(1)
        #msgBox.setWindowTitle("Error")
        #msgBox.setText("It seems the mmdict daemon is not running. Please first run the daemon. "
        #               "Click OK to exit.")
        #msgBox.buttonClicked.connect(lambda x: exit(1))
        #msgBox.

    else:
        CurrentState.set_dict_infos(dicts)
        ex.show()

initThread=InitDictThread()
initThread.result_ready.connect(show_mainwindow)
initThread.finished.connect(initThread.deleteLater)

def run_gui():
    ProgressDialog.show_progress(None,"Init dicts...")
    initThread.start()
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


