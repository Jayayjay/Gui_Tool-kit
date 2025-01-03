from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder

Builder.load_file('main.kv')

class HoverButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = self.background_normal  # Initial background
        self.background_down = self.background_down      # Background when pressed

    def on_enter(self):
        # Change background or effect when hovering
        self.background_normal = 'assets/hovered_icon.png'  # Image for hover effect

    def on_leave(self):
        # Reset back to original image when not hovering
        self.background_normal = self.background_normal


class CustomToolbar(BoxLayout):
    pass


class ToolbarApp(App):
    def build(self):
        Window.size = (500, 100)
        Window.borderless = True
        # Set a suitable window size
        return CustomToolbar()


if __name__ == '__main__':
    ToolbarApp().run()
