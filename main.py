import os
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

# Android features (jnius) ko safely handle karne ke liye
try:
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Context = autoclass('android.content.Context')
except Exception as e:
    PythonActivity = None
    Context = None
    print(f"Not running on Android or jnius missing: {e}")

class ZeraApp(App):
    def build(self):
        # Background layout
        self.layout = FloatLayout()
        
        # Image name (Vahi jo aapne upload ki hai)
        img_name = '1770689044948.jpg'
        
        # Check if image exists before loading
        if os.path.exists(img_name):
            self.img = Image(
                source=img_name,
                size_hint=(0.8, 0.8),
                pos_hint={'center_x': 0.5, 'center_y': 0.5}
            )
        else:
            # Agar image nahi mili toh placeholder show karega
            self.img = Image(
                pos_hint={'center_x': 0.5, 'center_y': 0.5}
            )
            print("Warning: Image file not found in repository!")

        self.layout.add_widget(self.img)
        return self.layout

    def on_start(self):
        print("Zera AI has started successfully!")

    def set_flashlight(self, state):
        """Android Flashlight control (Experimental)"""
        if not PythonActivity:
            return
        try:
            activity = PythonActivity.mActivity
            cameraManager = activity.getSystemService(Context.CAMERA_SERVICE)
            cameraId = cameraManager.getCameraIdList()[0]
            cameraManager.setTorchMode(cameraId, state)
        except Exception as e:
            print(f"Flashlight error: {e}")

if __name__ == '__main__':
    ZeraApp().run()
