from kivy.uix.screenmanager import ScreenManager
from kivymd.tools.hotreload.app import MDApp


class SM(ScreenManager):
    def get_classes(self):
        return {screen.__class__.__name__: screen.__class__.__module__ for screen in self.screens}


class MainApp(MDApp):
    DEBUG = True
    sm = None
    state = {}

    def build_app(self, first=False):
        if self.sm is None:
            self.state = {'current': 'one',
                          'one': 'data one',
                          'two': 'data two'}
        else:
            self.state = {'current': self.sm.current,
                          'one': self.sm.get_screen('one').ids.data.text,
                          'two': self.sm.get_screen('two').ids.data.text}

        KV_FILES = []
        self.sm = SM()
        CLASSES = self.sm.get_classes()

        return self.sm

    def apply_state(self, state):
        self.sm.current = state['current']
        self.sm.get_screen('one').ids.data.text = state['one']
        self.sm.get_screen('two').ids.data.text = state['two']


if __name__ == '__main__':
    app = MainApp()
    app.run()
