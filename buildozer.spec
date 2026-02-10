[app]
# (str) Title of your application
title = Zera AI Voice Assistant

# (str) Package name
package.name = zera_ai_pro

# (str) Package domain
package.domain = org.zera.assistant

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# Note: Humne pyaudio hata diya hai kyunki wo Android par build fail karta hai.
requirements = python3,kivy==2.2.1,kivymd,pillow,pyjnius,android

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions 
# Isme wo saari permissions hain jo ek AI assistant ko chahiye
android.permissions = INTERNET, CAMERA, FLASHLIGHT, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, VIBRATE, FOREGROUND_SERVICE

# (int) Target Android API
android.api = 31

# (int) Minimum API
android.minapi = 21

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) automatically accept SDK license
android.accept_sdk_license = True

# (str) Android logcat filters
android.logcat_filters = *:S python:D

[buildozer]
# (int) Log level (2 = full debug logs)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
