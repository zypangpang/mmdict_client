from pathlib import Path

from PyQt5 import QtWebEngineWidgets, QtCore
from PyQt5.QtCore import QUrl,Qt
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
import PyQt5.QtWidgets as Widgets
import configs
import requests,subprocess

class ProgressDialog:
    progress=None
    @classmethod
    def show_progress(cls,parent,title):
        cls.progress = Widgets.QProgressDialog(title, None, 0, 0, parent)
        cls.progress.setWindowModality(Qt.WindowModal)
        cls.progress.setMinimumDuration(500)
        cls.progress.setValue(0)

    @classmethod
    def hide_progress(cls):
        try:
            cls.progress.close()
            cls.progress.deleteLater()
            cls.progress=None
        except:
            print("progress delete failed")

def set_default_font(font,size):
    fontDataBase = QFontDatabase()
    defaultSettings = QWebEngineSettings.globalSettings()
    standardFont = fontDataBase.font(font, "", 12)
    defaultSettings.setFontFamily(QWebEngineSettings.StandardFont, standardFont.family())
    defaultSettings.setFontSize(QWebEngineSettings.DefaultFontSize, size)

def loadJS(view,SCRIPT,name):
    script = QtWebEngineWidgets.QWebEngineScript()
    view.page().runJavaScript(SCRIPT, QtWebEngineWidgets.QWebEngineScript.ApplicationWorld)
    script.setName(name)
    script.setSourceCode(SCRIPT)
    script.setInjectionPoint(QtWebEngineWidgets.QWebEngineScript.DocumentReady)
    script.setRunsOnSubFrames(True)
    script.setWorldId(QtWebEngineWidgets.QWebEngineScript.MainWorld)
    view.page().scripts().insert(script)

def load_css_js_from_file(type,view,path,name):
    path = QtCore.QFile(path)
    if not path.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
        return
    content = path.readAll().data().decode("utf-8")
    if type=='css':
        loadCSS(view,content,name)
    else:
        loadJS(view,content,name)

def loadCSS(view, css, name):
    SCRIPT = """
    (function() {
    css = document.createElement('style');
    css.type = 'text/css';
    css.id = "%s";
    document.head.appendChild(css);
    css.innerText = `%s`;
    })()
    """ % (name, css)

    loadJS(view,SCRIPT,name)
def pretty_dict_result(name,value):
    header = '<meta charset="utf-8"/>\n'
    html=header+\
         f'<h4 style="background-color:LightGray; padding-top: 5px; padding-bottom: 5px;'\
         f'padding-left: 5px; padding-right:5px">{name}</h4>' +\
         value
    return html


def join_dict_results(result_obj):
    header='<meta charset="utf-8"/>\n'
    html_list = []
    for dict, value in result_obj.items():
        html_list.append(
            f'<h4 style="background-color:LightGray; padding-top: 5px; padding-bottom: 5px;'
            f'padding-left: 5px; padding-right:5px">{dict}</h4>' + value
        )
    if not html_list:
        return header+"<h3>No results found</h3>"
    return header+"\n".join(html_list)

def get_data_folder_url(data_folder):
    #return QUrl.fromLocalFile(str(Path(data_folder).joinpath("index.html")))
    return QUrl.fromLocalFile(data_folder+"/index.html")

def httpPlaySound(sound_path,dict_name):
    addr=f"{configs.HTTP_SCHEME}://{configs.HTTP_HOST}:{configs.HTTP_PORT}/{dict_name}/{sound_path}"
    print(addr)

    r=requests.get(addr)
    with open("/tmp/mmdict_sound.tmp",'wb') as f:
        f.write(r.content)
    command=[configs.SOUND_PLAYER, "/tmp/mmdict_sound.tmp"]
    # os.system(SOUND_PLAYER+" "+str(Path(data_folder).joinpath(item)))
    subprocess.Popen(command)
    #if res.returncode != 0:
    #    raise Exception(f"{configs.SOUND_PLAYER} play sound error. Check both the program and sound file.")

