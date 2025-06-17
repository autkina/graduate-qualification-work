from kivy.properties import NumericProperty, ObjectProperty
from kivy.animation import Animation
from kivy.clock import Clock
import threading
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from db import db
from jsonvars import GlobalVars


class LoadPage(Screen): #экран загрузки
    angle = NumericProperty(0)
    anim = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_angle(self, item, angle):
        if angle == -360:
            item.angle = 0

    def stop_animation(self):
        self.anim.repeat = not(self.anim.repeat)
        if (self.anim.repeat):
            self.anim.start(self)
        else:
            self.anim.stop(self)
    def gotowww(self, obj):
        GlobalVars.readuser()
        print(GlobalVars.flag_acc)
        if GlobalVars.flag_acc == 1:
            self.manager.current = 'enterreg'
        else:
            self.gotolocal(self)
        
    def gotolocal(self, obj):
        self.manager.current = 'user'
        
    def on_enter(self):
        self.anim = Animation(angle=-360, duration=2)
        self.anim += Animation(angle=-360, duration=2)
        self.anim.repeat = True
        self.anim.start(self)
        threading.Thread(target=self.connect_to_db, daemon=True).start()
        
    def connect_to_db(self):
        try:
            dbconn = db.connect()
            if dbconn:
                connected = True
            else:
                connected = False
                print("Подключение не удалось [1]. Желаете попробовать ещё раз?")
        except Exception as e:
            connected = False
            print("Подключение не удалось [2]. Желаете попробовать ещё раз?")
        if connected:
            self.stop_animation()
            Clock.schedule_once(self.gotowww)
        else:
            connected = False
            print("Подключение не удалось [3]. Желаете попробовать ещё раз?")
            Clock.schedule_once(self.start_dialog_OK)
        
    def start_dialog_OK(self, obj):
        self.dialog=MDDialog(
            md_bg_color=GlobalVars.dark_green,
            text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Соединение не установлено[/font] Работа в локальном режиме[/color]",
            buttons=[
                MDFlatButton(
                    text="ОК", md_bg_color='white', theme_text_color="Custom", font_name=GlobalVars.Mtext_bold,on_release=self.close_dialog,),
            ],
        )
        self.dialog.open()
        
    def close_dialog(self, obj):
        self.dialog.dismiss()
        GlobalVars.flag_acc = 1
        self.gotolocal(self)