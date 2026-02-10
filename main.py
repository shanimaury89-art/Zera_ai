import os
from kivy.app import App
from kivy.uix.image import Image
from jnius import autoclass
import threading
import speech_recognition as sr

# Android Java Classes
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')

class ZeraApp(App):
    def build(self):
        # Aapki image load ho rahi hai
        self.img = # main.py ke andar line update karein
self.img = Image(source='1770689044948.jpg', size_hint=(0.6, 0.6), 
                 pos_hint={'center_x': 0.5, 'center_y': 0.5})

        
        threading.Thread(target=self.zera_listener, daemon=True).start()
        return self.img

    def zera_listener(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            while True:
                try:
                    audio = r.listen(source, phrase_time_limit=3)
                    text = r.recognize_google(audio).lower()
                    if "zera" in text:
                        # Command example: "Zera open Facebook"
                        self.handle_universal_command(text)
                except:
                    pass

    def handle_universal_command(self, cmd):
        if "open" in cmd:
            # "open" ke baad wala app ka naam nikalna
            app_to_open = cmd.split("open")[-1].strip()
            self.launch_app_by_name(app_to_open)
        
        elif "flashlight on" in cmd:
            self.set_flashlight(True)
        elif "flashlight off" in cmd:
            self.set_flashlight(False)

    def launch_app_by_name(self, app_name):
        activity = PythonActivity.mActivity
        pm = activity.getPackageManager()
        main_intent = autoclass('android.content.Intent')(autoclass('android.content.Intent').ACTION_MAIN)
        main_intent.addCategory(autoclass('android.content.Intent').CATEGORY_LAUNCHER)
        
        apps = pm.queryIntentActivities(main_intent, 0)
        
        for i in range(apps.size()):
            info = apps.get(i)
            label = str(info.loadLabel(pm)).lower()
            
            if app_name in label:
                package_name = info.activityInfo.packageName
                launch_intent = pm.getLaunchIntentForPackage(package_name)
                if launch_intent:
                    activity.startActivity(launch_intent)
                    return

    def set_flashlight(self, state):
        activity = PythonActivity.mActivity
        cameraManager = activity.getSystemService(Context.CAMERA_SERVICE)
        cameraId = cameraManager.getCameraIdList()[0]
        cameraManager.setTorchMode(cameraId, state)

if __name__ == '__main__':
    ZeraApp().run()
