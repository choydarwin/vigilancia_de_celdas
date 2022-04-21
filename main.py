from turtle import Screen
from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, RiseInTransition
from kivy.lang import Builder
from kivy.core.window import Window
import time


Builder.load_string("""
<Principal>
    GridLayout:
        cols:1
        size: root.width, root.height

        Label:
            text:"Vigilancia de celdas patron"
        ClockLabel:
            id: clock_label
            size_hint: 0.75,1
        Button:
            text: "Configuracion"
            background_color : 0, 0, 1, 1
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'otra'


<Otra>
    GridLayout:
        cols:1
        size: root.width, root.height
        Label:
            text:"Settings"
        ClockLabel:
            id: clock_label
            size_hint: 0.75,1
        Button:
            text: "Regresar"
            background_color : 0, 0, 1, 1
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'principal'


""")


class Principal(Screen):
    pass

class Otra(Screen):
    pass

class ClockLabel(Label):
    def __init__(self, **kwargs):
        super(ClockLabel, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
    def update(self, *args):
        self.text = time.strftime('%I:%M:%S')

screen_manager = ScreenManager(transition = RiseInTransition())
screen_manager.add_widget(Principal(name ="principal"))
screen_manager.add_widget(Otra(name ="otra"))
 
class VigilanciaApp(App):
    def build(self):
        return screen_manager

clock = VigilanciaApp()

clock.run()