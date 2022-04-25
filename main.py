from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, RiseInTransition
from kivy.lang import Builder
from kivy.uix.spinner import Spinner
import time
from kivy.storage.jsonstore import JsonStore


Builder.load_file('main.kv')

frecuencia_de_inicio=""
hora_de_inicio=""
minuto_de_inicio=""
minuto_de_inicio=""


class Principal(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        pass
        

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

            if frecuencia_de_inicio['score'] == 'Diaria' and hora_de_inicio['score'] == hora and minuto_de_inicio['score'] == minuto and segundo == '00':
                print('VAMOS A INICIAR DIARIO')

            if frecuencia_de_inicio['score'] == 'Semanal' and dia_de_inicio['score'] == dia and hora_de_inicio['score'] == hora and minuto_de_inicio['score'] == minuto and segundo == '00':
                print('VAMOS A INICIAR SEMANAL')  

            if frecuencia_de_inicio['score'] == 'Mensual' and dia_de_inicio['score'] == dia and hora_de_inicio['score'] == hora and minuto_de_inicio['score'] == minuto and segundo == '00':
                print('VAMOS A INICIAR MENSUAL')
        

        iniciar_secuencia()


class Configuracion(Screen):
    def __init__(self,**kw):
        super(Configuracion,self).__init__(**kw)
        self.store = JsonStore('configuraciones.json')

    #Listas para el spinner
    minutos = [str(i) for i in range (60)]
    horas = [str(i) for i in range(24)]
    
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
        

screen_manager = ScreenManager(transition = RiseInTransition())
screen_manager.add_widget(Principal(name ="main"))
screen_manager.add_widget(Configuracion(name ="config"))
 
class VigilanciaApp(App):
    def build(self):
        return screen_manager


if __name__ == '__main__':
    clock = VigilanciaApp()
    clock.run()