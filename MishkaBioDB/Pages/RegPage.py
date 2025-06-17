from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from jsonvars import GlobalVars
from db import db

class RegPage(Screen): #регистрация
    def on_validation(self):
        login = self.ids.input_login.text
        passw = self.ids.input_passw.text
        c_passw = self.ids.copy_passw.text
        if (len(login) > 2 and not(' ' in login)):
            if (len(passw) > 7):
                if passw == c_passw:
                    self.on_db_enter([login, passw])
                else:
                    self.start_dialog_close_err(self)  
            else:
                self.start_dialog_close_err(self)
        else:
            self.start_dialog_close_err(self)
                    
    def on_db_enter(self, data):
        print('on_db_enter')
        a_id = db.find_stdnt(data)
        if (a_id):
           self.start_dialog_close_reg_error(self)
        else:
            self.start_dialog_close_good(self)
            self.manager.current = 'user'
        
    def start_dialog_close_err(self, obj):
        self.dialog=MDDialog(
            md_bg_color=GlobalVars.dark_green,
            text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Ошибка\n[/font]Пожалуйста, заполните поля более чем 2 символами и проверьте пароли[/color]",
            buttons=[
                MDFlatButton(
                    text="Закрыть",  md_bg_color='white',
                    theme_text_color="Custom", font_name=GlobalVars.Mtext_bold,
                    on_release=self.close_dialog,
                ),
            ],
        )
        self.dialog.open()

    def start_dialog_close_reg_error(self, obj):
        self.dialog=MDDialog(
            md_bg_color=GlobalVars.dark_green,
            text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Аккаунт уже зарегистрирован[/font][/color]",
            buttons=[
                MDFlatButton(
                    text="Закрыть",  md_bg_color='white',
                    theme_text_color="Custom", font_name=GlobalVars.Mtext_bold,
                    on_release=self.close_dialog,
                ),
            ],
        )
        self.dialog.open()
        
    def start_dialog_close_good(self, obj):
        self.dialog=MDDialog(
            md_bg_color=GlobalVars.dark_green,
            text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Запрос направлен\n[/font]После принятия запроса вы сможете войти в аккаунт.\nОсуществляем вход в гостевой аккаунт[/color]",
            buttons=[
                MDFlatButton(
                    text="Закрыть",  md_bg_color='white',
                    theme_text_color="Custom", font_name=GlobalVars.Mtext_bold,
                    on_release=self.close_dialog,
                ),
            ],
        )
        self.dialog.open()        
        
    def close_dialog(self, obj):
        self.dialog.dismiss()