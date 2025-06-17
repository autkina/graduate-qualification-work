from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from jsonvars import GlobalVars
from db import db

class EnterReg(Screen): #экран входа
    def on_enter(self):
        GlobalVars.makeaccnull()
        GlobalVars.writeuser()
        
    def on_validation(self):
        login = self.ids.input_login.text
        passw = self.ids.input_passw.text
        print(login, passw)
        if (len(login) > 2 and not(' ' in login)):
            if (len(passw) > 7):
                self.on_db_enter([login, passw])
            else:
                self.start_dialog_close_err(self)
        else:
            self.start_dialog_close_err(self)
                    
    def on_db_enter(self, data):
        a_id = db.find_stdnt(data)
        if (a_id):
            GlobalVars.flag_acc = 2
            GlobalVars.key_acc = a_id[0]
            GlobalVars.type_acc = a_id[1]
            GlobalVars.last_name = data[0]
            GlobalVars.writeuser()
            if (GlobalVars.type_acc < 2):
                self.manager.current = 'stud'
            else:
                self.manager.current = 'lect'
        else:
            self.start_dialog_close(self)                       
            
    def on_guest(self):
        GlobalVars.makeaccnull()
        GlobalVars.writeuser()
        self.manager.current = 'user'
        
    def forget_password(self):
        self.start_dialog_OK(self)


    def start_dialog_close_err(self, obj):
        self.dialog=MDDialog(
            md_bg_color=GlobalVars.dark_green,
            text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Ошибка\n[/font]Пожалуйста, заполните поля более чем 2 символами[/color]",
            buttons=[
                MDFlatButton(
                    text="Закрыть",  md_bg_color='white',
                    theme_text_color="Custom", font_name=GlobalVars.Mtext_bold,
                    on_release=self.close_dialog,
                ),
            ],
        )
        self.dialog.open()
        
    def start_dialog_OK(self, obj):
        self.dialog=MDDialog(
            md_bg_color=GlobalVars.dark_green,
            text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Отправим пароль на вашу почту\n[/font]При смене почты свяжитесь с кафедрой для восстановления пароля[/color]",
            buttons=[
                MDFlatButton(
                    text="Отправить пароль",  md_bg_color='white',
                    theme_text_color="Custom", font_name=GlobalVars.Mtext_bold,
                    on_release=self.close_dialog,
                    
                ),
                MDFlatButton(
                    text="Закрыть",  md_bg_color='white',
                    theme_text_color="Custom", font_name=GlobalVars.Mtext_bold,
                    on_release=self.close_dialog,
                ),
            ],
        )
        self.dialog.open()
        
    def start_dialog_close(self, obj):
        self.dialog=MDDialog(
            md_bg_color=GlobalVars.dark_green,
            text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Аккаунт не найден\n[/font]Попробуйте ещё раз[/color]",
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