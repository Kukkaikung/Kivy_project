from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class MyApp(App) :
    
    def build(self):
        float_layout = FloatLayout()
        label01 = Label(text = 'Hello This test Program', font_size = 50)
        
        float_layout.add_widget(label01)

        return float_layout
    
if __name__ == '__main__' :
    MyApp().run()

        