from kivy.uix.screenmanager import ScreenManager
from kivymd.tools.hotreload.app import MDApp


class SM(ScreenManager):
    def get_classes(self):
        return {screen.__class__.__name__: screen.__class__.__module__ for screen in self.screens}


class MainApp(MDApp):
    DEBUG = True

    sm = None

    def build_app(self, first=False):
        self.sm = SM()

        KV_FILES = []

        self.sm = SM()

        CLASSES = self.sm.get_classes()

        self.sm.current = 'one'
        return self.sm


if __name__ == '__main__':
    app = MainApp()
    app.run()
