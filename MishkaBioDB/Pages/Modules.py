from kivy.uix.screenmanager import Screen
from jsonvars import GlobalVars
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from db import db


class Modules(Screen): #экран модулей
    def on_enter(self):        
        btns = [self.ids.btn_mod_1, self.ids.btn_mod_2, self.ids.btn_mod_3, self.ids.btn_mod_4, self.ids.btn_mod_5]
        if db.isc:        
            GlobalVars.modules = db.find_modules()
            db_access = db.find_modules_access([GlobalVars.last_name])
            if db_access:
                GlobalVars.mod_access = db_access
                GlobalVars.writemodules()        
        GlobalVars.readmodules()
        modules = GlobalVars.modules
        access = GlobalVars.mod_access        
        print("modules", modules)
        print("access", access)
        if (len(modules) < 1):
            self.start_dialog_Error(self)
        else:
            for i in range(len(modules)):
                btns[i].text = modules[i]
                if access[i] == 1:
                    btns[i].disabled = False
                else:
                    btns[i].disabled = True      
            if GlobalVars.mod_access[0] == 0:
                self.start_dialog_OK(self)
            
            
    def start_dialog_OK(self, obj):
        self.dialog=MDDialog(
            md_bg_color=GlobalVars.dark_green,
            text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Доступ к модулям[/font]\nЗакрыт преподавателем[/color]",
            buttons=[
                MDFlatButton(
                    text="ОК", md_bg_color='white', theme_text_color="Custom", font_name=GlobalVars.Mtext_bold,on_release=self.close_dialog,),
            ],
        )
        self.dialog.open()
        

    def start_dialog_Error(self, obj):
        self.dialog=MDDialog(
            md_bg_color=GlobalVars.dark_green,
            text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Доступ к модулям[/font]\nНедоступен в первый раз. Зайдите с подключением к интернету.[/color]",
            buttons=[
                MDFlatButton(
                    text="ОК", md_bg_color='white', theme_text_color="Custom", font_name=GlobalVars.Mtext_bold,on_release=self.close_dialog,),
            ],
        )
        self.dialog.open()
        

    def close_dialog(self, obj):
        self.dialog.dismiss()
        
    def choose_module(self, *args, **kwargs):
        result = Builder.load_string(db.load_module(kwargs['i'])) 
        ##по итогам работы модуля будет возвращаться массив итогов, который с помощью приложения переносится в базу данных##
        GlobalVars.writelocalsession() # записываются данные локальной сессии
        GlobalVars.makenull() # обнуляются для новой сесии