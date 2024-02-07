from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, WipeTransition, FadeTransition
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivy.core.text import LabelBase
import mysql.connector
Window.size = (1100, 650)
connection = mysql.connector.connect(
    user='root',
    password='Asecna2024',
    host='localhost',
    database='login')

mycursor = connection.cursor()


class MainApp(MDApp):

    """def on_start(self):
        mycursor.execute("SELECT COUNT(user) FROM entry")
        result = mycursor.fetchone()
        print(result[0])
        if result[0] == 0:
            self.root.current = "Test"
        else:
            self.root.current = "login" """

    def build(self):
        self.icon = "Logo.png"
        self.title = "Manamboatra"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Lime"
        screen = ScreenManager()
        screen.transition.duration = .5
        screen.add_widget(Builder.load_file("equip.kv"))
        screen.add_widget(Builder.load_file('login.kv'))
        screen.add_widget(Builder.load_file('Test.kv'))
        screen.add_widget(Builder.load_file("Chip.kv"))
        screen.add_widget(Builder.load_file("Choice.kv"))
        return screen

    def logger(self):
        user_input = self.root.get_screen('login').ids.user.text
        password_input = self.root.get_screen('login').ids.password.text

        get_user = "SELECT user FROM entry "
        get_pass = "SELECT password FROM entry WHERE user='"+str(user_input)+"'"
        if user_input:
            mycursor.execute(get_user)
            result = mycursor.fetchall()
            for userdb in result:
                if userdb[0] == user_input:
                    mycursor.execute(get_pass)
                    for passdb in mycursor.fetchall():
                        if passdb[0] == password_input:
                            self.root.current = 'centre'
                            self.root.get_screen('login').ids.user.text = ''
                            self.root.get_screen('login').ids.password.text = ''
                        else:
                            self.root.get_screen('login').ids.welcome_label.text = 'Verifier votre mot de passe'
        else:
            self.root.get_screen('login').ids.welcome_label.text = 'Mba fenoy izy io'

    def show_time_picker(self, textfield_instance, input, keyboard, *args):
        # Open time picker dialog.
        from datetime import datetime
        if keyboard:
            print(f"ID de l'objet dans show_time_picker : {input.hint_text}")
            time_picker = MDTimePicker()
            time_picker.bind(on_save=lambda instance, time: self.on_time_picker_dismiss(input.hint_text, time))
            time_picker.set_time(datetime.today().time())
            time_picker.open()

    def on_time_picker_dismiss(self, input_id, time):
        rapport_screen = self.root.get_screen("rapport")
        rapport_screen.ids[input_id].text = str(time)

    def show_dialog(self):
        dialog = MDDialog(
            title="Alert !!",
            text="Voulez-vous quitter??",
            buttons=[
                MDFlatButton(
                    text="Oui",
                    on_release=self.stop
                ),
                MDFlatButton(
                    text="Non",
                    on_release=self.close_dialog
                )
            ]
        )
        dialog.open()

    def close_dialog(self, instance):
        instance.parent.parent.parent.dismiss()

    def change_color(self, instance):
        if instance in self.root.get_screen('rapport').ids.values():
            current_id = list(self.root.get_screen('rapport').ids.keys())[list(self.root.get_screen('rapport').ids.values()).index(instance)]
            print(current_id)
            for i in range(4):
                if f"nav_icon{i+1}" == current_id:
                    self.root.get_screen('rapport').ids[f"nav_icon{i+1}"].md_bg_color = '#19F498'
                    self.root.get_screen('rapport').ids[f"nav_icon{i+1}"].text_color = 'black'
                    self.root.get_screen('rapport').ids[f"nav_icon{i+1}"].icon_color = 'black'
                else:
                    self.root.get_screen('rapport').ids[f"nav_icon{i + 1}"].md_bg_color = 'white'
                    self.root.get_screen('rapport').ids[f"nav_icon{i+1}"].text_color = 'black'
                    self.root.get_screen('rapport').ids[f"nav_icon{i+1}"].icon_color = 'black'


if __name__ == "__main__":
    LabelBase.register(name='poppins',
                       fn_regular='./fonts/Poppins/Poppins-SemiBold.ttf')
    MainApp().run()
