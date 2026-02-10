[app]
title = Zera AI
package.name = zeraai
package.domain = org.zera
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Requirements: Isme se pyaudio hata diya hai taaki build pass ho
requirements = python3,kivy,kivymd,pillow,pyjnius

orientation = portrait
fullscreen = 1

# Permissions: Flashlight aur Mic ke liye
android.permissions = INTERNET, CAMERA, FLASHLIGHT, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Archs: Dono 32-bit aur 64-bit phones ke liye
android.archs = arm64-v8a, armeabi-v7a

# License accept karna zaroori hai
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
