from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
import time

Window.size = (400, 400)
Builder.load_string("""
<Layout>
    Label:
        text:"Vigilancia de celdas patron"
    ClockLabel:
        id: clock_label
        size_hint: 0.75,1
""")

class Layout(BoxLayout):
    pass

class ClockLabel(Label):
    def __init__(self, **kwargs):
        super(ClockLabel, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
    def update(self, *args):
        self.text = time.strftime('%I:%M:%S')
 
class DigitalClockApp(App):
    def build(self):
        return Layout()

clock = DigitalClockApp()

clock.run()