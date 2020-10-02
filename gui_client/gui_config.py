import configparser,os,copy
from pathlib import Path

CONFIG_SECTION='gui client'
PROGRAM_SECTION='internal settings DO NOT MODIFY'

class GuiConfigs():
    DICT_HOST = "dict host"
    # DICT_HOST="localhost"

    DICT_PORT = "dict port"

    #HTTP_SCHEME = "dict scheme"
    HTTP_HOST = "http host"
    HTTP_PORT = "http port"

    SOUND_PLAYER = 'sound player'

    ZOOM_FACTOR='zoom factor'

    @classmethod
    def check_config_file(cls,file_path):
        return os.path.exists(file_path)

    @classmethod
    def generate_init_configs(cls,file_path):
        #index_folder = DEFAULT_CONFIG_PATH.parent.joinpath("index")
        configs = configparser.ConfigParser()
        configs[CONFIG_SECTION] = {
            cls.DICT_HOST: 'localhost',
            cls.DICT_PORT: 9999,
            cls.HTTP_HOST: "localhost",
            cls.HTTP_PORT: 8000,
            cls.SOUND_PLAYER:"mpv",
        }
        #configs[PROGRAM_SECTION] = {
        #    cls.ZOOM_FACTOR : 1.0,
        #}
        with open(file_path, "w") as f:
            configs.write(f)
        return file_path

    def __init__(self,file_path):
        self.config_path=file_path
        self.config=configparser.ConfigParser()
        self.config.read(file_path)
        self.ori_config=copy.deepcopy(self.config)

    def save(self):
        with open(self.config_path, "w") as f:
            self.ori_config.write(f)

    def get_dict_server(self):
        host,port=self.config[CONFIG_SECTION].get(self.DICT_HOST), self.config[CONFIG_SECTION].get(self.DICT_PORT)
        if host and port:
            return host,int(port)
        else:
            raise Exception("Dict host or port is not set.")

    def get_http_server(self):
        host,port=self.config[CONFIG_SECTION].get(self.HTTP_HOST), self.config[CONFIG_SECTION].get(self.HTTP_PORT)
        if host and port:
            return host,int(port)
        else:
            raise Exception("Http host or port is not set.")

    def get_sound_player(self):
        return self.config[CONFIG_SECTION].get(self.SOUND_PLAYER,'mpv')

    def set_value(self,key,value):
        self.config[CONFIG_SECTION][key]=value

    def set_zoom_factor(self,val):
        try:
            self.config[PROGRAM_SECTION][self.ZOOM_FACTOR]=val
        except:
            self.config[PROGRAM_SECTION]={
                self.ZOOM_FACTOR:val
            }

        try:
            self.ori_config[PROGRAM_SECTION][self.ZOOM_FACTOR]=val
        except:
            self.ori_config[PROGRAM_SECTION]={
                self.ZOOM_FACTOR:val
            }


    def get_zoom_factor(self):
        try:
            return float(self.config[PROGRAM_SECTION][self.ZOOM_FACTOR])
        except:
            return 1.0


#def set_dicts(self,dicts:dict):
    #    #dict_names=[Path(x).stem for x in dict_paths]
    ##    self.config[CONFIG_DAEMON_SECTION][self.DICT_FILED]=','.join(dicts.values())
    #    self.config[CONFIG_DAEMON_SECTION][self.ENABLED_FILED]=','.join(dicts.keys())
    #    with open(self.config_path,"w") as f:
    #        self.config.write(f)
    #    return dicts.keys()

    #def add_dict(self,dict_path):
    #    dict_name=Path(dict_path).stem
    #    self.config[CONFIG_DAEMON_SECTION][self.DICT_FILED]+=f",{dict_path}"
    #    self.config[CONFIG_DAEMON_SECTION][self.ENABLED_FILED]+=f",{dict_name}"
    #    with open(self.config_path,"w") as f:
    #        self.config.write(f)
    #    return dict_name


    #def get_section(self,section_name):
    #    if section_name in self.config.sections():
    #        return self.config[section_name]
    #    raise Exception(f"No config section {section_name}")

    #def get_value(self, section, key):
    #    return self.config[section][key]

    #def get_daemon_value(self, key):
    #    return self.config[CONFIG_DAEMON_SECTION][key]

    #def get_frontend_value(self, key):
    #    return self.config[CONFIG_FRONTEND_SECTION][key]

    #def get_dictionary_paths(self):
    #    dicts = self.get_value("dictionary daemon", "dictionaries").split(",")
    ##    dicts=[x.strip() for x in dicts]
    #    index_folder=Path(self.get_daemon_value("index folder"))
    #    ans={}
    #    for path in dicts:
    #        path=Path(path)
    #        name=path.stem
    #        data_folder=str(index_folder.joinpath(name))
    #        ans[name]=[str(path),data_folder]
    #    return ans


    #def get_enabled_dicts(self):
    #    try:
    #        dicts=self.get_daemon_value("enabled dictionaries")
    #    except Exception as e:
    #        return []
    #    return [x.strip() for x in dicts.split(',')] if dicts else []



if __name__ == '__main__':
    pass
