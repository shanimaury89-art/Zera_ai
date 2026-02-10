import os
import threading
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock

# Android special features ke liye jnius use hota hai
try:
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Context = autoclass('android.content.Context')
except:
    PythonActivity = None
    Context = None

class ZeraApp(App):
    def build(self):
        # Aapki glowing ring image yahan load hogi
        # Size aur position center mein rakhi hai
        self.img = Image(
            source='1770689044948.jpg', 
            size_hint=(0.7, 0.7), 
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        return self.img

    def on_start(self):
        # App start hote hi agar kuch check karna ho
        print("Zera AI is starting...")

    def set_flashlight(self, state):
        """Android Flashlight control karne ke liye function"""
        if not PythonActivity:
            return
            
        try:
            activity = PythonActivity.mActivity
            cameraManager = activity.getSystemService(Context.CAMERA_SERVICE)
            cameraId = cameraManager.getCameraIdList()[0]
            cameraManager.setTorchMode(cameraId, state)
        except Exception as e:
            print(f"Flashlight error: {e}")

    def launch_app_by_name(self, app_name):
        """Android apps open karne ke liye function"""
        if not PythonActivity:
            return
            
        try:
            activity = PythonActivity.mActivity
            pm = activity.getPackageManager()
            main_intent = autoclass('android.content.Intent')(autoclass('android.content.Intent').ACTION_MAIN)
            main_intent.addCategory(autoclass('android.content.Intent').CATEGORY_LAUNCHER)
            
            apps = pm.queryIntentActivities(main_intent, 0)
            
            for i in range(apps.size()):
                info = apps.get(i)
                label = str(info.loadLabel(pm)).lower()
                
                if app_name.lower() in label:
                    package_name = info.activityInfo.packageName
                    launch_intent = pm.getLaunchIntentForPackage(package_name)
                    if launch_intent:
                        activity.startActivity(launch_intent)
                        return
        except Exception as e:
            print(f"App launch error: {e}")

if __name__ == '__main__':
    ZeraApp().run()
