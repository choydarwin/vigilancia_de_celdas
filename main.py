from cgitb import text
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import CardTransition, ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import StringProperty
import time


class FirstWindow(Screen):
    pass
    
class ClockText(Label):
    def update(self, *args):
        self.text = time.strftime('%I'+':'+'%M' + ':' + '%S' +  ' %p')
        print(self.text)
        return ClockText

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass
                               
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class FirstApp(App):
    def build(self):
        clocktext = ClockText()
        Clock.schedule_interval(clocktext.update, 1)
        return kv

if __name__ == '__main__':
    FirstApp().run()