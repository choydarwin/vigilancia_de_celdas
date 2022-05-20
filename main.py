from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, RiseInTransition
from kivy.lang import Builder
import time
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from functools import partial
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview import RecycleView


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

        BoxLayout:
            orientation: 'vertical'
            Label:
                text:"Configuracion seleccionada - " 

        Button:
            text: "Configuracion"
            background_color : 0, 0, 1, 1
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'config'


<Configuracion>

    GridLayout:
        cols:1
        size: root.width, root.height

        Label:
            text:"Settings"

        Spinner: 
            id: spinner_frecuencia
            on_text: root.spinner_frecuencia_de_vigilancia(spinner_frecuencia.text)
            text: "Seleccionar modalidad"
            values: ["Diaria", "Semanal", "Mensual"]
            on_text: spinner_dia.disabled = True if spinner_frecuencia.text == "Diaria" else False

        Spinner: 
            id: spinner_dia
            on_text: root.spinner_dia(spinner_dia.text)
            text: "Seleccionar dia"
            values: ["Monday", "Tuesday", "Miercoles", "Jueves", "Viernes"]
            
        
        BoxLayout:
            orientation:'horizontal'
            Spinner: 
                id: spinner_hora
                on_text: root.spinner_hora_de_inicio(spinner_hora.text)
                text: "Seleccionar hora de inicio"
                values: root.horas

            Spinner: 
                id: spinner_minuto
                on_text: root.spinner_minuto_de_inicio(spinner_minuto.text)
                text: "Seleccionar minuto de inicio"
                values: root.minutos

        Button:
            text: "Regresar"
            background_color : 0, 0, 1, 1
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'main'

<MyBL>:
    t1: ""
    t2: ""
    orientation: "horizontal"
    Label:
        text: root.t1
    Label:
        text: root.t2
<RV>:
    viewclass: 'MyBL'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True


<Ventana_proceso>
    GridLayout:
        cols:1
        size: root.width, root.height

        Label:
            text:"Vigilancia de celdas patron"

        RV:

        ProgressBar:
            id: proceso
            min: 0
            max: 100
            value:0

        Button:
            text: "Configuracion"
            background_color : 0, 0, 1, 0
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'config'

""")

frecuencia_de_inicio=""
hora_de_inicio=""
minuto_de_inicio=""
minuto_de_inicio=""

data_sms=[{"t1":"PREPARANDO"}]


class Principal(Screen):
    
    def __init__(self, **kw):
        super(Screen,self).__init__(**kw)

        #print_estado=StringProperty()

    def actualizar_label(self): 

        #self.print_estado = StringProperty()  
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
                Clock.schedule_once(partial(esp_32.activar,"uno_y_cuatro"),2)
                Clock.schedule_once(partial(esp_32.activar,"dos_y_tres"),4)
                Clock.schedule_once(partial(esp_32.activar,"tres_y_uno"),6)
                Clock.schedule_once(partial(esp_32.activar,"cuatro_y_dos"),8)
                
            if frecuencia_de_inicio['score'] == 'Semanal' and dia_de_inicio['score'] == dia and hora_de_inicio['score'] == hora and minuto_de_inicio['score'] == minuto and segundo == '00':
                print('VAMOS A INICIAR SEMANAL') 
                screen_manager.current= "proceso" 

            if frecuencia_de_inicio['score'] == 'Mensual' and dia_de_inicio['score'] == dia and hora_de_inicio['score'] == hora and minuto_de_inicio['score'] == minuto and segundo == '00':
                print('VAMOS A INICIAR MENSUAL')
                screen_manager.current= "proceso"
        
        iniciar_secuencia()

class esp_32():
    def activar(celdas_a_comparar,*args):
        print("vamos a activar: " + celdas_a_comparar)
        RV.agregar_en_pantalla(celdas_a_comparar)   
      

class Configuracion(Screen):
    def __init__(self,**kw):
        super(Configuracion,self).__init__(**kw)
        self.store = JsonStore('configuraciones.json')

    #Listas para el spinner
    minutos = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
    horas = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    
    def spinner_frecuencia_de_vigilancia(self, value):
        global frecuencia_de_inicio
        print("Modalidad: " + value)
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
        
class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,RecycleBoxLayout):
    pass

class MyBL(RecycleDataViewBehavior, BoxLayout):
    ''' Add selection support to the Label '''
    index = None
    #data=data_sms lo mismo que el comnetario de abajo

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        #self.data=data_sms pense que iba a funcionar asi
        return super(MyBL, self).refresh_view_attrs(
            rv, index, data)

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        Clock.schedule_interval(self.monitoriar,2)
    
    def monitoriar(self,*kw):
        self.data = data_sms


    @classmethod    
    def agregar_en_pantalla(self,celdas_a_comparar):
        data_sms.append({"t1":"comparando celdas: "+ celdas_a_comparar})
        #print(data_sms)

screen_manager = ScreenManager(transition = RiseInTransition())

class VigilanciaApp(App):
    def build(self):
        #screen_manager = ScreenManager(transition = RiseInTransition())
        screen_manager.add_widget(Principal(name ="main"))
        screen_manager.add_widget(Configuracion(name ="config"))
        screen_manager.add_widget(Ventana_proceso(name="proceso"))
        return screen_manager

if __name__ == '__main__':
    clock = VigilanciaApp()
    clock.run()