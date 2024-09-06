# main.py

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

# Load the .kv file
Builder.load_file('presentation.kv')

class PresentationScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class TaJiRApp(App):
    def build(self):
        self.sm = ScreenManager()
        
        # Adding the PresentationScreen
        self.sm.add_widget(PresentationScreen(name='presentation'))
        
        # Adding the MainScreen for later navigation
        self.sm.add_widget(MainScreen(name='main'))
        
        return self.sm
    
    def switch_to_main_screen(self):
        # Switch to the main screen
        self.sm.current = 'main'

if __name__ == '__main__':
    TaJiRApp().run()

