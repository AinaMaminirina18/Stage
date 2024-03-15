from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager


class Screen_com(MDApp):
    def build(self):
        screen = ScreenManager()
        screen.add_widget(Builder.load_file("Com/main.kv"))
        return screen


Screen_com().run()


