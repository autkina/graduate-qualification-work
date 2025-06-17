from transliterate import translit
import hashlib
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen
from jsonvars import GlobalVars
from db import db
class FillStudentsPage(Screen): #модуль студентов
    
    def InsertUserLogin(self, data):
      name = data.split(' ')
      if (len(name[0]) > 0):
        login = translit(name[0], language_code='ru', reversed=True).replace("'", '')
        sha = hashlib.sha1(login.encode()).hexdigest()
        passw = sha[:8]
        login = f'{login}{sha[9:11]}'
        res_login = db.insert_stdnt([login, passw])
        self.ids.students_list.text += f'Логин: {res_login} Пароль: {passw}\n'
        db.grp_stdn([self.ids.group_name.text, res_login])
        
    def on_group_of_students(self):
        std_list = self.ids.students_list.text
        grp_name = self.ids.group_name.text
        if self.ids.btn_send.text == 'ОТПРАВИТЬ':
            if len(grp_name) > 0:
               db.insert_grp([GlobalVars.key_acc, grp_name])
            self.ids.students_list.text = ''
            if (std_list[0].isdigit()):  #код для текста, когда есть числа #'1\tПетров А.А.\n'         
              student_lines = std_list.split('\n') #каждая строка - отдельный объект
              for student in student_lines:
                like_split = student.split('\t')
                if (len(like_split) > 1):
                  self.InsertUserLogin(like_split[1])
            else: #код для текста, когда чисел нет #'Петров А.А.\n'
              student_lines = std_list.split('\n')
              for student in student_lines:
                self.InsertUserLogin(student)
            self.start_dialog_close(self)
        else:
            self.manager.current = 'lectModules'
            

    def start_dialog_close(self, obj):
        self.dialog=MDDialog(
            md_bg_color=GlobalVars.dark_green,
            text="[color=#ffffff][font=MTest/Montserrat-Bold.ttf]Группа создана\n[/font]Скопируйте полученный список и отправьте студентам[/color]",
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
        self.ids.btn_send.text = 'ВЫЙТИ'
        self.dialog.dismiss()
        
    def on_leave(self):
       if self.ids.btn_send.text == 'ВЫЙТИ':
         self.ids.students_list.text = ''
         self.ids.group_name.text = ''       

          