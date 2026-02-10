[app]
title = Zera AI
package.name = zeraai
package.domain = org.zera
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Requirements (Isme koi galti nahi honi chahiye)
requirements = python3,kivy==2.2.1,kivymd,pillow,pyjnius

orientation = portrait
fullscreen = 1

# Permissions
android.permissions = INTERNET, CAMERA, FLASHLIGHT, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Android specific (Important for GitHub Actions)
android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
