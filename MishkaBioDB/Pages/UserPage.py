from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from jsonvars import GlobalVars

class UserPage(Screen):
    def on_enter(self):
        if not(GlobalVars.readuser()):
            GlobalVars.flag_acc = 1
        if (GlobalVars.flag_acc == 1):
            self.ids.last_name.text = "Гостевой аккаунт"
            self.ids.info_1.text = "Вы не сможете сохранить результаты работы модулей"
            self.ids.info_2.text = ""
            self.ids.info_3.text = "Вам доступны незакрытые модули"
        else:
            self.ids.last_name.text = GlobalVars.last_name
            self.ids.info_1.text = "Вы можете сохранять результаты работы модулей"
            self.ids.info_2.text = ""
            self.ids.info_3.text = "У вас есть недоступные модули, закрытые преподавателем"
            
    def on_btn_exit(self):
        self.start_dialog_OK(self)

    def start_dialog_OK(self, obj):
        self.dialog=MDDialog(
            md_bg_color=GlobalVars.dark_green,
            text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Вы уверены, что хотите выйти из аккаунта?\n[/font]Нажатие на кнопку 'Да' вернёт вас на окно входа[/color]",
            buttons=[
                MDFlatButton(
                    text="ДА", md_bg_color='white',
                    theme_text_color="Custom", font_name=GlobalVars.Mtext_bold,
                    on_release=self.gotoreg,
                ),
                MDFlatButton(
                    text="НЕТ",  md_bg_color='white',
                    theme_text_color="Custom", font_name=GlobalVars.Mtext_bold,
                    on_release=self.close_dialog,
                ),
            ],
        )
        self.dialog.open()
        
    def close_dialog(self, obj):
        self.dialog.dismiss()
        
    def gotoreg(self, obj):
        self.close_dialog(self)
        GlobalVars.makeaccnull()
        GlobalVars.writeuser()
        self.manager.current = 'enterreg'