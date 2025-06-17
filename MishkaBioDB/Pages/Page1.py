from kivy.uix.screenmanager import Screen
from jsonvars import GlobalVars

class Page1(Screen): #стартовая страница
    def on_enter(self):        
        if not(GlobalVars.readuser()):
            GlobalVars.flag_acc = 1