import os
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

class ZeraApp(App):
    def build(self):
        self.layout = FloatLayout()
        
        # Image ka sahi naam jo aapne upload kiya hai
        img_name = '1770689044948.jpg'
        
        if os.path.exists(img_name):
            self.img = Image(
                source=img_name,
                size_hint=(0.8, 0.8),
                pos_hint={'center_x': 0.5, 'center_y': 0.5}
            )
        else:
            # Agar image nahi mili toh black screen na dikhe
            self.img = Image(pos_hint={'center_x': 0.5, 'center_y': 0.5})
            print("Image not found!")

        self.layout.add_widget(self.img)
        return self.layout

if __name__ == '__main__':
    ZeraApp().run()
