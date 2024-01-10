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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp



class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 1

        
        input_layout = GridLayout(cols = 2)

        self.name_input = TextInput(hint_text='Enter your name', font_size=40, multiline=False, padding_y=(70, 0))
        self.confirm_button = Button(text='Confirm', font_size=35, on_press=self.confirm_pressed)
        
        
        input_layout.add_widget(self.name_input)
        input_layout.add_widget(self.confirm_button)
        
        self.start_button = Button(text='Start', font_size=35, on_press=self.start_game)
        self.setting_button = Button(text='Setting', font_size=35, on_press=self.go_to_settings)

        self.add_widget(input_layout)
        self.add_widget(self.start_button)
        self.add_widget(self.setting_button)

    def start_game(self, instance):
        MyApp.get_running_app().set_name(self.name_input.text)
        MyApp.get_running_app().screen_manager.current = 'game_screen'

    def go_to_settings(self, instance):
        MyApp.get_running_app().screen_manager.current = 'settings_screen'
        

    def confirm_pressed(self, instance):
        name = self.name_input.text
        your_name = Label(text=f'Your name {name}')


class GameScreen(GridLayout):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.cols = 1
        self.name_label = Label(text='')

        self.add_widget(self.name_label)

    def set_name(self, name):
        self.name_label.text = f'Your name: {name}'


class SettingsScreen(GridLayout):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.cols = 1
        self.top_label = Label(text = 'Welcome!', font_size = 20, size_hint_y = None, height = dp(30))
        
        self.audio_button = Button(text='Audio', on_press=self.audio_settings)
        self.back_button = Button(text='Back', on_press=self.go_back)

        self.add_widget(self.top_label)
        self.add_widget(self.audio_button)
        self.add_widget(self.back_button)

    def audio_settings(self, instance):
        # Add audio settings logic here
        pass

    def go_back(self, instance):
        MyApp.get_running_app().screen_manager.current = 'main_screen'


class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.main_screen = MainScreen()
        screen = Screen(name='main_screen')
        screen.add_widget(self.main_screen)
        self.screen_manager.add_widget(screen)

        self.game_screen = GameScreen()
        screen = Screen(name='game_screen')
        screen.add_widget(self.game_screen)
        self.screen_manager.add_widget(screen)

        self.settings_screen = SettingsScreen()
        screen = Screen(name='settings_screen')
        screen.add_widget(self.settings_screen)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def set_name(self, name):
        self.game_screen.set_name(name)


if __name__ == '__main__':
    MyApp().run()