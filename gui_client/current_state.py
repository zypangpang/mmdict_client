
class CurrentState():
    word=None
    dict_names=[]
    cur_dict_name=None
    history=[]
    result_obj={}

    @classmethod
    def set_dict_infos(cls,dicts):
        cls.dict_names=dicts
        cls.cur_dict_name=cls.dict_names[0]

    @classmethod
    def reset(cls,word,result_obj):
        cls.word=word
        cls.result_obj=result_obj
        cls.history=[]
        avl_dicts=cls.get_avl_dicts()
        if not avl_dicts:
            cls.cur_dict_name=None
        else:
            cls.cur_dict_name=avl_dicts[0]

    @classmethod
    def reset_history(cls):
        cls.history=[]

    @classmethod
    def get_avl_dicts(cls):
        #ans=[]
        #for name in cls.dict_names:
        #    if name in cls.result_obj:
        #        ans.append(name)
        #return ans
        return list(cls.result_obj.keys())

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

        return cls.cur_dict_name,cls.result_obj.get(cls.cur_dict_name,"No entry found")


    @classmethod
    def set_cur_dict(cls,name):
        cls.cur_dict_name=name

    @classmethod
    def get_cur_dict(cls):
        return cls.cur_dict_name

