from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp


class SM(ScreenManager):
    pass


class MainApp(MDApp):
    sm = None

    def build(self):
        self.sm = SM()
        self.sm.current = 'one'
        return self.sm


if __name__ == '__main__':
    app = MainApp()
    app.run()
