import os
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
import threading
import speech_recognition as sr

# Background transparent karne ke liye (Android par permission chahiye hogi)
Window.clearcolor = (0, 0, 0, 0) 

class ZeraApp(App):
    def build(self):
        # Aapki wo glowing ring image yahan load hogi
        # Ensure karein ki 'zera_ring.png' file same folder mein ho
        self.img = Image(source='1770689181484.jpg', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        # Background mein voice sunne ke liye thread chalu karna
        threading.Thread(target=self.start_listening, daemon=True).start()
        
        return self.img

    def start_listening(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            while True:
                try:
                    # 'Hey Zera' sunne ka intezar
                    audio = recognizer.listen(source, phrase_time_limit=3)
                    command = recognizer.recognize_google(audio).lower()
                    
                    if "zera" in command:
                        print("Zera Active!")
                        self.process_command(command)
                except:
                    pass

    def process_command(self, cmd):
        if "open whatsapp" in cmd:
            os.system("am start -n com.whatsapp/.Main")
        elif "open youtube" in cmd:
            os.system("am start -n com.google.android.youtube/com.google.android.apps.youtube.app.watchwheel.WatchWheelActivity")
        elif "flashlight on" in cmd:
            # Native Android command
            os.system("cmd notification post -S bigtext 'Zera' 'Flashlight On'") 
            # Note: Flashlight ke liye professional APK mein Java Bridge use hota hai

    def on_stop(self):
        # App band hone par cleanup
        pass

if __name__ == '__main__':
    ZeraApp().run()
