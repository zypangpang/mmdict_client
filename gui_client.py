from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore
from gui_client.socket_client import SocketClient
from gui_client.gui import MainWindow

#from signal import signal, SIGPIPE,  SIG_IGN
#signal(SIGPIPE, SIG_IGN)


def test_qt():
    #header='<meta charset="UTF-8"/>\n'
    _,record=lookup("mouse")
    #print(QDir.currentPath())
    #print(record)
    #record=header+record
    app=QApplication([])
    set_default_font()
    view = QtWebEngineWidgets.QWebEngineView()
    page=MyWebPage()
    view.setPage(page)
    baseUrl = QUrl.fromLocalFile(QDir.currentPath() + "/index.html")
    print(baseUrl)
    page.setHtml(record,baseUrl)
    #view.load(QUrl("file://t.html"))
    #load_css_js_from_file('css',view,"LDOCE6.css","ld6")
    #load_css_js_from_file('js',view,"entry.js","entry")
    view.show()
    app.exec_()

def test_window():
    app=QApplication([])
    ex=MainWindow()
    app.exec()


def test_client():
    q=QUrl("entry: abc")
    print(q.toString().split(":")[1].strip("/ "))
    print(q.scheme())
    print(q.host())
    print(q.path())
    print(q.fragment())


if __name__ == '__main__':
    #output(300)
    test_window()


