from turtle import Screen
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, RiseInTransition
from kivy.lang import Builder
from kivy.uix.spinner import Spinner
import time

Builder.load_file('main.kv')

class Principal(Screen):
    pass

class Configuracion(Screen):
    
    def spinner_frecuencia_de_vigilancia(self, value):
        print("Se selecciono hacer la vigilancia: " + value)
    
    def spinner_dia(self, value):
        print("El dia de la vigilancia sera:  " + value)

    def spinner_hora_de_inicio(self, value):
        print("La hora de vigilancia sera: " + value)

class ClockLabel(Label):
    def __init__(self, **kwargs):
        super(ClockLabel, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
    def update(self, *args):
        self.text = time.strftime('%I:%M:%S')

screen_manager = ScreenManager(transition = RiseInTransition())
screen_manager.add_widget(Principal(name ="main"))
screen_manager.add_widget(Configuracion(name ="config"))
 
class VigilanciaApp(App):
    def build(self):
        return screen_manager

if __name__ == '__main__':
    clock = VigilanciaApp()
    clock.run()