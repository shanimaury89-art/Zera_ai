import os
import logging
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# Logging setup for debugging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("ZeraAI")

class ZeraApp(App):
    def build(self):
        # Main Layout
        self.root_layout = FloatLayout()
        
        # Background color (Dark theme)
        with self.root_layout.canvas.before:
            Color(0.05, 0.05, 0.05, 1) # Dark Grey
            self.rect = Rectangle(size=Window.size, pos=(0, 0))
        Window.bind(size=self._update_rect)

        # Status Label
        self.status_label = Label(
            text="Zera AI: Ready",
            font_size='18sp',
            color=(0, 1, 1, 1),  # Cyan color
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.1}
        )

        # Main Glowing Ring Image
        img_path = '1770689044948.jpg'
        if os.path.exists(img_path):
            self.main_img = Image(
                source=img_path,
                size_hint=(0.8, 0.8),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                allow_stretch=True
            )
            logger.info("Image loaded successfully.")
        else:
            self.main_img = Label(text="[ Image Missing ]", color=(1,0,0,1))
            logger.error("Image file NOT found in directory.")

        # Adding widgets to layout
        self.root_layout.add_widget(self.main_img)
        self.root_layout.add_widget(self.status_label)

        # Start a simple animation timer
        Clock.schedule_interval(self.animate_ui, 1.0 / 30.0)
        
        return self.root_layout

    def _update_rect(self, instance, value):
        self.rect.pos = (0, 0)
        self.rect.size = value

    def animate_ui(self, dt):
        # Yahan hum future mein pulse animation dalenge
        pass

    def on_start(self):
        logger.info("App Started Successfully")
        self.status_label.text = "Zera AI: Online"

    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ == '__main__':
    try:
        ZeraApp().run()
    except Exception as e:
        logger.error(f"Fatal Error: {str(e)}")
