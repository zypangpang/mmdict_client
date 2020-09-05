import logging,subprocess,requests,io
import configs
import PyQt5.QtWidgets as Widgets
from PyQt5.QtCore import QUrl, pyqtSignal, Qt, QEvent
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor, QWebEngineUrlRequestInfo, QWebEngineUrlSchemeHandler, \
    QWebEngineUrlScheme
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEnginePage, QWebEngineProfile, QWebEngineScript
from PyQt5 import QtWebEngineWidgets, QtCore
from .socket_client import SocketClient
from .gui_utils import set_default_font,pretty_dict_result

'''
class MyUrlRequestInterceptor(QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info: QWebEngineUrlRequestInfo) -> None:
        print(info.requestUrl())

class EntrySchemeHandler(QWebEngineUrlSchemeHandler):
    def requestStarted(self, request):
        url = request.requestUrl()
        _,item = url.toString().split(":")
        item=item.strip("/ ")
        result_obj: dict = SocketClient.lookup(item)
        raw_html=join_dict_results(result_obj).encode("utf-8")
        buf = QtCore.QBuffer(request)
        #request.destroyed.connect(buf.deleteLater)
        buf.open(QtCore.QIODevice.WriteOnly)
        buf.write(raw_html)
        buf.seek(0)
        buf.close()
        request.reply(b"text/html", buf)
'''
class CurrentState():
    word=None
    dict_names=[]
    cur_dict_name=None
    history=[]
    result_obj={}
    all_words=None

    #@classmethod
    #def get_all_words(cls):
    #    if not cls.cur_dict_name:
    #        return []
    #    if not cls.all_words:
    #        cls.all_words=SocketClient.search_word_index(cls.cur_dict_name)
    #    return cls.all_words

    @classmethod
    def set_dict_infos(cls,dicts):
        cls.dict_names=dicts
        #for dict in dicts:
        #    cls.dictionaries[dict[0]]=dict[1:]
        #    cls.dict_names.append(dict[0])

        cls.cur_dict_name=cls.dict_names[0]

    @classmethod
    def reset(cls,word,result_obj):
        cls.word=word
        cls.result_obj=result_obj
        cls.history=[]
        avl_dicts=cls.get_avl_dicts()
        if not avl_dicts:
            cls.cur_dict_name=None
        else: #cls.cur_dict_name not in avl_dicts:
            cls.cur_dict_name=avl_dicts[0]

    @classmethod
    def reset_history(cls):
        cls.history=[]

    @classmethod
    def get_avl_dicts(cls):
        ans=[]
        for name in cls.dict_names:
            if name in cls.result_obj:
                ans.append(name)
        return ans

    @classmethod
    def add_history(cls,entry):
        cls.history.append(entry)

    @classmethod
    def get_prev_entry(cls):
        if len(cls.history)>1:
            cls.history.pop()
            return cls.history[-1]
        return None


    @classmethod
    def get_definition(cls,dict_name=None):
        if dict_name:
            cls.cur_dict_name=dict_name
            cls.all_words=None

        return cls.cur_dict_name,cls.result_obj.get(cls.cur_dict_name,"No entry found")


    @classmethod
    def set_cur_dict(cls,name):
        cls.cur_dict_name=name
    @classmethod
    def get_cur_dict(cls):
        return cls.cur_dict_name

    #@classmethod
    #def get_cur_dict_info(cls):
    #    if cls.cur_dict_name:
    #        return cls.cur_dict_name, cls.dictionaries[cls.cur_dict_name][1]
    #    if len(cls.dict_names) > 0:
    #        cls.set_cur_dict(cls.dict_names[0])
    #        return cls.cur_dict_name,cls.dictionaries[cls.cur_dict_name][1]
    #    return "",""

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

