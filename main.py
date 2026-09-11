from kivy.app import App
from kivy.uix.label import Label
class HydraApp(App):
    def build(self):
        return Label(text="Hydra Smart Duplicate Finder - Ready")
HydraApp().run()
