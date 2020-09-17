import socket,json,constants
from bs4 import BeautifulSoup
from constants import FRONT_END
import configs


class SocketClient():
    front_end=FRONT_END.QTWEBENGINE
    @classmethod
    def __request(cls,data):
        if configs.DICT_HOST=='unix':
            return cls.__request_unix(data)
        else:
            return cls.__request_inet(data)

    @classmethod
    def __request_unix(cls, data):
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            sock.connect(constants.SOCKET_LOCATION)
            sock.sendall(data.encode("utf-8"))
            msg_list = []
            while True:
                msg = sock.recv(8192)
                if not msg:
                    break
                msg_list.append(msg)
        return b"".join(msg_list).decode("utf-8")

    @classmethod
    def __request_inet(cls,data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((configs.DICT_HOST,configs.DICT_PORT))
            sock.sendall(data.encode("utf-8"))
            msg_list = []
            while True:
                msg = sock.recv(8192)
                if not msg:
                    break
                msg_list.append(msg)
        return b"".join(msg_list).decode("utf-8")
    @classmethod
    def __assemble_cmd(cls,command,**kwargs):
        return json.dumps({
            "command":command,
            "kwargs":kwargs
        })

    @classmethod
    def __general_tweak(cls,result_obj):
        for key,val in result_obj.items():
            if val.startswith("@@@LINK="):
                word=val[8:].strip()
                entry=f'<A href="entry://{word}">{word}</A>'
                result_obj[key]=f"SEE: {entry}"

    @classmethod
    def __tweak_for_qt_webengine(cls,result_obj):
        for key,val in result_obj.items():
            soup=BeautifulSoup(val,"lxml")
            all_a=soup.find_all("a")
            for a in all_a:
                if " " in a.get('href',""):
                    a['href']=a['href'].replace("://",":")
            result_obj[key]=str(soup)
        return result_obj

    @classmethod
    def __tweak_for_console(cls, result_obj):
        for key,val in result_obj.items():
            soup=BeautifulSoup(val,"lxml")
            result_obj[key]=soup.text
        return result_obj

    @classmethod
    def lookup(cls,word,dicts=None,raw=False):
        data=cls.__assemble_cmd("Lookup",word=word,dicts=dicts) if dicts else cls.__assemble_cmd("Lookup",word=word)
            #data=data+","+','.join(dicts)
        recv_data=cls.__request(data)
        return_obj=json.loads(recv_data)
        if return_obj['status_code'] == 1:
            return return_obj
        #print(r_obj['USE THE RIGHT WORD'])
        if raw:
            return return_obj

        r_obj=return_obj['results']
        #cls.__general_tweak(r_obj)
        if cls.front_end==FRONT_END.QTWEBENGINE:
            return_obj['results']=cls.__tweak_for_qt_webengine(r_obj)
        elif cls.front_end==FRONT_END.CONSOLE:
            return_obj['results']=cls.__tweak_for_console(r_obj)

        return return_obj


    @classmethod
    def list_dicts(cls,enabled=True):
        #data=f"ListDicts:{int(enabled)}"
        data=cls.__assemble_cmd("ListDicts",enabled=enabled)
        return json.loads(cls.__request(data))

    @classmethod
    def search_word_index(cls,dict_name,word):
        #data=f"ListWord:{dict_name.strip()},{word.strip()}"
        data=cls.__assemble_cmd("ListWord",dict_name=dict_name.strip(),word=word.strip())
        return json.loads(cls.__request(data))

    @classmethod
    def test(cls):
        data="Test"
        return cls.__request(data)




if __name__ == '__main__':
    pass