class MyWebPage(QWebEnginePage):
    play_sound_error_sig=pyqtSignal(str)
    #text_selected=pyqtSignal(str)
    def acceptNavigationRequest(self, url: QUrl, type: QWebEnginePage.NavigationType, isMainFrame: bool, **kwargs):
        if type == QWebEnginePage.NavigationTypeLinkClicked:
            if url.scheme() == 'entry':
                _, item = url.toString().split(":")
                item = item.strip("/ ")
                dict_name=CurrentState.get_cur_dict()
                #try:
                result_obj: dict = SocketClient.lookup(item,[dict_name])
                raw_html = pretty_dict_result(dict_name,result_obj.get(dict_name,"No entry found"))
                #except Exception as e:
                #    print(f"Lookup {item} error = {e}")
                #    return False
                #print(self.url())
                self.setHtml(raw_html,self.url())
                CurrentState.add_history(item)
            elif url.scheme() == 'sound':
                item=url.toString().split("://")[1]
                name=CurrentState.get_cur_dict()
                try:
                    httpPlaySound(item,name)
                except Exception as e:
                    self.play_sound_error_sig.emit(str(e))
                    print(f"play sound error = {e}")

                #command=[SOUND_PLAYER, str(Path(data_folder).joinpath(item))]
                #os.system(SOUND_PLAYER+" "+str(Path(data_folder).joinpath(item)))
                #subprocess.Popen(command)

            return False

        return True

    '''
    def event(self, event: QtCore.QEvent) -> bool:
        if event.type()==QEvent.MouseButtonDblClick:
            text=self.selectedText().strip()
            if text:
                print(text)
                self.text_selected.emit(text)
        return super().event(event)
    '''


ENTRY_SCHEME=b"entry"

