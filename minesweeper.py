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
import random
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
import webbrowser


class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 1

        self.background_music = SoundLoader.load('C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\gui\\venv\\kivy_project\\Toothless-Dancing-Meme-_NEW-VARIATIONS_.mp3')
        self.background_music.loop = True
        self.background_music.play()
        
        input_layout = GridLayout(cols = 2)
        self.name_input = TextInput(hint_text='Enter your name', font_size=40, multiline=False, padding_y=(70, 0))
        self.confirm_button = Button(text='Confirm', font_size=35, on_press=self.confirm_pressed)
        
        
        input_layout.add_widget(self.name_input)
        input_layout.add_widget(self.confirm_button)
        
        self.start_button = Button(text='Start', font_size=35, on_press=self.start_game)
        self.setting_button = Button(text='Setting', font_size=35, on_press=self.go_to_settings)
        self.gamescreen_button = Button(text='Tutorial',font_size=35, on_press=self.go_gamescreen) #Tutorial Button
        self.dont_push_button = Button(text="Don't push", font_size=35, on_press=self.dont_push_pressed)

        self.add_widget(input_layout)
        self.add_widget(self.start_button)
        self.add_widget(self.setting_button)
        self.add_widget(self.gamescreen_button) #TutorialButton
        self.add_widget(self.dont_push_button)

        self.player_name = '' 


    def start_game(self, instance):
        minesweeper_game = MinesweeperGame(rows=7, cols=7, mines=7, player_name=self.player_name)
        screen = Screen(name='minesweeper_game_screen')
        screen.add_widget(minesweeper_game)
        MyApp.get_running_app().screen_manager.add_widget(screen)

        MyApp.get_running_app().screen_manager.current = 'minesweeper_game_screen'


    def go_to_settings(self, instance):
        MyApp.get_running_app().screen_manager.current = 'settings_screen'

    def go_gamescreen(self, instance): #go to tutorial
        MyApp.get_running_app().screen_manager.current = 'game_screen'
        

    def confirm_pressed(self, instance):
        self.player_name = self.name_input.text
        your_name = Label(text=f'Your name {self.player_name}')
        MyApp.get_running_app().settings_screen.set_your_name_label(self.player_name)

    def dont_push_pressed(self, instance):
        dont_push_screen = DontPushScreen()
        screen = Screen(name='dont_push_screen')
        screen.add_widget(dont_push_screen)
        MyApp.get_running_app().screen_manager.add_widget(screen)

        MyApp.get_running_app().screen_manager.current = 'dont_push_screen'
        self.stop_background_music()

    def play_background_music(self):
        if not self.background_music.state == 'play':
            self.background_music.play()

    def stop_background_music(self):
        if self.background_music.state == 'play':
            self.background_music.stop()


class GameScreen(GridLayout):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.cols = 1
        self.name_label = Label(text=" How to play: Find the bomb.\n By left-clicking on a square, if it's not a bomb,\n it will show a number that tells you how many bombs there are around the square.\n Open all the squares that aren't bombs to win.", font_size=15)
        self.back_button = self.back_button = Button(text='Back', on_press=self.go_back)
        self.exit_button = Button(text='Exit', on_press=self.exit_app)
        
        self.add_widget(self.name_label)
        self.add_widget(self.back_button)
        self.add_widget(self.exit_button)

    def go_back(self, instance):
        MyApp.get_running_app().screen_manager.current = 'main_screen'
    
    def exit_app(self, instance):
        App.get_running_app().stop()


class SettingsScreen(GridLayout):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.cols = 1
        
        label_layout = BoxLayout(size_hint_y=None, height=dp(30), spacing=10)
        
        self.your_name_label = Label(text='Your name:', size_hint_x=None, width=Window.width / 2)
        label_layout.add_widget(self.your_name_label)

        self.audio_label = Label(text='Audio: On', size_hint_x=None, width=Window.width / 2)
        label_layout.add_widget(self.audio_label)

        self.add_widget(label_layout)

        self.audio_button = Button(text='Audio', on_press=self.audio_settings)
        self.back_button = Button(text='Back', on_press=self.go_back)
        self.exit_button = Button(text='Exit', on_press=self.exit_app)

        self.add_widget(self.audio_button)
        self.add_widget(self.back_button)
        self.add_widget(self.exit_button)

        self.audio_status = True

    def audio_settings(self, instance):
        if self.audio_status:
            self.audio_status = False
            self.audio_label.text = 'Audio: Off'
            MyApp.get_running_app().main_screen.stop_background_music()
        else:
            self.audio_status = True
            self.audio_label.text = 'Audio: On'
            MyApp.get_running_app().main_screen.play_background_music()

    def go_back(self, instance):
        MyApp.get_running_app().screen_manager.current = 'main_screen'

    def set_your_name_label(self, name) :
        self.your_name_label.text = f'Your name: {name}'

    def exit_app(self, instance):
        App.get_running_app().stop()

