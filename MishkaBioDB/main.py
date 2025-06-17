import glob
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import BorderImage, Color, Rectangle, RenderContext, RoundedRectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.atlas import Atlas
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivy.storage.jsonstore import JsonStore
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from jsonvars import GlobalVars
from db import db
from Pages.Page1 import Page1
from Pages.EnterReg import EnterReg
from Pages.RegPage import RegPage
from Pages.LoadPage import LoadPage
from Pages.UserPage import UserPage
from Pages.HelpPage import HelpPage
from Pages.StudPage import StudPage
from Pages.LectPage import LectPage
from Pages.Modules import Modules
from Pages.Module1 import Module1
from Pages.LectModule import LectModule
from Pages.FillStudentsPage import FillStudentsPage
from Pages.GroupAccess import GroupAccess

class ModuleButtonLabel(ButtonBehavior, Label):
    markup = True
    halign = 'center'
    font_size = 19
    max_width = GlobalVars.all_max_width + 50  # максимальная ширина кнопки
    max_height = 78  # максимальная высота кнопки
    font_name = GlobalVars.Mtext_med
    multiline = True
    def __init__(self, **kwargs):
        super(ModuleButtonLabel, self).__init__(**kwargs)

        with self.canvas.before:
            Color(rgba=GlobalVars.dark_green)
            self.rect = RoundedRectangle(pos=self.pos, radius=[5,])
            self.bind(pos=self.schedule_update_rect, size=self.schedule_update_rect)

    def schedule_update_rect(self, instance, value):
        Clock.schedule_once(self.update_rect)
        
    def update_rect(self, dt):
        if self.rect.pos != self.pos or self.rect.size != self.size:
            self.rect.pos = self.pos
            self.rect.size = self.size

    def on_width(self, instance, value):
        if value > self.max_width:
            self.width = self.max_width

    def on_height(self, instance, value):
        if value > self.max_height:
            self.height = self.max_height

class ButtonLabelMed(ButtonBehavior, Label):
    markup = True
    halign = 'center'
    font_size = 24
    max_width = GlobalVars.all_max_width + 25
    max_height = 100
    font_name = GlobalVars.Mtext_reg
    def __init__(self, **kwargs):
        super(ButtonLabelMed, self).__init__(**kwargs)

        with self.canvas.before:
            Color(rgba=GlobalVars.dark_green)
            self.rect = RoundedRectangle(pos=self.pos, radius=[10,])
            self.bind(pos=self.schedule_update_rect, size=self.schedule_update_rect)

    def schedule_update_rect(self, instance, value):
        Clock.schedule_once(self.update_rect)
        
    def update_rect(self, dt):
        if self.rect.pos != self.pos or self.rect.size != self.size:
            self.rect.pos = self.pos
            self.rect.size = self.size

    def on_width(self, instance, value):
        if value > self.max_width:
            self.width = self.max_width

    def on_height(self, instance, value):
        if value > self.max_height:
            self.height = self.max_height

class ButtonLabel(ButtonBehavior, Label):
    markup = True
    halign = 'center'
    font_size = 21
    max_width = GlobalVars.all_max_width + 75
    max_height = 70
    font_name = GlobalVars.Mtext_semibold
    def __init__(self, **kwargs):
        super(ButtonLabel, self).__init__(**kwargs)

        with self.canvas.before:
            Color(rgba=GlobalVars.dark_green)
            self.rect = RoundedRectangle(pos=self.pos, radius=[10,])
            self.bind(pos=self.schedule_update_rect, size=self.schedule_update_rect)

    def schedule_update_rect(self, instance, value):
        Clock.schedule_once(self.update_rect)
        
    def update_rect(self, dt):
        if self.rect.pos != self.pos or self.rect.size != self.size:
            self.rect.pos = self.pos
            self.rect.size = self.size

    def on_width(self, instance, value):
        if value > self.max_width:
            self.width = self.max_width

    def on_height(self, instance, value):
        if value > self.max_height:
            self.height = self.max_height

