import os
import logging
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# Setup professional logging for Android
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("ZeraAI_System")

class ZeraAIApp(App):
    def build(self):
        # Initializing the Main Engine Layout
        self.canvas_layout = FloatLayout()
        
        # Creating a Deep Tech Background
        with self.canvas_layout.canvas.before:
            Color(0.01, 0.01, 0.03, 1) # Dark Cyber Blue
            self.bg_rect = Rectangle(size=Window.size, pos=(0, 0))
        Window.bind(size=self._refresh_bg)

        # AI Core Visual (The Glowing Ring)
        # Path: Same as your uploaded file
        ring_source = '1770689044948.jpg'
        
        if os.path.exists(ring_source):
            self.core_image = Image(
                source=ring_source,
                size_hint=(0.9, 0.9),
                pos_hint={'center_x': 0.5, 'center_y': 0.55}
            )
            logger.info("Visual Core: Initialized successfully.")
        else:
            self.core_image = Label(
                text="[ CORE DATA MISSING ]",
                color=(1, 0, 0, 1),
                font_size='24sp'
            )
            logger.error("Visual Core: Image file not detected.")

        # System Status Label
        self.status_text = Label(
            text="SYSTEM: INITIALIZING...",
            font_size='18sp',
            bold=True,
            color=(0, 1, 0.8, 1),
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.1}
        )

        # Version Branding
        self.version_tag = Label(
            text="Zera OS v1.0.1 | Stable Build",
            font_size='12sp',
            color=(0.4, 0.4, 0.4, 1),
            pos_hint={'center_x': 0.5, 'y': 0.02}
        )

        # Assembling the UI Components
        self.canvas_layout.add_widget(self.core_image)
        self.canvas_layout.add_widget(self.status_text)
        self.canvas_layout.add_widget(self.version_tag)

        # Scheduling the Boot Sequence
        Clock.schedule_once(self.activate_system, 3.5)
        
        return self.canvas_layout

    def _refresh_bg(self, instance, value):
        self.bg_rect.size = value
        self.bg_rect.pos = (0, 0)

    def activate_system(self, dt):
        self.status_text.text = "SYSTEM: ZERA IS ONLINE"
        self.status_text.color = (0, 1, 0.2, 1) # Success Green
        logger.info("System Status: Online and ready.")

    def on_pause(self):
        # Keeping the app alive in background
        return True

if __name__ == '__main__':
    try:
        ZeraAIApp().run()
    except Exception as fatal_error:
        logger.critical(f"System Crash: {str(fatal_error)}")
