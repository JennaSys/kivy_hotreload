from kivy.uix.screenmanager import ScreenManager
from kivymd.tools.hotreload.app import MDApp


class SM(ScreenManager):
    def get_classes(self):
        return {screen.__class__.__name__: screen.__class__.__module__ for screen in self.screens}


class MainApp(MDApp):
    DEBUG = True
    sm = None

    def build_app(self, first=False):
        if self.sm is not None:
            self.state = {'current': self.sm.current}

        KV_FILES = []
        self.sm = SM()
        CLASSES = self.sm.get_classes()

        return self.sm

    def apply_state(self, state):
        if state is not None:
            self.sm.current = state['current']


if __name__ == '__main__':
    app = MainApp()
    app.run()
