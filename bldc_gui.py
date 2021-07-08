from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import math
# from pyfirmata import Arduino, SERVO
from time import sleep
#port = '/dev/ttyACM0'
#pin = 10
#board = Arduino(port)

#def rotateServo(pin, angle):
       #board.digital[pin].write(angle)

class Function(Screen):
    pass
    #def switch_on(self, instance, value):
       # if value is True:
            #rotateServo(pin, 5)
        #else:
            #rotateServo(pin, 0)
    #def rotate(self):
        #spin = str(math.floor(self.ids.spin_value.value))
        #if int(spin)>100:
            #rotateServo(spin,spin)
        #else:
            #board.digital[pin].write(0)

class InfraredLightApp(MDApp):
    def build(self):
        Builder.load_file('layout.kv')
        return Function()

InfraredLightApp().run()