class MainWindow(Widgets.QWidget):

    def __init__(self):
        super().__init__()

        self.http_prefix=f"{configs.HTTP_SCHEME}://{configs.HTTP_HOST}:{configs.HTTP_PORT}"
        self.zoom_factor=1
        self.init_dictionary()

        #QWebEngineUrlScheme.registerScheme(QWebEngineUrlScheme(ENTRY_SCHEME))

        self.line_edit=Widgets.QLineEdit()
        self.line_edit.setPlaceholderText("Type word to lookup. [Ctrl+L]")
        self.search_button=Widgets.QPushButton('&Lookup')
        self.status_bar=Widgets.QStatusBar()
        self.back_btn=Widgets.QPushButton('&Back')
        self.help_btn=Widgets.QPushButton('&Help')
        #self.next_btn=Widgets.QPushButton("Next")
        self.dict_list_widget= Widgets.QListWidget()
        self.index_line_edit=Widgets.QLineEdit()
        self.index_line_edit.setPlaceholderText("index search")
        self.index_search_btn=Widgets.QPushButton("&Search")
        self.index_search_items=Widgets.QListWidget()

        self.init_webview()


        self.init_layout()

        self.connect_slot()
        self.setWindowTitle("mmDict")

    def init_dictionary(self):
        try:
            CurrentState.set_dict_infos(SocketClient.list_dicts())
        except Exception as e:
            logging.error(e)
            logging.error("It seems the mmdict daemon is not running. Please first run the daemon.")
            exit(1)

    def init_layout(self):
        layout = Widgets.QVBoxLayout()
        first_row_layout = Widgets.QHBoxLayout()
        first_row_layout.addWidget(self.line_edit)
        first_row_layout.addWidget(self.search_button)
        first_row_layout.addWidget(self.back_btn)
        first_row_layout.addWidget(self.help_btn)
        #first_row_layout.addWidget(self.next_btn)
        layout.addLayout(first_row_layout)

        second_row_layout = Widgets.QHBoxLayout()
        second_row_layout.addWidget(self.view)
        #self.view.setSizePolicy(Widgets.QSizePolicy.Expanding,Widgets.QSizePolicy.Expanding)

        #self.dict_list_widget.setMaximumWidth(400)
        #self.index_search_items.setMaximumWidth(400)

        second_row_second_col=Widgets.QGridLayout()
        second_row_second_col.addWidget(self.dict_list_widget,0,0,1,2)
        second_row_second_col.addWidget(self.index_line_edit,1,0)
        second_row_second_col.addWidget(self.index_search_btn,1,1)
        second_row_second_col.addWidget(self.index_search_items,2,0,1,2)

        second_row_layout.addLayout(second_row_second_col)

        second_row_layout.setStretch(0, 3)
        second_row_layout.setStretch(1, 1)

        layout.addLayout(second_row_layout)

        self.status_bar.setFixedHeight(20)
        layout.addWidget(self.status_bar)

        #layout.setSpacing(0)
        layout.setContentsMargins(3,3,3,3)

        self.setLayout(layout)
        self.setMinimumHeight(700)
        self.setMinimumWidth(700)

    def init_webview(self):
        set_default_font("Noto Sans CJK SC",16)

        # disable scroll bar
        #defaultSettings = QWebEngineSettings.globalSettings()
        #defaultSettings.setAttribute(QWebEngineSettings.ShowScrollBars,False)

        #self.profile=QWebEngineProfile.defaultProfile()
        #handler = self.profile.urlSchemeHandler(ENTRY_SCHEME)
        #if handler is not None:
        #    self.profile.removeUrlSchemeHandler(handler)
        #self.handler=EntrySchemeHandler()
        #self.profile.installUrlSchemeHandler(ENTRY_SCHEME,self.handler)

        self.page = MyWebPage()

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.setPage(self.page)
        style="""
        @keyframes example {
  0%   {color:red; left:50px; top:50px;}
  25%  {color:yellow; left:250px; top:50px;}
  50%  {color:blue; left:250px; top:450px;}
  75%  {color:green; left:50px; top:450px;}
  100% {color:red; left:50px; top:50px;}
}
h1 {
animation-name: example; 
animation-duration: 4s;
position:relative;
animation-iteration-count: 2;
display: table;
left: 50px;
top:50px;
}
.center {
    position: fixed;
  left: 50%;
  bottom: 0px;
  transform: translate(-50%, -50%);
  margin: 0 auto;
}
.footer{
position:absolute;
bottom:10px;
}
        """

        #self.page.setHtml(f'<style>{style}</style><h1>:-)<br>Welcome to mmDict</h1><p class="center ">Copyright &copy ZaiyuPang 2020</p>')
        self.page.setHtml(f'<style>{style}</style><h1>:-)<br>Welcome to mmDict</h1>')

        #self.interceptor=MyUrlRequestInterceptor()
        #self.profile.setUrlRequestInterceptor(self.interceptor)

    def connect_slot(self):
        self.search_button.clicked.connect(self.lookup)
        self.page.linkHovered.connect(self.showMessage)
        self.page.play_sound_error_sig.connect(lambda e: self.showMessage(e))
        self.page.selectionChanged.connect(self.search_selected)
        self.back_btn.clicked.connect(self.history_back)
        self.help_btn.clicked.connect(self.show_help)
        self.dict_list_widget.itemClicked.connect(self.switch_dict)
        self.index_search_btn.clicked.connect(self.search_index)
        self.index_search_items.itemClicked.connect(self.click_index_search)
        Widgets.QShortcut(QKeySequence(Qt.CTRL+Qt.Key_Return),self.line_edit).activated.connect(self.lookup)
        Widgets.QShortcut(QKeySequence(Qt.Key_J),self.view).activated.connect(self.scrollDown)
        Widgets.QShortcut(QKeySequence(Qt.Key_K),self.view).activated.connect(self.scrollUp)
        Widgets.QShortcut(QKeySequence(Qt.Key_G),self.view).activated.connect(
            lambda : self.view.page().runJavaScript("window.scrollTo(0,0);")
        )
        self.index_line_edit.returnPressed.connect(self.index_search_btn.click)
        self.line_edit.returnPressed.connect(self.search_button.click)
        Widgets.QShortcut(QKeySequence(Qt.CTRL+Qt.Key_L),self).activated.connect(
            lambda :self.line_edit.setFocus() or self.line_edit.selectAll())
        Widgets.QShortcut(QKeySequence.ZoomIn,self.view).activated.connect(self.zoomIn)
        Widgets.QShortcut(QKeySequence.ZoomOut,self.view).activated.connect(self.zoomOut)

    def show_help(self):
        msgBox=Widgets.QMessageBox()
        msgBox.setWindowTitle("Help")
        msgBox.setText('''
[ mmDict: yet another mdict client ]
Author: pangzaiyu@163.com

Keyboard shortcuts:
    Enter: Lookup/Search
    Alt+L/S/H/B: Lookup, Search, Help, Back
    Ctrl+L: focus input line edit
    j/k: Scroll down/up
    g: Back to top
    Ctrl+Plus/Minus: Zoom out/in

Acknowledgement:
    The mdict parse codes are from:
    https://bitbucket.org/xwang/mdict-analysis
    https://github.com/zhansliu/writemdict
    Great thanks to their work.
''')
        msgBox.exec()

    def __show_history(self,item):
        name = CurrentState.get_cur_dict()
        result_obj = SocketClient.lookup(item, [name])
        html = pretty_dict_result(name, result_obj.get(name, "No entry found"))
        self.page.setHtml(html, QUrl(f"{self.http_prefix}/{name}/"))

    def history_back(self):
        prev=CurrentState.get_prev_entry()
        if prev:
            self.__show_history(prev)

    def scrollDown(self):
        #cur_pos=self.view.page().scrollPosition()
        self.view.page().runJavaScript(f"window.scrollBy(0,50);", QWebEngineScript.ApplicationWorld)

    def scrollUp(self):
        self.view.page().runJavaScript(f"window.scrollBy(0,-50);", QWebEngineScript.ApplicationWorld)



    def zoomIn(self):
        self.zoom_factor+=.1
        self.page.setZoomFactor(self.zoom_factor)

    def zoomOut(self):
        self.zoom_factor-=.1
        self.page.setZoomFactor(self.zoom_factor)

    def switch_dict(self,cur_item):
        dict_name=cur_item.text()
        self.__show_definition(dict_name)

    def click_index_search(self,cur_item):
        self.line_edit.setText(cur_item.text())
        self.lookup()

    def __show_definition(self,dict_name):
        name,  value = CurrentState.get_definition(dict_name)
        CurrentState.reset_history()
        #self.page.setHtml(html,get_data_folder_url(data_folder))
        self.page.setHtml(pretty_dict_result(name, value), QUrl(f"{self.http_prefix}/{name}/"))
        CurrentState.add_history(CurrentState.word)
        self.view.page().runJavaScript("window.scrollTo(0,0);")

    def search_selected(self):
        text=self.page.selectedText().strip()
        if text:
            self.line_edit.setText(text)
            #self.__lookup(text)

    def __lookup(self,word):
        result_obj = SocketClient.lookup(word)
        CurrentState.reset(word, result_obj)
        self.__show_definition(None)

        avl_dicts = CurrentState.get_avl_dicts()
        self.dict_list_widget.clear()
        self.dict_list_widget.insertItems(0, avl_dicts)

    def lookup(self):
        word=self.line_edit.text().strip()
        if not word:
            return
        self.__lookup(word)


    def search_index(self):
        input=self.index_line_edit.text()
        dict_name = CurrentState.get_cur_dict()
        if not dict_name:
            self.index_search_items.clear()
            return
        all_words=SocketClient.search_word_index(dict_name,input)
        '''
        fzy=True
        try:
            subprocess.run(['which','fzy'],check=True)
        except subprocess.CalledProcessError:
            fzy=False

        if fzy:
            results=subprocess.run(['fzy','-e',input],input='\n'.join(all_words),
                                   check=True,text=True,capture_output=True).stdout.split('\n')
            results=results[:20]
        else:
            results=process.extract(input,all_words,limit=20)
            results=[item[0] for item in results]
        '''
        #results.sort(key=lambda x: x[1],reverse=True)
        self.index_search_items.clear()
        self.index_search_items.insertItems(0,all_words)


    def showMessage(self,msg):
        self.status_bar.showMessage(str(msg),4000)



