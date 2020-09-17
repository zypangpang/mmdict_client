from PyQt5.QtCore import pyqtSignal, QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from .work_thread import LookupThread
from .current_state import CurrentState
from .gui_utils import pretty_dict_result,ProgressDialog,httpPlaySound


class MyWebPage(QWebEnginePage):
    play_sound_error_sig=pyqtSignal(str)
    search_all=pyqtSignal(str)

    def __init__(self,parent=None):
        super().__init__(parent)
        self.lookupThread=LookupThread()
        self.lookupThread.result_ready.connect(self.show_result)

    def show_result(self,word,result_obj):
        dict_name = CurrentState.get_cur_dict()
        raw_html = pretty_dict_result(dict_name, result_obj['results'].get(dict_name, "No entry found"))
        # except Exception as e:
        #    print(f"Lookup {item} error = {e}")
        #    return False
        # print(self.url())
        self.setHtml(raw_html, self.url())
        CurrentState.add_history(word)
        ProgressDialog.hide_progress()

    #text_selected=pyqtSignal(str)
    def acceptNavigationRequest(self, url: QUrl, type: QWebEnginePage.NavigationType, isMainFrame: bool, **kwargs):
        if type == QWebEnginePage.NavigationTypeLinkClicked:
            if url.scheme() == 'entry':
                try:
                    _, item = url.toString().split(":")
                except:
                    return False
                ProgressDialog.show_progress(self.parent(),"Loading...")
                item = item.strip("/ ")
                if CurrentState.is_no_entry_state():
                    self.search_all.emit(item)
                    return False

                dict_name=CurrentState.get_cur_dict()
                self.lookupThread.word=item
                self.lookupThread.dicts=[dict_name]
                self.lookupThread.start()
                #dict_name=CurrentState.get_cur_dict()
                #try:
                #result_obj: dict = SocketClient.lookup(item,[dict_name])
                #raw_html = pretty_dict_result(dict_name,result_obj.get(dict_name,"No entry found"))
                #except Exception as e:
                #    print(f"Lookup {item} error = {e}")
                #    return False
                #print(self.url())
                #self.setHtml(raw_html,self.url())
                #CurrentState.add_history(item)

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