class DontPushScreen(GridLayout):
    def __init__(self, **kwargs):
        super(DontPushScreen, self).__init__(**kwargs)
        self.cols = 1

        back_button = Button(text='Back', font_size=15, on_press=self.go_back)
        youtube_button = Button(text="This is the last warning, don't push!!", font_size=35, on_press=self.open_youtube)
        self.exit_button = Button(text='Exit', font_size=15,on_press=self.exit_app)

        self.add_widget(back_button)
        self.add_widget(youtube_button)
        self.add_widget(self.exit_button)
    
    def go_back(self, instance):
        MyApp.get_running_app().main_screen.play_background_music()
        MyApp.get_running_app().screen_manager.current = 'main_screen'

    def open_youtube(self, instance):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 

    def exit_app(self, instance):
        App.get_running_app().stop()
        

class MinesweeperGame(GridLayout):
    def __init__(self, rows, cols, mines, player_name='', **kwargs):
        super(MinesweeperGame, self).__init__(**kwargs)
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = []
        self.unopened_cells = rows * cols - mines
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.player_name = player_name
        self.create_board()
        self.explosion_sound = SoundLoader.load('C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\gui\\venv\\kivy_project\\New_Nuke_Effect.mp3')
        self.congrat_sound = SoundLoader.load('C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\gui\\venv\\kivy_project\\Congratulations-_BBC-Sound-Effect-into-Cheer-Into-Applause-Inclusion_.mp3')

    def play_explosion_sound(self):
        if self.explosion_sound:
            self.explosion_sound.play()
    
    def play_congrat_sound(self):
        if self.congrat_sound:
            self.congrat_sound.play()
    
    def create_board(self):
        bomb_positions = random.sample(range(self.rows * self.cols), self.mines)
        for pos in bomb_positions:
            row = pos // self.cols
            col = pos % self.cols
            self.board[row][col] = 'B'

        for row in range(self.rows):
            for col in range(self.cols):
                if row < 7 and col < 7:
                    button = Button(
                        text='',
                        on_press=lambda instance, row=row, col=col: self.on_button_press(row, col)
                    )
                    self.add_widget(button)
                    self.buttons.append(button)

    def on_button_press(self, row, col):
        button_index = row * self.cols + col
        button = self.buttons[button_index]

        if self.is_bomb(row, col):
            button.text = 'Bomb'
            self.end_game()
            self.play_explosion_sound()
        else:
            bomb_count = self.count_bombs_around(row, col)
            button.text = str(bomb_count)
            self.unopened_cells -= 1

            if self.unopened_cells == 0:
                self.win_game()
    
    def is_bomb(self, row, col):
        return True if self.board[row][col] == 'B' else False
    
    def count_bombs_around(self, row, col):
        count = 0
        for i in range(max(0, row - 1), min(self.rows, row + 2)):
            for j in range(max(0, col - 1), min(self.cols, col + 2)):
                if self.board[i][j] == 'B':
                    count += 1
        return count
    
    def end_game(self):
        for button in self.buttons:
            button.disabled = True
        self.show_result_popup("Game Over", f'{self.player_name}, You hit a bomb!')
        MyApp.get_running_app().main_screen.stop_background_music() 


    def win_game(self):
        for button in self.buttons:
            button.disabled = True
        self.show_result_popup("Congratulations!", f"{self.player_name}, You Win!")
        MyApp.get_running_app().main_screen.stop_background_music() 
        self.play_congrat_sound()

    def show_result_popup(self, title, message):
        popup_content = Label(text=message)
        popup = Popup(title=title, content=popup_content, size_hint=(None, None), size=(400, 200))
        popup.open()

class MinesweeperApp(App):
    def build(self):
        return MinesweeperGame(rows=7, cols=7,mines=7)


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

        self.dont_push_screen = DontPushScreen()
        screen = Screen(name='dont_push_screen')
        screen.add_widget(self.dont_push_screen)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def set_name(self, name):
        self.game_screen.set_name(name)


if __name__ == '__main__':
    MyApp().run()