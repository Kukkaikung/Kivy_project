from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.core.window import Window


class MyApp(App) :
    
    def build(self) :
        self.name_input = TextInput(text='Enter your name', font_size = 40)
        start_button = Button(text='Start', font_size = 40, on_press=self.switch_to_start)
        setting_button = Button(text='Setting', font_size = 40, on_press=self.switch_to_setting)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.name_input)
        layout.add_widget(start_button)
        layout.add_widget(setting_button)

        return layout
    
    def switch_to_start(self, instance):
        self.root.clear_widgets()
        self.root.add_widget(Label(text=f"Game is starting, {self.name_input.text}", font_size = 40))

    def switch_to_setting(self, instance):
        self.root.clear_widgets()
        audio_button = Button(text='Audio Setting')
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(audio_button)
        self.root.add_widget(layout)

    

if __name__ == '__main__' :
    MyApp().run()

        