class SmallButtonLabel(ButtonBehavior, Label):
    markup = True
    font_size = 20
    max_width = GlobalVars.all_max_width # максимальная ширина кнопки
    max_height = 80  # максимальная высота кнопки
    font_name = GlobalVars.Mtext_med
    color = GlobalVars.smoky_green
    def __init__(self, **kwargs):
        super(SmallButtonLabel, self).__init__(**kwargs)

        with self.canvas.before:
            Color(rgba=(0,0,0,0))
            self.rect = Rectangle(pos=self.pos)
            self.bind(pos=self.schedule_update_rect, size=self.schedule_update_rect)

    def schedule_update_rect(self, instance, value):
        Clock.schedule_once(self.update_rect)
        
    def update_rect(self, dt):
        if self.rect.pos != self.pos or self.rect.size != self.size:
            self.rect.pos = self.pos
            self.rect.size = self.size

    def on_width(self, instance, value):
        if value > self.max_width:
            self.width = self.max_width

    def on_height(self, instance, value):
        if value > self.max_height:
            self.height = self.max_height

class JustLabel(Label):
    markup=True
    text_size=(340, None)
    font_size=30
    halign='center'
    valign='bottom'
    max_width=GlobalVars.all_max_width
    max_height=80
    color=GlobalVars.dark_green
    font_name=GlobalVars.Mtext_semibold

    def __init__(self, **kwargs):
        super(JustLabel, self).__init__(**kwargs)

        with self.canvas.before:
            Color(rgba=GlobalVars.light_green)
            self.rect = RoundedRectangle(pos=self.pos, radius=[10, ])
            self.bind(pos=self.schedule_update_rect, size=self.schedule_update_rect)

    def schedule_update_rect(self, instance, value):
        Clock.schedule_once(self.update_rect)
        
    def update_rect(self, dt):
        if self.rect.pos != self.pos or self.rect.size != self.size:
            self.rect.pos = self.pos
            self.rect.size = self.size

    def on_width(self, instance, value):
        if value > self.max_width:
            self.width = self.max_width

    def on_height(self, instance, value):
        if value > self.max_height:
            self.height = self.max_height

class SmallLabel(Label):
    markup=True
    text_size=(300, None)
    font_size=17
    halign='left'
    valign='bottom'
    max_width=GlobalVars.all_max_width
    max_height=50
    color=GlobalVars.smoky_green
    font_name=GlobalVars.Mtext_med

    def __init__(self, **kwargs):
        super(SmallLabel, self).__init__(**kwargs)

        with self.canvas.before:
            Color(rgba=GlobalVars.light_green)
            self.rect = RoundedRectangle(pos=self.pos, radius=[10, ])
            self.bind(pos=self.schedule_update_rect, size=self.schedule_update_rect)

    def schedule_update_rect(self, instance, value):
        Clock.schedule_once(self.update_rect)
        
    def update_rect(self, dt):
        if self.rect.pos != self.pos or self.rect.size != self.size:
            self.rect.pos = self.pos
            self.rect.size = self.size

    def on_width(self, instance, value):
        if value > self.max_width:
            self.width = self.max_width

    def on_height(self, instance, value):
        if value > self.max_height:
            self.height = self.max_height

class HelpLabel(ButtonBehavior, Label):
    markup = True
    halign='left'
    font_size = 19
    max_width = GlobalVars.all_max_width
    max_height = 30
    font_name = GlobalVars.Mtext_reg
    color = GlobalVars.dark_red
    def __init__(self, **kwargs):
        super(HelpLabel, self).__init__(**kwargs)

        with self.canvas.before:
            Color(rgba=(0,0,0,0))
            self.rect = Rectangle(pos=self.pos)
            self.bind(pos=self.schedule_update_rect, size=self.schedule_update_rect)

    def schedule_update_rect(self, instance, value):
        Clock.schedule_once(self.update_rect)
        
    def update_rect(self, dt):
        if self.rect.pos != self.pos or self.rect.size != self.size:
            self.rect.pos = self.pos
            self.rect.size = self.size

    def on_width(self, instance, value):
        if value > self.max_width:
            self.width = self.max_width

    def on_height(self, instance, value):
        if value > self.max_height:
            self.height = self.max_height

