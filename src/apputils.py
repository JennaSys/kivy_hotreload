import os

from kivymd.app import MDApp


def load_kv(module_name):
    MDApp.get_running_app().KV_FILES.append(f"{os.path.join(*module_name.split('.'))}.kv")

