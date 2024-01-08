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


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.name_input = TextInput(hint_text='Enter your name')
        self.start_button = Button(text='Start', on_press=self.start_game)
        self.setting_button = Button(text='Setting', on_press=self.go_to_settings)

        self.add_widget(self.name_input)
        self.add_widget(self.start_button)
        self.add_widget(self.setting_button)

    def start_game(self, instance):
        MyApp.get_running_app().screen_manager.current = 'game_screen'

    def go_to_settings(self, instance):
        MyApp.get_running_app().screen_manager.current = 'settings_screen'


class GameScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Game is starting'))


class SettingsScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.audio_button = Button(text='Audio', on_press=self.audio_settings)
        self.back_button = Button(text='Back', on_press=self.go_back)

        self.add_widget(self.audio_button)
        self.add_widget(self.back_button)

    def audio_settings(self, instance):
        # Add audio settings logic here
        pass

    def go_back(self, instance):
        pass



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


if __name__ == '__main__':
    MyApp().run()