class InfoLabel(Label):
    markup=True
    halign='left'
    text_size=(300, None)
    font_size=22
    max_width=GlobalVars.all_max_width
    max_height=80
    color=GlobalVars.dark_green
    font_name=GlobalVars.Mtext_reg

    def __init__(self, **kwargs):
        super(InfoLabel, self).__init__(**kwargs)

        with self.canvas.before:
            Color(rgba=(0,0,0,0))
            self.rect = RoundedRectangle(pos=self.pos, radius=[10, ])
            self.bind(pos=self.schedule_update_rect, size=self.schedule_update_rect)

    def schedule_update_rect(self, instance, value):
        Clock.schedule_once(self.update_rect)
        
    def update_rect(self, dt):
        if self.rect.pos != self.pos or self.rect.size != self.size:
            self.rect.pos = self.pos
            self.rect.size = self.size

    def on_width(self, instance, value):
        if value > self.max_width:
            self.width = self.max_width

    def on_height(self, instance, value):
        if value > self.max_height:
            self.height = self.max_height

class NameInfoLabel(Label):
    text_size=(300, None)
    font_size=26
    max_width=GlobalVars.all_max_width
    max_height=80
    color=GlobalVars.dark_green
    font_name=GlobalVars.Mtext_semibold

    def __init__(self, **kwargs):
        super(NameInfoLabel, self).__init__(**kwargs)

        with self.canvas.before:
            Color(rgba=(0,0,0,0))
            self.rect = RoundedRectangle(pos=self.pos, radius=[10, ])
            self.bind(pos=self.schedule_update_rect, size=self.schedule_update_rect)

    def schedule_update_rect(self, instance, value):
        Clock.schedule_once(self.update_rect)
        
    def update_rect(self, dt):
        if self.rect.pos != self.pos or self.rect.size != self.size:
            self.rect.pos = self.pos
            self.rect.size = self.size

    def on_width(self, instance, value):
        if value > self.max_width:
            self.width = self.max_width

    def on_height(self, instance, value):
        if value > self.max_height:
            self.height = self.max_height            

class RootScreen(ScreenManager):
    def acc_type_screen(self):
        if GlobalVars.type_acc == 1:
            self.current = 'stud'
        else:
            self.current = 'lect'

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #defie color scheme
        self.dark_green = GlobalVars.dark_green
        self.light_green = GlobalVars.light_green
        self.smoky_green = GlobalVars.smoky_green
        self.ghosty_green = GlobalVars.ghosty_green
        self.dark_red = GlobalVars.dark_red
        #define font
        self.Mtext_med = GlobalVars.Mtext_med
        self.Mtext_reg = GlobalVars.Mtext_reg
        self.Mtext_bold = GlobalVars.Mtext_bold
        self.Mtext_semibold = GlobalVars.Mtext_semibold
        #acc
        self.acc_type = GlobalVars.type_acc
        #dpi
        self.dpi = Window.dpi
    
        def start_dialog_OK(self, obj):
            self.dialog=MDDialog(
                md_bg_color=self.dark_green,
                text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Данные не сохранены. Пока![/font][/color]",
                buttons=[
                    MDFlatButton(
                        text="ОК",
                        md_bg_color='white',
                        theme_text_color="Custom",
                        font_name=GlobalVars.Mtext_bold,
                    
                    ),
                    MDFlatButton(
                        text="ЗАКРЫТЬ",
                        md_bg_color='white',
                        theme_text_color="Custom",
                        font_name=GlobalVars.Mtext_bold,
                        on_release=self.close_dialog,
                    ),
                ],
            )
            self.dialog.open()
        
        def start_dialog_YesNo(self, obj):
            self.dialog=MDDialog(
                md_bg_color=self.dark_green,
                text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Сохранить расчёты?[/font][/color]",
           
                buttons=[
                    MDFlatButton(
                        text="ДА",
                        md_bg_color='white',
                        theme_text_color="Custom",
                        font_name=GlobalVars.Mtext_bold,
                    ),
                    MDFlatButton(
                        text="НЕТ",
                        md_bg_color='white',
                        theme_text_color="Custom",
                        font_name=GlobalVars.Mtext_bold,
                    ),
                    MDFlatButton(
                        text="ЗАКРЫТЬ",
                        md_bg_color='white',
                        theme_text_color="Custom",
                        font_name=GlobalVars.Mtext_bold,
                        on_release=self.close_dialog,
                    ),
                ],
            )
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        
    Window.size = (360, 800)
    def build(self):
        self.theme_cls.primary_palette = 'BlueGray'
        return RootScreen()

if __name__ == "__main__":
    MainApp().run()