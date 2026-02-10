import os
import logging
import threading
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# Android Logger Setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("ZeraAI")

class ZeraApp(App):
    def build(self):
        # Setting up the Main UI Container
        self.root_layout = FloatLayout()
        
        # Adding a professional dark background
        with self.root_layout.canvas.before:
            Color(0.02, 0.02, 0.05, 1) # Deep Night Blue
            self.bg_rect = Rectangle(size=Window.size, pos=(0, 0))
        Window.bind(size=self._update_background)

        # AI Status Display
        self.status = Label(
            text="[ ZERA SYSTEM ONLINE ]",
            font_size='20sp',
            bold=True,
            color=(0, 0.8, 1, 1), # Electric Blue
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.15}
        )

        # Loading the Assistant Core Image (The Ring)
        img_file = '1770689044948.jpg'
        if os.path.exists(img_file):
            self.core_display = Image(
                source=img_file,
                size_hint=(0.85, 0.85),
                pos_hint={'center_x': 0.5, 'center_y': 0.55},
                allow_stretch=True
            )
            logger.info("Zera Core Visuals Loaded.")
        else:
            self.core_display = Label(text="Visual Core Missing", color=(1,0,0,1))
            logger.error(f"Critical: {img_file} not found in repository.")

        # App Info Label
        self.info = Label(
            text="AI Version 1.0.0 | Developer Mode",
            font_size='12sp',
            color=(0.5, 0.5, 0.5, 1),
            size_hint=(1, 0.05),
            pos_hint={'center_x': 0.5, 'y': 0.02}
        )

        # Adding all components to the screen
        self.root_layout.add_widget(self.core_display)
        self.root_layout.add_widget(self.status)
        self.root_layout.add_widget(self.info)

        return self.root_layout

    def _update_background(self, instance, value):
        self.bg_rect.size = value
        self.bg_rect.pos = (0, 0)

    def on_start(self):
        # Triggering the startup sequence
        logger.info("Initializing Zera AI Framework...")
        Clock.schedule_once(self.complete_boot, 2)

    def complete_boot(self, dt):
        self.status.text = "ZERA: Listening for commands..."
        self.status.color = (0, 1, 0.5, 1) # Neon Green

    def on_pause(self):
        # Essential for Android apps to not crash in background
        return True

if __name__ == '__main__':
    try:
        ZeraApp().run()
    except Exception as e:
        logger.critical(f"App Startup Failed: {e}")
