from kivy.uix.screenmanager import Screen
from jsonvars import GlobalVars
from db import db

class LectPage(Screen): #экран преподавателя
    def on_enter(self):
        if db.isc:
            self.ids.btn_manage.disabled = False
