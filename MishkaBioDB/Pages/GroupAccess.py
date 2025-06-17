from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from jsonvars import GlobalVars
from db import db
class CustomDropDown(DropDown):
    pass

class GroupAccess(Screen): #модуль студентов
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown_groups = DropDown()
        self.dropdown_modules = DropDown()
        
    def on_enter(self):
        self.ids.btn_groups.text = ''
        self.ids.btn_modules.text = ''        

    def dropdown_groups_click(self):
        self.dropdown_groups.clear_widgets()        
        data = db.find_groups()
        for item in data:
            btn = Button(text=item, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.select_item_g(btn.text))
            self.dropdown_groups.add_widget(btn)
        self.dropdown_groups.open(self.ids.btn_groups)

    def select_item_g(self, text):
        self.ids.btn_groups.text = text
        self.dropdown_groups.dismiss()
        
    def dropdown_modules_click(self):
        self.dropdown_modules.clear_widgets()        
        data = db.find_modules()
        for item in data:
            btn = Button(text=item, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.select_item_m(btn.text))
            self.dropdown_modules.add_widget(btn)
        self.dropdown_modules.open(self.ids.btn_modules)

    def select_item_m(self, text):
        self.ids.btn_modules.text = text
        self.dropdown_modules.dismiss()        
        if (len(self.ids.btn_groups.text) > 2 and len(self.ids.btn_modules.text) > 2):
            mod_state = db.check_state([self.ids.btn_groups.text, self.ids.btn_modules.text])
            if mod_state:
                self.ids.btn1.state = 'normal'
                self.ids.btn2.state = 'down'
            else:
                self.ids.btn1.state = 'down'
                self.ids.btn2.state = 'normal'
        self.ids.btn1.disabled = False
        self.ids.btn2.disabled = False

    def toggle(self, *args, **kwargs):
        if kwargs['i'] == 1:           
            self.ids.btn1.state = 'down'
            self.ids.btn2.state = 'normal'
        if kwargs['i'] == 2:           
            self.ids.btn1.state = 'normal'
            self.ids.btn2.state = 'down'
        
    def start_dialog_OK(self, obj):
        new_state = None
        if self.ids.btn1.state == 'down':
            new_state = 0
        else:
            new_state = 1        
        db.change_state([self.ids.btn_groups.text, self.ids.btn_modules.text, new_state])        
        self.dialog=MDDialog(
            md_bg_color=GlobalVars.dark_green,
            text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Сохранение данных\n[/font]Изменения сохранены удачно[/color]",
            buttons=[
                MDFlatButton(
                    text="Закрыть", md_bg_color='white',
                    theme_text_color="Custom", font_name=GlobalVars.Mtext_bold,
                    on_release=self.close_dialog),
            ],
        )
        self.dialog.open()
        
    def close_dialog(self, obj):
        self.dialog.dismiss()
        self.manager.current = 'lectModules'