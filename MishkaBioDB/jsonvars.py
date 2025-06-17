from kivy.storage.jsonstore import JsonStore
from datetime import datetime

class GlobalVars:
    flag_acc = 1 #флаг пользователя: 1 - гость, 2 - авторизован
    key_acc = 0 #ID пользователя
    type_acc = 1 #тип пользователя
    last_name = "" #имя пользователя
    modules = [] #массив модулей
    mod_access = [] #массив состояний доступа к модулю
    key_mod = 1 #ID модуля
    name_mod = "" #наименование модуля
    soil_value = "" #значение почвы
    key_mod_meas = 0 #ID замера в модуле
    key_sel = 0 #ID выборки
    name_meas = "" #пользовательское наименование замера
    datetime_meass = "" #дата и время замера
    name_feats = [] #массив имён проверяемых параметров
    scores = [] #массив значений проверяемых параметров
    session_count = 1 #номер сессии
    
    Mtext_med = 'MTest/Montserrat-Medium.ttf'
    Mtext_reg = 'MTest/Montserrat-Regular.ttf'
    Mtext_bold = 'MTest/Montserrat-Bold.ttf'
    Mtext_semibold = 'MTest/Montserrat-SemiBold.ttf'
    dark_green = (44/255, 57/255, 57/255, 1)
    light_green = (221/255, 230/255, 217/255, 1)
    smoky_green = (156/255, 163/255, 154/255, 1)
    ghosty_green = (219/255, 231/255, 216/255, 1)
    dark_red = (127/255, 13/255, 0/255, 1)
    all_max_width = 360 * 0.8
    all_max_height = 800 * 0.8
    
    @classmethod    
    def writelocalsession(cls): 
        today = datetime.now().strftime("%Y-%m-%d") #сегодняшняя дата
        jstorename = (f'{today}_{cls.session_count}.json') #имя генерируемого json-файла
        store = JsonStore(jstorename)
        store.put("start", key_mod=cls.key_mod,name_mod=cls.name_mod,
                  soil_value=cls.soil_value,key_mod_meas=cls.key_mod_meas,key_sel=cls.key_sel,
                  name_meas=cls.name_meas,datetime_meass=datetime.now().strftime("%d.%m.%Y"),
                  name_feats=cls.name_feats, scores=cls.scores)
        cls.session_count = cls.session_count + 1
        
    @classmethod    
    def writeuser(cls): 
        store = JsonStore('userinfo.json')
        store.put("you", flag_acc=cls.flag_acc,key_acc=cls.key_acc,type_acc=cls.type_acc,last_name=cls.last_name)
        
    @classmethod    
    def readuser(cls): 
        store = JsonStore('userinfo.json')
        if store.exists('you'):
            cls.flag_acc = store.get('you')['flag_acc']
            cls.last_name = store.get('you')['last_name']
            cls.type_acc = store.get('you')['type_acc']
            print(cls.flag_acc, cls.last_name, cls.type_acc)
            return True
        else:
            return False

    @classmethod    
    def writemodules(cls): 
        store = JsonStore('modinfo.json')
        store.put("access", modules=cls.modules,mod_access=cls.mod_access)
        
    @classmethod    
    def readmodules(cls): 
        store = JsonStore('modinfo.json')
        if store.exists('access'):
            cls.modules = store.get('access')['modules']
            cls.mod_access = store.get('access')['mod_access']

    @classmethod    
    def makeaccnull(cls):
        cls.flag_acc = 1
        cls.key_acc = 0
        cls.type_acc = 0
        cls.last_name = ""
        
    @classmethod    
    def makenull(cls): 
        cls.key_mod = 1
        cls.name_mod = ""
        cls.soil_value = ""
        cls.key_mod_meas = 0
        cls.key_sel = 0
        cls.name_meas = ""
        cls.datetime_meass = "" 
        cls.key_meass = []
        cls.name_feats = []
        cls.scores = []
        cls.session_count = 1