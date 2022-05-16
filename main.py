from inspect import ArgSpec
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, RiseInTransition
from kivy.lang import Builder
from kivy.uix.spinner import Spinner
import time
from kivy.storage.jsonstore import JsonStore
from kivy.properties import StringProperty, ListProperty
from kivy.uix.recycleview import RecycleView
from functools import partial
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.properties import BooleanProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from random import sample
from string import ascii_lowercase

Builder.load_file('main.kv')
frecuencia_de_inicio=""
hora_de_inicio=""
minuto_de_inicio=""
minuto_de_inicio=""


class Principal(Screen):
    
    def __init__(self, **kw):
        super(Screen,self).__init__(**kw)

    print_estado=StringProperty()

    def actualizar_label(self): 

        self.print_estado = StringProperty()  
        self.store=JsonStore('configuraciones.json')
        self.frecuencia_de_inicio=self.store.get('Frecuencia_de_vigilancia')
        self.dia_de_inicio=self.store.get('Dia_de_vigilancia')
        self.hora_de_inicio=self.store.get('Hora_de_vigilancia')
        self.minuto_de_inicio=self.store.get('Minuto_de_vigilancia')
        
        self.print_estado='Modalidad: '  #+ ' - ' + 'Dia: ' + dia_de_inicio['score'] + ' - ' + 'Hora: ' + hora_de_inicio['score']  + ' - ' + 'Minuto: ' + minuto_de_inicio['score']


class ClockLabel(Label):
    def __init__(self, **kwargs):
        super(ClockLabel, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
        

    def update(self, *args):

        self.store = JsonStore('configuraciones.json')
        global dia, hora, mes, minuto, segundo, año
        hora=time.strftime('%H')
        minuto=time.strftime('%M')
        segundo=time.strftime('%S')
        dia = time.strftime('%A')
        mes = time.strftime('%B')
        año = time.strftime('%g')

        print(año + ": " + mes + ": " + dia + ": " + hora + ": " +  minuto + ": " + segundo)
        self.text = time.strftime('%I:%M:%S')
        
        def iniciar_secuencia():
            global frecuencia_de_inicio, dia_de_inicio, hora_de_inicio, minuto_de_inicio

            frecuencia_de_inicio=self.store.get('Frecuencia_de_vigilancia')
            dia_de_inicio=self.store.get('Dia_de_vigilancia')
            hora_de_inicio=self.store.get('Hora_de_vigilancia')
            minuto_de_inicio=self.store.get('Minuto_de_vigilancia')
            
            #PRINT HORA COMPLETA

            #print(frecuencia_de_inicio['score'])
            #print(dia_de_inicio['score'])
            #print(hora_de_inicio['score'])
            #print(minuto_de_inicio['score'])

            #init=iniciar_vigilancia()


            if frecuencia_de_inicio['score'] == 'Diaria' and hora_de_inicio['score'] == hora and minuto_de_inicio['score'] == minuto and segundo == '00':
                print('VAMOS A INICIAR DIARIO')
                screen_manager.current= "proceso"
                esp_32()
                
            if frecuencia_de_inicio['score'] == 'Semanal' and dia_de_inicio['score'] == dia and hora_de_inicio['score'] == hora and minuto_de_inicio['score'] == minuto and segundo == '00':
                print('VAMOS A INICIAR SEMANAL') 
                screen_manager.current= "proceso" 

            if frecuencia_de_inicio['score'] == 'Mensual' and dia_de_inicio['score'] == dia and hora_de_inicio['score'] == hora and minuto_de_inicio['score'] == minuto and segundo == '00':
                print('VAMOS A INICIAR MENSUAL')
                screen_manager.current= "proceso"
        
        iniciar_secuencia()


class esp_32():
    def __init__(self):
        print("hola soy esp")
        self.iniciar()
    
    def iniciar(self):
        print("vamos a inicar")
        
        def activar(*args):
            print("vamos a darle")
            hola=RequestRecycleView()
            hola.add()
            
            
        Clock.schedule_once(activar,2)

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''



class RequestRow(RecycleDataViewBehavior):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''

        self.index = index
        self.row_index = str(index)
        self.row_content = data['text']
        return super(RequestRow, self).refresh_view_attrs(
            rv, index, data)

class RequestRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []
        self.add()
        

    def add(self,*args):
        print("vamos a iniciar lakjdslfkjasdf")
        for r in range(3):
            row = {'text': ''.join(sample(ascii_lowercase, 6))}
            self.data.append(row)

        Clock.schedule_once(self.add,2)



class Configuracion(Screen):
    def __init__(self,**kw):
        super(Configuracion,self).__init__(**kw)
        self.store = JsonStore('configuraciones.json')

    #Listas para el spinner
    minutos = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
    horas = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    
    def spinner_frecuencia_de_vigilancia(self, value):
        global frecuencia_de_inicio
        print("Se selecciono hacer la vigilancia: " + value)
        self.store.put('Frecuencia_de_vigilancia', score= value)
        frecuencia_de_inicio = value
                
    def spinner_dia(self, value):
        global dia_de_inicio
        print("El dia de la vigilancia sera:  " + value)
        self.store.put('Dia_de_vigilancia', score= value)
        dia_de_inicio = value

    def spinner_hora_de_inicio(self, value):
        global hora_de_inicio
        print("La hora de vigilancia sera: " + value)
        self.store.put('Hora_de_vigilancia', score= value)
        hora_de_inicio = value

    def spinner_minuto_de_inicio(self, value):
        global minuto_de_inicio
        print("El minuto inicio sera: " + value)
        self.store.put('Minuto_de_vigilancia', score= value)
        minuto_de_inicio = value
        

class Ventana_proceso(Screen):
    pass

screen_manager = ScreenManager(transition = RiseInTransition())
screen_manager.add_widget(Principal(name ="main"))
screen_manager.add_widget(Configuracion(name ="config"))
screen_manager.add_widget(Ventana_proceso(name="proceso"))
 
class VigilanciaApp(App):
    def build(self):
        return screen_manager


if __name__ == '__main__':
    clock = VigilanciaApp()
    clock.run()