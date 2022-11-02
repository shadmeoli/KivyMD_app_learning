import json
from datetime import datetime
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.card import MDCardSwipe

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty

# window size
Window.size = (350, 700)


# main entry app
class Todo(MDApp):

    # kv file
    path_to_kv_file = "splash.kv"

    primary_color = [
        0.12941176470588237,
        0.5882352941176471,
        0.9529411764705882,
        1
    ]

    # rendering function
    def build(self):

        global screen_manager
        screen_manager = ScreenManager(
            # transition=NoTransition()
        )
        # file rendering pages
        screen_manager.add_widget(Builder.load_file("splash.kv"))

        return screen_manager

# onotilizer
if __name__ == '__main__':
    # LabelBase.register(name="Math")
    Todo().run()
