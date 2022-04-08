from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import CardTransition, ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import time


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass
                               
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class FirstApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    FirstApp().run()