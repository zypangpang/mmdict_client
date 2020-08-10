from gui_client.socket_client import SocketClient
import fire
from constants import FRONT_END
SocketClient.front_end=FRONT_END.CONSOLE

class Main():
    __dicts = SocketClient.list_dicts()
    __dict_names = [dict[0] for dict in __dicts]

    @classmethod
    def list_dicts(cls):
        output=[f"{i}: "+dict for i,dict in enumerate(cls.__dict_names)]
        print("\n".join(output))

    @classmethod
    def list_words(cls,dict_index=0):
        name=cls.__dict_names[dict_index]
        word_list=SocketClient.list_words(name)
        print("\n".join(word_list))

    @classmethod
    def lookup(cls,word,raw=False,dicts=None):
        if dicts:
            dicts=[dicts] if not isinstance(dicts,list) else dicts
            dicts=[cls.__dict_names[i] for i in dicts]
        result_obj=SocketClient.lookup(word,dicts,raw)
        for dict, value in result_obj.items():
            print(f"\033[1m<{dict}>\033[0m")
            print(value)



if __name__ == '__main__':
    fire.Fire(Main)



